#!/usr/bin/env python3
"""
Parse the KNX Datapoint Types markdown file and produce dpt_new.json.

Strategy:
  1. Parse the Overview table (section 2) for the full DPT list (ID, format, name).
  2. Parse the detailed sections (3+) for ranges, units, resolution, encoding,
     value_map, use_scope, application_domain, notes.
  3. Derive data_type_category, size_bits, size_bytes from the format code.
  4. Merge everything and output JSON matching the existing schema.
"""

import json
import math
import re
import sys
from pathlib import Path

MD_PATH = Path(__file__).parent / "output.md"
OUTPUT_PATH = Path(__file__).parent / "dpt_new2.json"

# ── Format code → size + category mappings ──────────────────────────────────

FORMAT_SIZE_BITS = {
    "B1": 1,
    "B2": 2,
    "B1U3": 4,
    "A8": 8,
    "U8": 8,
    "V8": 8,
    "N8": 8,
    "B5N3": 8,
    "r2U6": 8,
    "B1r1U6": 8,
    "U16": 16,
    "V16": 16,
    "F16": 16,
    "U8N8": 16,
    "N3U5r2U6r2U6": 24,
    "r3U5r4U4r1U7": 24,
    "U32": 32,
    "V32": 32,
    "F32": 32,
    "U4U4U4U4U4U4B4N4": 32,
    "U16F16": 32,
    "A112": 112,
    "U8r4U4r3U5U3U5r2U6r2U6B16": 64,
}

FORMAT_CATEGORY = {
    "B1": "boolean",
    "B2": "composite",
    "B1U3": "composite",
    "A8": "character",
    "U8": "unsigned",
    "V8": "signed",
    "N8": "enum",
    "B8": "bitset",
    "B16": "bitset",
    "B24": "bitset",
    "B32": "bitset",
    "B5N3": "composite",
    "r2U6": "unsigned",
    "B1r1U6": "composite",
    "U16": "unsigned",
    "V16": "signed",
    "F16": "float",
    "U8N8": "composite",
    "N3U5r2U6r2U6": "composite",
    "r3U5r4U4r1U7": "composite",
    "U32": "unsigned",
    "V32": "signed",
    "F32": "float",
    "U4U4U4U4U4U4B4N4": "composite",
    "U16F16": "composite",
    "A112": "string",
    "U8r4U4r3U5U3U5r2U6r2U6B16": "composite",
}

# Sparkplug data type mapping (same as add_data_type.py)
DATA_TYPES = {
    "Unknown": 0, "Int8": 1, "Int16": 2, "Int32": 3, "Int64": 4,
    "UInt8": 5, "UInt16": 6, "UInt32": 7, "UInt64": 8,
    "Float": 9, "Double": 10, "Boolean": 11, "String": 12,
    "DateTime": 13, "Text": 14, "Bytes": 17,
}

DATETIME_MAIN_NUMBERS = {10, 11, 19}


def resolve_sparkplug_type(row: dict) -> str:
    category = row.get("data_type_category")
    size_bits = row.get("size_bits")
    main = row.get("dpt_main_number")

    if main in DATETIME_MAIN_NUMBERS:
        return "DateTime"
    if category == "boolean":
        return "Boolean"
    if category == "signed":
        return {8: "Int8", 16: "Int16", 32: "Int32", 64: "Int64"}.get(size_bits, "Bytes")
    if category == "unsigned":
        return {8: "UInt8", 16: "UInt16", 32: "UInt32", 64: "UInt64"}.get(size_bits, "UInt8")
    if category == "float":
        return "Float"
    if category == "enum":
        return "UInt8"
    if category in ("character", "string"):
        return "String"
    if category == "bitset":
        return {8: "UInt8", 16: "UInt16", 24: "Bytes", 32: "UInt32", 64: "UInt64"}.get(size_bits, "Bytes")
    if category == "composite":
        return "Bytes"
    return "Unknown"


def guess_size_bits(fmt: str) -> int | None:
    """Heuristic: sum up bit-widths from format code tokens."""
    if fmt in FORMAT_SIZE_BITS:
        return FORMAT_SIZE_BITS[fmt]
    # Try to calculate from tokens like U8, B1, F16, r3, N4, V32, A112, etc.
    total = 0
    for token in re.findall(r'[A-Za-z]\d+', fmt):
        bits = int(token[1:])
        total += bits
    # Handle bracketed repetitions like [4], [5] etc. -- rough heuristic
    if total > 0:
        return total
    return None


