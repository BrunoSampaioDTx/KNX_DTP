import json
data = json.load(open('dpt_new1.json'))
for e in data:
    if e['dpt_id'] in ('9.022', '273.007'):
        print(f"{e['dpt_id']}: unit={e['unit']!r} res={e['resolution']!r}")
