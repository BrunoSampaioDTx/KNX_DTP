#!/usr/bin/env python3

import json
import re
from pathlib import Path

SOURCE_JSON = Path(__file__).resolve().parent / "final_results" / "standard_knx_datapoint_types.json"
OUTPUT_JSON = Path(__file__).resolve().parent / "final_results" / "standard_knx_datapoint_types_with_step.json"

# Matches a leading numeric token at the start of the resolution string:
# integers (10), decimals (0.01, .5), and scientific notation (1e-3).
LEADING_NUMBER_PATTERN = re.compile(r"^\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)")


def extract_resolution_step(resolution):
    if not isinstance(resolution, str):
        return None

    match = LEADING_NUMBER_PATTERN.search(resolution)
    if not match:
        return None

    value = float(match.group(1))
    return int(value) if value.is_integer() else value


def is_integer_number(value):
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return value.is_integer()
    return False


def fallback_step(entry):
    category = entry.get("data_type_category")
    value_min = entry.get("value_min")
    value_max = entry.get("value_max")

    if category in {"boolean", "composite", "enum"}:
        return 1

    if category in {"unsigned", "signed"} and is_integer_number(value_min) and is_integer_number(value_max):
        return 1

    return None


def insert_step_after_resolution(entry, step):
    updated = {}
    inserted = False

    for key, value in entry.items():
        updated[key] = value
        if key == "resolution":
            updated["step"] = step
            inserted = True

    if not inserted:
        updated["step"] = step

    return updated


def main():
    try:
        data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Source file not found: {SOURCE_JSON}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in source file {SOURCE_JSON}: {exc}") from exc

    output = []

    for entry in data:
        step = extract_resolution_step(entry.get("resolution"))
        if step is None:
            step = fallback_step(entry)
        output.append(insert_step_after_resolution(entry, step))

    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {len(output)} entries to {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
