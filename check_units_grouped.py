import json
from collections import defaultdict

data = json.load(open('dpt_new1.json'))

by_unit = defaultdict(list)
no_unit = []
for e in data:
    u = e.get('unit')
    if u:
        by_unit[u].append(e['dpt_id'])
    else:
        no_unit.append(e['dpt_id'])

print("=== DPTs GROUPED BY UNIT ===\n")
for unit in sorted(by_unit.keys()):
    ids = by_unit[unit]
    print(f"  {unit!r:20s} ({len(ids):3d}): {', '.join(ids)}")

print(f"\n=== NO UNIT ({len(no_unit)}) ===")
print(f"  {', '.join(no_unit)}")
