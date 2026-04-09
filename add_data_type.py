import json
from pathlib import Path

INPUT = "knx_datapoint_types.json"
OUTPUT = "knx_datapoint_types.json"

# C# DataType enum mapping
DATA_TYPES = {
    "Unknown": 0,
    "Int8": 1,
    "Int16": 2,
    "Int32": 3,
    "Int64": 4,
    "UInt8": 5,
    "UInt16": 6,
    "UInt32": 7,
    "UInt64": 8,
    "Float": 9,
    "Double": 10,
    "Boolean": 11,
    "String": 12,
    "DateTime": 13,
    "Text": 14,
    "Bytes": 17,
}

# DPT main numbers that represent date/time
DATETIME_MAIN_NUMBERS = {10, 11, 19}


def resolve_data_type(row: dict) -> str:
    category = row.get("data_type_category")
    size_bits = row.get("size_bits")
    main = row.get("dpt_main_number")
    format_code = row.get("format_code", "")

    # Special case: date/time composites
    if main in DATETIME_MAIN_NUMBERS:
        return "DateTime"

    if category == "boolean":
        return "Boolean"

    if category == "signed":
        return {8: "Int8", 16: "Int16", 32: "Int32", 64: "Int64"}.get(size_bits, "Bytes")

    if category == "unsigned":
        return {8: "UInt8", 16: "UInt16", 32: "UInt32", 64: "UInt64"}.get(size_bits, "UInt8")

    if category == "float":
        if size_bits == 32 and "IEEE" in (row.get("encoding") or ""):
            return "Float"
        return "Float"  # KNX F16 maps to Float as closest fit

    if category == "enum":
        return "UInt8"

    if category in ("character", "string"):
        return "String"

    if category == "bitset":
        return {8: "UInt8", 16: "UInt16", 24: "Bytes", 32: "UInt32"}.get(size_bits, "Bytes")

    if category == "composite":
        return "Bytes"

    return "Unknown"


def main():
    data = json.loads(Path(INPUT).read_text(encoding="utf-8"))

    for row in data:
        dt_name = resolve_data_type(row)
        row["sparkplug_data_type"] = dt_name
        row["sparkplug_data_type_value"] = DATA_TYPES.get(dt_name, 0)

    Path(OUTPUT).write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Summary
    from collections import Counter
    counts = Counter(r["sparkplug_data_type"] for r in data)
    print(f"Updated {len(data)} entries:")
    for dt, n in counts.most_common():
        print(f"  {dt:>10} ({DATA_TYPES.get(dt, 0):>2}): {n}")


if __name__ == "__main__":
    main()