def guess_category(fmt: str, main: int) -> str:
    if fmt in FORMAT_CATEGORY:
        return FORMAT_CATEGORY[fmt]
    if main in DATETIME_MAIN_NUMBERS:
        return "composite"
    # Multi-field formats where ALL tokens are the same base type
    field_tokens = re.findall(r'[A-Za-z]\d+', fmt)
    if len(field_tokens) > 1:
        # All-A tokens (e.g., A8A8, A8A8A8A8) = string
        if all(t.startswith('A') for t in field_tokens):
            return "string"
        return "composite"
    # Bitset formats: B followed by number (B8, B16, B24, B32)
    if re.match(r'^B\d+$', fmt) and fmt != 'B1':
        return "bitset"
    if fmt.startswith("B1") and len(fmt) == 2:
        return "boolean"
    if fmt.startswith("N"):
        return "enum"
    if fmt.startswith("F"):
        return "float"
    if fmt.startswith("U") and not any(c.isalpha() and c != 'U' for c in fmt[1:]):
        return "unsigned"
    if fmt.startswith("V"):
        return "signed"
    if fmt.startswith("A"):
        return "string"
    return "composite"


def parse_overview_table(text: str) -> list[dict]:
    """
    Parse section 2 'Overview' table.
    Rows are like: |1.001|B1|DPT_Switch|
    """
    entries = []
    in_overview = False
    # Match table rows with DPT ID pattern
    row_re = re.compile(
        r'^\|(\d+\.\d+)\|([A-Za-z0-9_\[\]\(\) <>]+)\|([A-Za-z0-9_/\-]+)\|',
    )

    for line in text.splitlines():
        if "## **2 Overview**" in line or "## 2 Overview" in line:
            in_overview = True
            continue
        if in_overview and line.startswith("## **3 "):
            break
        if not in_overview:
            continue

        m = row_re.match(line)
        if m:
            dpt_id = m.group(1).strip()
            fmt_raw = m.group(2).strip()
            name = m.group(3).strip()
            # Clean up format codes: remove <br> tags and whitespace
            fmt = re.sub(r'<br\s*/?>', '', fmt_raw).strip()
            entries.append({
                "dpt_id": dpt_id,
                "format_code": fmt,
                "dpt_name": name,
            })

    return entries


def parse_number(s: str) -> float | int | None:
    """Parse a number from a (possibly noisy) string."""
    if not s:
        return None
    s = s.strip().replace('\u00a0', '').replace(' ', '')
    s = s.replace(',', '.')
    s = re.sub(r'[^\d.\-+eE]', '', s)
    if not s:
        return None
    try:
        v = float(s)
        return int(v) if v == int(v) else v
    except ValueError:
        return None


KNOWN_UNITS = {
    '%', '°', '°C', '°F', 'K', 'K/h', 'K/%',
    'lux', 'Lux', 'ms', 's', 'min', 'h',
    'mV', 'V', 'mA', 'A', 'W', 'kW', 'MW', 'VA', 'VAR',
    'Wh', 'kWh', 'MWh', 'VAh', 'kVAh', 'VARh', 'kVARh',
    'Pa', 'ppm', 'Hz',
    'm', 'mm', 'km', 'km/h',
    'm/s', 'm²', 'm2', 'm3', 'm³', 'm3/h', 'm3/s',
    'kg', 'kg/h', 'l/h', 'l/m2',
    'J', 'J/h', 'kJ', 'kJ/h',
    'counter pulses', 'pulses', 'ratio', 'litre',
    'none', 'n.a.',
    # F32 physical units (with proper SI spacing)
    'ms-2', 'rad', 'rad s-2', 'rad s-1', 'J mol-1', 's-1', 'mol',
    'J s', 'N', 'N s-1', 'Nm', 'Nm-1', 'N m-2',
    'F', 'C', 'C m', 'C m-2', 'C m-3',
    'm2 N-1', 'S', 'S m-1', 'Ω', 'Ωm',
    'kg m-3', 'kg s-1',
    'A m-1', 'A m2', 'A m-2',
    'V m-1', 'V K-1',
    'Wb', 'T', 'H',
    'W m-1 K-1', 'W m-2', 'W/m2',
    'J K-1', 'JK-1', 'J s', 'J or lm s',
    'cd', 'cd m-2', 'lm', 'sr',
    'm s-1', 'gm-3', 'm3 s-1', 'm3 h-1', 'l s-1',
    'µg', 'µgm-3',
}
KNOWN_UNITS_LOWER = {u.lower() for u in KNOWN_UNITS}

