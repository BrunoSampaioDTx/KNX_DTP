import json
data = json.load(open('../output/dpt_new1.json'))
entries = {e['dpt_id']: e for e in data}
for dpt_id in ['14.038', '14.059', '14.060', '14.061']:
    u = entries[dpt_id]['unit']
    print(f"{dpt_id}: unit={u!r} chars={[hex(ord(c)) for c in u]}")
