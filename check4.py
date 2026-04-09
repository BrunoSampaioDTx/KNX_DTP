import json
data = json.load(open('dpt_new1.json'))
for e in data:
    if e.get('unit') in ('b0', 'r1b1U6'):
        print(f"{e['dpt_id']}: unit={e['unit']!r} name={e['dpt_name']!r} fmt={e.get('format_code')!r}")