# OCR spacing corrections for compound SI units
# The markdown OCR often drops spaces between SI unit factors
UNIT_OCR_FIXES = {
    'm2N-1': 'm2 N-1',
    'kgm-3': 'kg m-3',
    'kgs-1': 'kg s-1',
    'm3s-1': 'm3 s-1',
    'm3h-1': 'm3 h-1',
    'ls-1': 'l s-1',
    'W m-1K-1': 'W m-1 K-1',
    'µgm-3': 'µg m-3',
    # Unicode normalization: U+2126 (Ohm sign) → U+03A9 (Greek capital Omega)
    '\u2126': 'Ω',
    '\u2126m': 'Ωm',
}


def extract_value_map_from_text(text: str) -> dict:
    """Extract value map from text that contains patterns like:
    '0 = Off', '1 = On', '0 : autonomous', '1 : slave', etc.
    Handles <br> line separators and multi-line cell content.
    """
    # Normalize: replace <br> with newlines
    normalized = re.sub(r'<br\s*/?>', '\n', text)
    value_map = {}

    # Pattern 1: "N = label" (B1 style)
    # Pattern 2: "N : label" (N8 style)
    # Pattern 3: "N= label" or "N =label" (variants)
    for m in re.finditer(
        r'(?:^|\n)\s*(\d+)\s*[=:]\s*([A-Za-z][^\n\d]*?)(?=\n\s*\d+\s*[=:]|\n\s*\d+\s+to\s|\n\s*(?:other|reserved)|$)',
        normalized,
        re.MULTILINE
    ):
        key = m.group(1).strip()
        val = m.group(2).strip().rstrip(',. ')
        # Skip reserved/not used/shall not be used
        if val and not re.match(r'(?:reserved|not used|shall not)', val, re.IGNORECASE):
            if len(val) < 100:
                value_map[key] = val

    # Also try inline format: "0 = Off 1 = On" in same segment
    if not value_map:
        for m in re.finditer(
            r'(\d+)\s*[=:]\s*([A-Za-z][\w\s\-\(\)/,\.]+?)(?=\s+\d+\s*[=:]|$)',
            normalized
        ):
            key = m.group(1).strip()
            val = m.group(2).strip().rstrip(',. ')
            if val and not re.match(r'(?:reserved|not used|shall not)', val, re.IGNORECASE):
                if len(val) < 100:
                    value_map[key] = val

    return value_map


def extract_range_from_text(text: str) -> tuple:
    """Extract (min, max) range values from text.
    Handles formats like: [0…100], [-273 °C … 670 433,28°C], [0 to 3],
    0 mm … 65 535 mm, -32 768 … 32 767, {0,1}
    """
    cleaned = re.sub(r'<br\s*/?>', ' ', text)

    # Pattern 1: [min … max] or [min...max] with optional units embedded
    m = re.search(
        r'\[?\s*(-?[\d\s,.]+)\s*(?:[A-Za-z°/²³µ]+(?:-\d+)?)?\s*(?:…|\.\.\.)\s*(-?[\d\s,.]+)\s*(?:[A-Za-z°/²³µ]+(?:-\d+)?)?\s*\]?',
        cleaned
    )
    if m:
        vmin = parse_number(m.group(1))
        vmax = parse_number(m.group(2))
        if vmin is not None and vmax is not None:
            return (vmin, vmax)

    # Pattern 2: [min to max]
    m = re.search(
        r'\[\s*(-?\d+)\s+to\s+(-?\d+)\s*\]',
        cleaned
    )
    if m:
        return (int(m.group(1)), int(m.group(2)))

    # Pattern 3: min unit … max unit (e.g., "0 ms … 65 535 ms", "0 gm-3… 670 760 gm-3")
    m = re.search(
        r'(-?[\d\s,.]+)\s*(?:[A-Za-z°/²³µ]+(?:-\d+)?)?\s*(?:…|\.\.\.)\s*(-?[\d\s,.]+)\s*(?:[A-Za-z°/²³µ]+(?:-\d+)?)?',
        cleaned
    )
    if m:
        vmin = parse_number(m.group(1))
        vmax = parse_number(m.group(2))
        if vmin is not None and vmax is not None:
            return (vmin, vmax)

    # Pattern 4: {0,1} for boolean
    m = re.search(r'\{0\s*,\s*1\}', cleaned)
    if m:
        return (0, 1)

    return (None, None)


