import json

data = json.load(open('../output/dpt_new1.json'))
entries = {e['dpt_id']: e for e in data}

# Collect all unique units
units = sorted(set(e.get('unit') for e in data if e.get('unit')))
print("=== ALL UNIQUE UNITS ===")
for i, u in enumerate(units, 1):
    print(f"  {i}: {u!r}")

print(f"\nTotal unique units: {len(units)}")

# Check specific fixes
print("\n=== SPECIFIC CHECKS ===")
checks = {
    '9.022': 'W/m2 unit fix',
    '273.007': 'W/m2 unit fix',
    '14.024': 'electric flux unit',
    '12.1200': 'litre unit',
    '14.077': 'volume flux unit',
    '14.1200': 'volume flux meter unit',
    '14.1201': 'volume flux ls unit',
    '17.001': 'scene number (no unit)',
    '20.102': 'HVAC mode (no unit)',
    '20.604': 'lighting (no unit)',
    '20.1203': 'metering (no unit)',
    '24.001': 'var string (no unit)',
    '25.1000': 'double nibble (no unit)',
    '200.100': 'heat/cool (no unit)',
}
for dpt_id, desc in checks.items():
    if dpt_id in entries:
        e = entries[dpt_id]
        print(f"  {dpt_id} ({desc}): unit={e.get('unit')!r} res={e.get('resolution')!r}")
