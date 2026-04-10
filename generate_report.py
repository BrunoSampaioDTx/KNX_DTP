#!/usr/bin/env python3
"""
KNX Datapoint Types — Markdown Report Generator
Reads standard_knx_datapoint_types.json and produces Result.md
with summary analytics and a full reference table.
"""

import json
from collections import Counter
from pathlib import Path

INPUT_FILE = Path("final_results/standard_knx_datapoint_types.json")
OUTPUT_FILE = Path("final_results/Result.md")


def load_data(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def distinct_sorted(values):
    """Return sorted list of distinct non-None values."""
    return sorted({v for v in values if v is not None})


def counter_table(counter: Counter, col1: str, col2: str) -> str:
    """Render a Counter as a small markdown table, sorted by count desc."""
    lines = [f"| {col1} | {col2} |", "| --- | ---: |"]
    for val, cnt in counter.most_common():
        label = val if val is not None else "*(none)*"
        lines.append(f"| {label} | {cnt} |")
    return "\n".join(lines)


def build_report(data: list[dict]) -> str:
    md = []

    # ── Header ──────────────────────────────────────────────
    md.append("# KNX Datapoint Types — Reference Report\n")
    md.append(f"> Auto-generated from `{INPUT_FILE.name}`  ")
    md.append(f"> **Total datapoint types:** {len(data)}\n")

    # ── 1. High-level overview ──────────────────────────────
    md.append("---\n## 1. Dataset Overview\n")

    main_numbers = distinct_sorted(d["dpt_main_number"] for d in data)
    md.append(f"- **Distinct main DPT numbers:** {len(main_numbers)}  ")
    md.append(f"  `{', '.join(str(m) for m in main_numbers)}`")
    md.append(f"- **Total sub-types:** {len(data)}")

    categories = Counter(d["data_type_category"] for d in data)
    md.append(f"- **Distinct data-type categories:** {len(categories)}")

    format_codes = Counter(d["format_code"] for d in data)
    md.append(f"- **Distinct format codes:** {len(format_codes)}")

    sparkplug_types = Counter(d["sparkplug_data_type"] for d in data)
    md.append(f"- **Distinct Sparkplug types:** {len(sparkplug_types)}")

    # ── 2. Application Domains ──────────────────────────────
    md.append("\n---\n## 2. Application Domains\n")
    domain_counter = Counter(d["application_domain"] for d in data)
    md.append(counter_table(domain_counter, "Application Domain", "Count"))

    # ── 3. Units ────────────────────────────────────────────
    md.append("\n---\n## 3. Distinct Units\n")
    unit_counter = Counter(d["unit"] for d in data)
    none_count = unit_counter.pop(None, 0)
    units_sorted = sorted(unit_counter.keys())
    md.append(f"**{len(units_sorted)}** distinct units found "
              f"({none_count} entries have no unit).\n")
    md.append("| # | Unit | Count |")
    md.append("| ---: | --- | ---: |")
    for i, u in enumerate(units_sorted, 1):
        md.append(f"| {i} | {u} | {unit_counter[u]} |")

    # ── 4. Data-Type Categories ─────────────────────────────
    md.append("\n---\n## 4. Data-Type Categories\n")
    md.append(counter_table(categories, "Category", "Count"))

    # ── 5. Format Codes ─────────────────────────────────────
    md.append("\n---\n## 5. Format Codes\n")
    md.append(counter_table(format_codes, "Format Code", "Count"))

    # ── 6. Use Scope ────────────────────────────────────────
    md.append("\n---\n## 6. Use Scope Distribution\n")
    scope_counter = Counter(d["use_scope"] for d in data)
    md.append(counter_table(scope_counter, "Use Scope", "Count"))

    # ── 7. Sparkplug Type Mapping ───────────────────────────
    md.append("\n---\n## 7. Sparkplug Data-Type Mapping\n")
    md.append(counter_table(sparkplug_types, "Sparkplug Type", "Count"))

    # ── 8. Distinct DPT IDs & Names ────────────────────────
    md.append("\n---\n## 8. Distinct DPT IDs & Names\n")
    md.append(f"**{len(data)}** datapoint (sub-)types defined.\n")
    md.append("| # | DPT ID | DPT Name | Description | Category | Domain |")
    md.append("| ---: | --- | --- | --- | --- | --- |")
    for i, d in enumerate(data, 1):
        md.append(
            f"| {i} "
            f"| {d['dpt_id']} "
            f"| {d['dpt_name']} "
            f"| {d['description']} "
            f"| {d['data_type_category']} "
            f"| {d['application_domain']} |"
        )

    # ── 9. Full Reference Table ─────────────────────────────
    md.append("\n---\n## 9. Full Reference Table\n")

    columns = [
        ("DPT ID", "dpt_id"),
        ("Main#", "dpt_main_number"),
        ("Sub#", "dpt_sub_number"),
        ("Name", "dpt_name"),
        ("Description", "description"),
        ("Format", "format_code"),
        ("Bits", "size_bits"),
        ("Bytes", "size_bytes"),
        ("Category", "data_type_category"),
        ("Min", "value_min"),
        ("Max", "value_max"),
        ("Unit", "unit"),
        ("Resolution", "resolution"),
        ("Encoding", "encoding"),
        ("Coefficient", "coefficient"),
        ("Scope", "use_scope"),
        ("Domain", "application_domain"),
        ("Value Map", "value_map"),
        ("Notes", "notes"),
        ("Sparkplug Type", "sparkplug_data_type"),
        ("Sparkplug Val", "sparkplug_data_type_value"),
    ]

    header = "| " + " | ".join(c[0] for c in columns) + " |"
    sep = "| " + " | ".join("---" for _ in columns) + " |"
    md.append(header)
    md.append(sep)

    for d in data:
        cells = []
        for _, key in columns:
            val = d.get(key)
            if val is None:
                cells.append("")
            elif key == "value_map" and isinstance(val, dict):
                # Compact representation: 0→Off, 1→On
                pairs = ", ".join(f"{k}→{v}" for k, v in val.items())
                cells.append(pairs)
            elif key == "encoding":
                # Escape pipes inside encoding strings
                cells.append(str(val).replace("|", "∣"))
            else:
                cells.append(str(val))
        md.append("| " + " | ".join(cells) + " |")

    md.append("")
    return "\n".join(md)


def main():
    data = load_data(INPUT_FILE)
    report = build_report(data)
    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(f"✔ Report written to {OUTPUT_FILE}  ({len(data)} entries)")


if __name__ == "__main__":
    main()