def extract_unit_from_cell(cell: str) -> str | None:
    """Extract a unit from a table cell."""
    cleaned = re.sub(r'<br\s*/?>', ' ', cell).strip()

    # Skip hex values like FFh, 80h, etc.
    if re.match(r'^[0-9A-Fa-f]+h$', cleaned):
        return None

    # Skip KNX encoding format codes: U8, N8, F16, F32, B1Z8, U8U8B16, r2U6, etc.
    # Format code segments use letters U/V/N/F/B/Z/A/r/b followed by digits.
    # First check against known units to not accidentally filter SI units (m2, m3).
    if cleaned.lower() not in KNOWN_UNITS_LOWER and cleaned not in KNOWN_UNITS:
        if re.match(r'^(?:[UVNFBZArbh]\d{1,3})+$', cleaned):
            return None

    # Skip application domain / use_scope labels (not units)
    NOT_UNITS = {
        'hvac', 'hwh', 'tu', 'lighting', 'metering', 'vac', 'foci',
        'general', 'busy', 'scenenumber',
        'g', 'fb', 'use', 'name', 'id', 'pdt', 'range', 'resol',
        'none', 'see', 'below', 'encoding', 'field', 'comment',
        'description', 'types', 'datapoint', 'type', 'format',
        'conditions', 'applications', 'binary', 'encoded',
        'b', 'on', 'off', 'up', 'down', 'no', 'yes',
        'day', 'msb', 'lsb', 'value', 'time', 'date', 'mode',
        'to', 'from', 'and', 'or', 'the', 'of', 'in', 'for',
        'reserved', 'default', 'false', 'true', 'bit', 'system',
    }
    if cleaned.lower() in NOT_UNITS:
        return None

    # Direct match against known units
    if cleaned.lower() in KNOWN_UNITS_LOWER or cleaned in KNOWN_UNITS:
        if cleaned.lower() not in ('none', 'n.a.'):
            return cleaned

    # Short unit pattern: °C, %, mV, W/m2, m3/h, etc.
    # Allow digits inside units (m2, m3, W/m2, l/m2, gm-3, etc.)
    if re.match(r'^[°µ%]?[A-Za-z0-9²³/·\-]+$', cleaned) and len(cleaned) <= 12:
        if cleaned.lower() not in NOT_UNITS and len(cleaned) >= 2:
            return cleaned

    # Check if cell contains "unit" + space + value pattern (e.g., "°C 100")
    m = re.match(r'^([°µ%]?[A-Za-z0-9²³/·\-]{1,12})\s+(\d+)$', cleaned)
    if m and len(m.group(1)) >= 2 and len(m.group(1)) <= 12:
        candidate = m.group(1)
        if candidate.lower() not in NOT_UNITS:
            return candidate

    return None


def extract_unit_from_range_text(text: str) -> str | None:
    """Try to extract unit from a range string like '-273 °C … 670 433,28°C'."""
    cleaned = re.sub(r'<br\s*/?>', ' ', text).strip()
    # Look for unit attached at the end of range
    m = re.search(r'[\d,.]\s*([°µ]?[A-Za-z][A-Za-z²³/·\-]*)\s*$', cleaned)
    if m:
        candidate = m.group(1).strip()
        if candidate.lower() in KNOWN_UNITS_LOWER or candidate in KNOWN_UNITS:
            return candidate
        # Short physical units
        if len(candidate) <= 8 and candidate.lower() not in (
            'to', 'and', 'or', 'the', 'see', 'a', 'an',
            'reserved', 'default', 'false', 'true', 'used',
        ):
            return candidate
    return None


def extract_resolution_from_cell(cell: str) -> str | None:
    """Extract resolution from a table cell."""
    cleaned = re.sub(r'<br\s*/?>', ' ', cell).strip()

    # Skip if it looks like it's not a resolution
    if 'DPT' in cleaned or 'PDT' in cleaned or 'APPLICATIONS' in cleaned:
        return None
    if cleaned.lower() in ('not applicable', '(not applicable)', 'n.a.', 'none', ''):
        return None
    # Skip if it looks like a DPT ID (e.g., "1.001", "20.002")
    if re.match(r'^\d+\.\d{2,4}$', cleaned):
        return None

    # Pattern: ≈0,4 % or 0,01 °C or 1 pulse or 1 mm or 0,01 W/m2
    m = re.match(r'^[≈~]?\s*([\d.,]+)\s*([%°]?[A-Za-z0-9²³/·\-\s]*)', cleaned)
    if m and m.group(1):
        val = m.group(1).strip()
        # Skip bare "0" — resolution of zero is meaningless; it's a range boundary
        if val == '0':
            return None
        # Normalize European decimal comma → dot
        val = val.replace(',', '.')
        unit = m.group(2).strip()
        if unit:
            return f"{val} {unit}"
        return val

    return None


