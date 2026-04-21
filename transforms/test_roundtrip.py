#!/usr/bin/env python3
import ast
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "transforms"))

from knx_dpt_transforms import (
    dpt9_decode,
    dpt9_encode,
    f32_decode,
    f32_encode,
    v16_decode,
    v16_encode,
    v32_decode,
    v32_encode,
    v8_decode,
    v8_encode,
)


FINAL_RESULTS = ROOT / "final_results"
NUMERIC_PREFIX_RE = re.compile(r"^\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)")
ALLOWED_FORMULA_NAMES = {
    "ui_value",
    "raw_value",
    "round",
    "ord",
    "chr",
    "dpt9_decode",
    "dpt9_encode",
    "f32_decode",
    "f32_encode",
    "v8_decode",
    "v8_encode",
    "v16_decode",
    "v16_encode",
    "v32_decode",
    "v32_encode",
}


def _parse_factor(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = NUMERIC_PREFIX_RE.match(value)
        if match:
            return float(match.group(1))
    return None


def _sample_values(entry: dict):
    category = (entry.get("data_type_category") or "").lower()
    if category == "character":
        return ["A", "B", "a", "0", "Z"]
    if category == "boolean":
        return [0, 1, 0, 1, 1]

    v_min = entry.get("value_min", 0)
    v_max = entry.get("value_max", 4)
    if not isinstance(v_min, (int, float)) or not isinstance(v_max, (int, float)):
        return [0, 1, 2, 3, 4]

    if v_min == v_max:
        return [v_min] * 5

    category = (entry.get("data_type_category") or "").lower()
    size_bits = int(entry.get("size_bits", 0) or 0)
    step = _parse_factor(entry.get("coefficient")) or _parse_factor(entry.get("resolution")) or _parse_factor(entry.get("step")) or 1.0

    if category == "signed" and size_bits > 0:
        representable_min = -(2 ** (size_bits - 1)) * step
        representable_max = (2 ** (size_bits - 1) - 1) * step
        v_min = max(v_min, representable_min)
        v_max = min(v_max, representable_max)
    elif category == "unsigned" and size_bits > 0:
        representable_min = 0
        representable_max = (2**size_bits - 1) * step
        v_min = max(v_min, representable_min)
        v_max = min(v_max, representable_max)

    points = [v_min + (v_max - v_min) * i / 4 for i in range(5)]
    if step > 0:
        points = [round(p / step) * step for p in points]
    return [min(v_max, max(v_min, p)) for p in points]


def _tolerance(entry: dict):
    category = (entry.get("data_type_category") or "").lower()
    if category in {"boolean", "enum", "bitset"}:
        return 0.0
    if category in {"signed", "unsigned"}:
        step = _parse_factor(entry.get("coefficient")) or _parse_factor(entry.get("resolution")) or _parse_factor(entry.get("step")) or 1.0
        return 0.0 if step == 1 else max(step / 2.0, 1e-9)
    step = _parse_factor(entry.get("coefficient")) or _parse_factor(entry.get("resolution")) or _parse_factor(entry.get("step")) or 1.0
    return max(step / 2.0, 1e-6)


def _eval_formula(formula: str, **kwargs):
    _validate_formula(formula)
    return eval(
        formula,
        {"__builtins__": {}},
        {
            **kwargs,
            "round": round,
            "ord": ord,
            "chr": chr,
            "dpt9_decode": dpt9_decode,
            "dpt9_encode": dpt9_encode,
            "f32_decode": f32_decode,
            "f32_encode": f32_encode,
            "v8_decode": v8_decode,
            "v8_encode": v8_encode,
            "v16_decode": v16_decode,
            "v16_encode": v16_encode,
            "v32_decode": v32_decode,
            "v32_encode": v32_encode,
        },
    )


def _validate_formula(formula: str):
    tree = ast.parse(formula, mode="eval")
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id not in ALLOWED_FORMULA_NAMES:
            raise ValueError(f"Unexpected name in formula: {node.id}")


def main():
    files = sorted(FINAL_RESULTS.glob("*.json"))
    checked = 0
    failures = []

    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            continue
        if not data or "formula_to_bus" not in data[0] or "formula_from_bus" not in data[0]:
            continue

        for entry in data:
            formula_to_bus = entry.get("formula_to_bus")
            formula_from_bus = entry.get("formula_from_bus")
            if formula_to_bus is None or formula_from_bus is None:
                continue

            tol = _tolerance(entry)
            for sample in _sample_values(entry):
                sample_tol = tol
                if "dpt9_" in formula_to_bus or "dpt9_" in formula_from_bus:
                    sample_tol = max(sample_tol, abs(float(sample)) * 1e-3, 0.02)
                raw = _eval_formula(formula_to_bus, ui_value=sample)
                decoded = _eval_formula(formula_from_bus, raw_value=raw)
                if isinstance(sample, str):
                    ok = decoded == sample
                elif sample_tol == 0:
                    ok = decoded == sample
                else:
                    ok = math.isclose(decoded, sample, rel_tol=0, abs_tol=sample_tol)

                if not ok:
                    failures.append(
                        f"{path.name} {entry.get('dpt_id')}: sample={sample!r} raw={raw!r} decoded={decoded!r} tol={sample_tol}"
                    )
                    break
            checked += 1

    if failures:
        raise SystemExit("Roundtrip failures:\n" + "\n".join(failures))

    print(f"Roundtrip validation passed for {checked} formula pairs.")


if __name__ == "__main__":
    main()
