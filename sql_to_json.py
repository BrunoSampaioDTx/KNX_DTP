import json
import sys
from decimal import Decimal
from pathlib import Path

import psycopg2
import psycopg2.extras

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "knx",
    "user": "knx",
    "password": "knx",
}


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o) if o % 1 else int(o)
        return super().default(o)


def export_to_json(output_path: str = "knx_datapoint_types.json") -> str:
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM public.knx_datapoint_types ORDER BY dpt_main_number, dpt_sub_number")
            rows = cur.fetchall()
    finally:
        conn.close()

    data = [dict(row) for row in rows]

    Path(output_path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False, cls=DecimalEncoder),
        encoding="utf-8",
    )
    print(f"Exported {len(data)} rows -> {output_path}")
    return output_path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "knx_datapoint_types.json"
    export_to_json(out)