def extract_detail_blocks(text: str) -> dict[str, dict]:
    """
    Extract detailed information for each DPT from the body of the markdown.
    Returns a dict keyed by dpt_id with fields: description, unit, resolution,
    encoding, value_min, value_max, use_scope, application_domain, value_map, notes.

    Uses a multi-pass approach:
    1. Find table rows with DPT IDs and parse cells
    2. Gather context lines around each DPT for additional extraction
    3. Use format-family heuristics for missing fields
    """
    details: dict[str, dict] = {}
    lines = text.splitlines()

    # Build a map of DPT ID → line indices where it appears
    dpt_row_re = re.compile(r'^\|[\s|]*(\d+\.\d+)\|')
    dpt_lines: dict[str, list[int]] = {}
    for i, line in enumerate(lines):
        m = dpt_row_re.match(line)
        if m:
            dpt_id = m.group(1).strip()
            dpt_lines.setdefault(dpt_id, []).append(i)

    # ── Find table headers to map columns ──
    # Headers contain keywords like "ID:", "Name:", "Range:", "Unit:", "Resol.:", "Use:", "Encoding:", "Comment:"
    header_re = re.compile(r'^\|.*(?:ID:|Name:).*\|$')

    for dpt_id, line_indices in dpt_lines.items():
        info: dict = {}

        for li in line_indices:
            line = lines[li]
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]

            if len(cells) < 2:
                continue

            # ── Flatten the entire row text for broad pattern matching ──
            row_text = re.sub(r'<br\s*/?>', '\n', line)

            # ── DPT Name ──
            for cell in cells[1:]:
                cleaned = re.sub(r'<br\s*/?>', ' ', cell).strip()
                if cleaned.startswith("DPT_"):
                    name_match = re.match(r'(DPT_[\w/\-]+)', cleaned)
                    if name_match:
                        info["dpt_name"] = name_match.group(1)
                    break

            # ── Value Map ──
            # Collect all cell text for value_map extraction
            for cell in cells:
                cell_text = re.sub(r'<br\s*/?>', '\n', cell)
                # Only look in cells that have the number : label or number = label pattern
                if re.search(r'\d+\s*[=:]\s*[A-Za-z]', cell_text):
                    vm = extract_value_map_from_text(cell_text)
                    if vm and len(vm) >= 2:
                        old_vm = info.get("value_map", {})
                        if len(vm) > len(old_vm):
                            info["value_map"] = vm

            # ── Use Scope ──
            for cell in cells:
                c = cell.strip()
                # Exact match for G or FB (possibly with footnote markers)
                if re.match(r'^(G|FB)\s*(?:\d+\)|[a-z]\)|SAB)?\s*$', c):
                    info["use_scope"] = "G" if c.startswith("G") else "FB"
                    break

            # ── Range ──
            for cell in cells:
                cell_clean = re.sub(r'<br\s*/?>', ' ', cell)
                vmin, vmax = extract_range_from_text(cell_clean)
                if vmin is not None:
                    info["value_min"] = vmin
                    info["value_max"] = vmax
                    # Also try to get unit from the range text
                    if "unit" not in info:
                        u = extract_unit_from_range_text(cell_clean)
                        if u:
                            info["unit"] = u
                    break

            # ── Identify range-related cell indices to skip ──
            # When "to" appears as a separate cell, adjacent cells are range
            # boundaries (e.g., |R:|0|to|255|) and must not be parsed as
            # unit or resolution.
            range_cell_indices = set()
            for idx, cell in enumerate(cells):
                if cell.strip().lower() == 'to':
                    range_cell_indices.add(idx)
                    if idx > 0:
                        range_cell_indices.add(idx - 1)
                    if idx + 1 < len(cells):
                        range_cell_indices.add(idx + 1)

            # ── Unit ──
            if "unit" not in info:
                for idx, cell in enumerate(cells):
                    if idx in range_cell_indices:
                        continue
                    u = extract_unit_from_cell(cell)
                    if u:
                        info["unit"] = u
                        break

            # ── Resolution ──
            if "resolution" not in info:
                for idx, cell in enumerate(cells):
                    if idx in range_cell_indices:
                        continue
                    r = extract_resolution_from_cell(cell)
                    if r:
                        info["resolution"] = r
                        break

            # ── F32 column-aware unit + description extraction ──
            # For 14.xxx types, table has: |ID:|Name:|Unit:|Comment:|Use:|
            # cell[0]=ID, cell[1]=Name, cell[2]=Unit, cell[3]=Comment, cell[4]=Use
            main_num = int(dpt_id.split(".")[0])
            if main_num == 14 and len(cells) >= 4:
                # Extract unit from the dedicated Unit column (index 2)
                unit_cell = re.sub(r'<br\s*/?>', ' ', cells[2]).strip()
                # "-" means no unit (dimensionless)
                if unit_cell and unit_cell != '-':
                    # Strip footnote markers like 10) and equation forms like "Hz = s-1"
                    unit_clean = re.sub(r'\d+\)\s*$', '', unit_cell).strip()
                    unit_clean = re.split(r'\s*=\s*', unit_clean)[0].strip()
                    if unit_clean and unit_clean.lower() not in ('none', 'n.a.'):
                        info["unit"] = unit_clean
                elif unit_cell == '-':
                    info["unit"] = None  # explicitly no unit
                # Extract description from the Comment column (index 3)
                if len(cells) >= 4:
                    comment_cell = re.sub(r'<br\s*/?>', ' ', cells[3]).strip()
                    if comment_cell and len(comment_cell) > 2 and 'DPT' not in comment_cell:
                        info["description"] = comment_cell

        # ── Also scan context lines around DPT rows for extra info ──
        for li in line_indices:
            # Look at 5 lines before and after for additional context
            context_start = max(0, li - 5)
            context_end = min(len(lines), li + 6)
            for ci in range(context_start, context_end):
                if ci == li:
                    continue
                ctx = lines[ci]
                # Skip if this line is another DPT ID row
                if dpt_row_re.match(ctx):
                    continue
                # Range from context
                if "value_min" not in info:
                    ctx_clean = re.sub(r'<br\s*/?>', ' ', ctx)
                    vmin, vmax = extract_range_from_text(ctx_clean)
                    if vmin is not None:
                        info["value_min"] = vmin
                        info["value_max"] = vmax

        # Store / merge
        if dpt_id not in details:
            details[dpt_id] = info
        else:
            for k, v in info.items():
                if k not in details[dpt_id] or (
                    k == "value_map" and isinstance(v, dict)
                    and len(v) > len(details[dpt_id].get("value_map", {}))
                ):
                    details[dpt_id][k] = v

    return details


