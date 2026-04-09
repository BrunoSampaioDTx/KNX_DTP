import json

data = json.load(open('dpt_new1.json'))
bad = ['SceneNumber','HWH','HVAC','TU','Lighting','Metering','VAC',
       'General','Busy','FOCI','general','c','litre','W/m','m3s-1','m3h-1','ls-1']

for e in data:
    if e.get('unit') in bad:
        print(f"{e['dpt_id']}: unit={e['unit']!r}  name={e['dpt_name']!r}  use_scope={e.get('use_scope')!r}")