def derive_description(dpt_name: str) -> str:
    """Generate a human-readable description from the DPT name."""
    # Remove DPT_ prefix
    name = dpt_name.replace("DPT_", "")
    # Split on underscores and CamelCase
    parts = name.replace("_", " ")
    # Clean up
    return parts.strip()


def get_application_domain(dpt_id: str, use_scope: str) -> str:
    """Determine application domain from DPT sub number."""
    parts = dpt_id.split(".")
    if len(parts) == 2:
        sub = int(parts[1])
        if sub >= 1200:
            return "metering"
        if 1000 <= sub < 1200:
            return "system"
        if 800 <= sub < 1000:
            return "shutters_blinds"
        if sub >= 600:
            return "lighting"
        if sub >= 100:
            return "hvac"
    return "common"


def build_json(overview: list[dict], details: dict[str, dict]) -> list[dict]:
    """Combine overview + detail data into the final JSON structure."""
    results = []

    for entry in overview:
        dpt_id = entry["dpt_id"]
        fmt = entry["format_code"]
        name = entry["dpt_name"]

        parts = dpt_id.split(".")
        main = int(parts[0])
        sub = int(parts[1])

        dt = details.get(dpt_id, {})

        # Size
        size_bits = guess_size_bits(fmt)
        if size_bits is None:
            size_bits = 8  # fallback
        size_bytes = size_bits / 8
        if size_bytes == int(size_bytes):
            size_bytes = int(size_bytes)
        # Convention for sub-byte sizes (matching existing KNX data)
        if size_bits < 8:
            SUB_BYTE_MAP = {1: 0.1, 2: 0.3, 3: 0.4, 4: 0.5}
            size_bytes = SUB_BYTE_MAP.get(size_bits, round(size_bits / 8, 1))
        elif size_bytes != int(size_bytes):
            # Non-whole bytes above 1 byte: round up to next whole octet
            # (KNX protocol always transmits whole octets)
            size_bytes = math.ceil(size_bytes)

        # Category
        category = guess_category(fmt, main)

        # Use scope
        use_scope = dt.get("use_scope", "G")

        # Application domain
        app_domain = get_application_domain(dpt_id, use_scope)

        # Value map
        value_map = dt.get("value_map") or None
        # Capitalize first letter of each value_map label for consistency
        if value_map:
            value_map = {k: v[0].upper() + v[1:] if v else v for k, v in value_map.items()}
            # Fix CamelCase concatenation: "SceneB" → "Scene B", "Apparentpower" → "Apparent power"
            fixed_vm = {}
            for k, v in value_map.items():
                # Insert space before uppercase letter preceded by lowercase
                v = re.sub(r'([a-z])([A-Z])', r'\1 \2', v)
                # Insert space before lowercase preceded by uppercase+uppercase (acronym boundary)
                v = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', v)
                fixed_vm[k] = v
            value_map = fixed_vm

        # ── DPT 2.x: generate value_map from corresponding DPT 1.x ──
        # DPT 2.xxx is the "controlled" version of DPT 1.xxx with c=control, v=value
        if main == 2 and not value_map:
            # Map DPT 2.x sub to DPT 1.x sub (same sub number)
            B2_VALUE_LABELS = {
                1: ("Off", "On"),       # Switch
                2: ("False", "True"),    # Bool
                3: ("Disable", "Enable"),  # Enable
                4: ("No ramp", "Ramp"),  # Ramp
                5: ("No alarm", "Alarm"),  # Alarm
                6: ("Low", "High"),      # BinaryValue
                7: ("Decrease", "Increase"),  # Step
                8: ("Up", "Down"),       # Direction1
                9: ("Open", "Close"),    # Direction2
                10: ("Stop", "Start"),   # Start
                11: ("Inactive", "Active"),  # State
                12: ("Not inverted", "Inverted"),  # Invert
            }
            labels = B2_VALUE_LABELS.get(sub)
            if labels:
                value_map = {
                    "0": f"No control, {labels[0]}",
                    "1": f"No control, {labels[1]}",
                    "2": f"Control, {labels[0]}",
                    "3": f"Control, {labels[1]}",
                }

        # Range
        value_min = dt.get("value_min")
        value_max = dt.get("value_max")

        # Unit
        unit = dt.get("unit")
        # Apply OCR spacing corrections for compound SI units
        if unit and unit in UNIT_OCR_FIXES:
            unit = UNIT_OCR_FIXES[unit]
        # Boolean types don't have physical units
        if category == "boolean":
            unit = None

        # Resolution
        resolution = dt.get("resolution")
        # Boolean types don't have resolution
        if category == "boolean":
            resolution = None

        # ── Apply format-family defaults for missing fields ──
        if value_min is None and value_max is None:
            if fmt == "B1":
                value_min, value_max = 0, 1
            elif fmt == "B2":
                value_min, value_max = 0, 3
            elif fmt == "U8":
                value_min, value_max = 0, 255
            elif fmt == "V8":
                value_min, value_max = -128, 127
            elif fmt == "U16":
                value_min, value_max = 0, 65535
            elif fmt == "V16":
                value_min, value_max = -32768, 32767
            elif fmt == "F16":
                value_min, value_max = -671088.64, 670433.28
            elif fmt == "U32":
                value_min, value_max = 0, 4294967295
            elif fmt == "V32":
                value_min, value_max = -2147483648, 2147483647
            elif fmt == "F32":
                value_min, value_max = None, None  # IEEE 754 — range varies
            elif fmt == "N8":
                # Enum: use 0..255 as the encoding range (N8 is always 1 octet)
                value_min, value_max = 0, 255

        if resolution is None:
            if fmt == "F16":
                resolution = "0.01"
            elif fmt == "F32":
                resolution = "IEEE 754 single precision"

        # Encoding
        encoding = None
        if category == "boolean":
            encoding = "binary"
        elif category == "bitset":
            encoding = "bit flags"
        elif category == "enum":
            encoding = "enumeration"
        elif category == "float" and fmt == "F16":
            encoding = "KNX float (0.01*M)*2^E"
        elif category == "float" and fmt == "F32":
            encoding = "IEEE 754 single precision"
        elif category in ("signed",):
            encoding = "two's complement"
        elif category in ("unsigned",):
            encoding = "binary encoded"
        elif category == "string":
            if "ASCII" in name:
                encoding = "ASCII encoding, 14 characters max"
            elif "8859" in name:
                encoding = "ISO 8859-1 encoding, 14 characters max"
        elif category == "character":
            if "ASCII" in name:
                encoding = "ASCII encoding"
            elif "8859" in name:
                encoding = "ISO 8859-1 encoding"

        # Description — use parsed description from detail if available, otherwise derive from name
        description = dt.get("description") or derive_description(name)

        # Build the row
        row = {
            "dpt_id": dpt_id,
            "dpt_main_number": main,
            "dpt_sub_number": sub,
            "dpt_name": name,
            "description": description,
            "format_code": fmt,
            "size_bits": size_bits,
            "size_bytes": size_bytes,
            "data_type_category": category,
            "value_min": value_min,
            "value_max": value_max,
            "unit": unit,
            "resolution": resolution,
            "encoding": encoding,
            "coefficient": None,
            "use_scope": use_scope,
            "application_domain": app_domain,
            "value_map": value_map,
            "notes": None,
        }

        # Sparkplug
        sp = resolve_sparkplug_type(row)
        row["sparkplug_data_type"] = sp
        row["sparkplug_data_type_value"] = DATA_TYPES.get(sp, 0)

        results.append(row)

    return results


def enrich_from_existing(results: list[dict], existing_path: Path) -> list[dict]:
    """
    If the existing JSON has richer data for a DPT, merge it in.
    This fills gaps (descriptions, value_maps, encoding) from the curated JSON.
    """
    if not existing_path.exists():
        return results

    existing_data = json.loads(existing_path.read_text(encoding="utf-8"))
    existing_map = {e["dpt_id"]: e for e in existing_data}

    for row in results:
        ref = existing_map.get(row["dpt_id"])
        if not ref:
            continue

        # Prefer existing curated description over auto-generated
        if ref.get("description") and (
            not row.get("description") or row["description"] == derive_description(row["dpt_name"])
        ):
            row["description"] = ref["description"]

        # Prefer existing value_map if ours is empty
        if ref.get("value_map") and not row.get("value_map"):
            row["value_map"] = ref["value_map"]

        # Prefer existing encoding if ours is generic/auto-generated
        GENERIC_ENCODINGS = {"binary", "binary encoded", "bit flags", "enumeration", "two's complement"}
        if ref.get("encoding") and (
            not row.get("encoding") or row.get("encoding") in GENERIC_ENCODINGS
        ):
            row["encoding"] = ref["encoding"]

        # Prefer existing unit/resolution/notes/range if ours are missing
        for field in ("unit", "resolution", "notes", "value_min", "value_max"):
            if ref.get(field) is not None and row.get(field) is None:
                row[field] = ref[field]

    return results


def main():
    md_path = MD_PATH
    if len(sys.argv) > 1:
        md_path = Path(sys.argv[1])

    print(f"Reading markdown: {md_path}")
    text = md_path.read_text(encoding="utf-8")

    print("Parsing overview table...")
    overview = parse_overview_table(text)
    print(f"  Found {len(overview)} DPTs in overview")

    print("Parsing detail sections...")
    details = extract_detail_blocks(text)
    print(f"  Found details for {len(details)} DPTs")

    print("Building JSON...")
    results = build_json(overview, details)

    # Enrich from existing curated JSON if available
    existing = md_path.parent / "knx_datapoint_types.json"
    if existing.exists():
        print(f"Enriching from existing: {existing}")
        results = enrich_from_existing(results, existing)

    # Sort by main number, then sub number
    results.sort(key=lambda r: (r["dpt_main_number"], r["dpt_sub_number"]))

    out = OUTPUT_PATH
    if len(sys.argv) > 2:
        out = Path(sys.argv[2])

    out.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nWritten {len(results)} entries → {out}")

    # Summary
    from collections import Counter
    cats = Counter(r["data_type_category"] for r in results)
    print("\nBy category:")
    for cat, n in cats.most_common():
        print(f"  {cat:>12}: {n}")

    mains = sorted(set(r["dpt_main_number"] for r in results))
    print(f"\nMain numbers ({len(mains)}): {mains}")


if __name__ == "__main__":
    main()
