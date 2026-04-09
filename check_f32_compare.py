import json

data = json.load(open('dpt_new1.json'))
entries = {e['dpt_id']: e for e in data}

# PDF reference data (from user)
pdf_units = {
    '14.000': 'ms-2', '14.001': 'rad s-2', '14.002': 'J mol-1', '14.003': 's-1',
    '14.004': 'mol', '14.005': None, '14.006': 'rad', '14.007': '°',
    '14.008': 'J s', '14.009': 'rad s-1', '14.010': 'm2', '14.011': 'F',
    '14.012': 'C m-2', '14.013': 'C m-3', '14.014': 'm2 N-1', '14.015': 'S',
    '14.016': 'S m-1', '14.017': 'kg m-3', '14.018': 'C', '14.019': 'A',
    '14.020': 'A m-2', '14.021': 'C m', '14.022': 'C m-2', '14.023': 'V m-1',
    '14.024': 'c', '14.025': 'C m-2', '14.026': 'C m-2', '14.027': 'V',
    '14.028': 'V', '14.029': 'A m2', '14.030': 'V', '14.031': 'J',
    '14.032': 'N', '14.033': 'Hz', '14.034': 'rad s-1', '14.035': 'J K-1',
    '14.036': 'W', '14.037': 'J', '14.038': 'Ω', '14.039': 'm',
    '14.040': 'J or lm s', '14.041': 'cd m-2', '14.042': 'lm', '14.043': 'cd',
    '14.044': 'A m-1', '14.045': 'Wb', '14.046': 'T', '14.047': 'A m2',
    '14.048': 'T', '14.049': 'A m-1', '14.050': 'A', '14.051': 'kg',
    '14.052': 'kg s-1', '14.053': 'N s-1', '14.054': 'rad', '14.055': '°',
    '14.056': 'W', '14.057': None, '14.058': 'Pa', '14.059': 'Ω',
    '14.060': 'Ω', '14.061': 'Ωm', '14.062': 'H', '14.063': 'sr',
    '14.064': 'W m-2', '14.065': 'm s-1', '14.066': 'Pa', '14.067': 'Nm-1',
    '14.068': '°C', '14.069': 'K', '14.070': 'K', '14.071': 'JK-1',
    '14.072': 'W m-1 K-1', '14.073': 'V K-1', '14.074': 's', '14.075': 'Nm',
    '14.076': 'm3', '14.077': 'm3 s-1', '14.078': 'N', '14.079': 'J',
    '14.080': 'VA',
}

print("=== F32 UNIT COMPARISON (PDF vs JSON) ===\n")
mismatches = []
for dpt_id in sorted(pdf_units.keys(), key=lambda x: float(x)):
    pdf_unit = pdf_units[dpt_id]
    json_unit = entries.get(dpt_id, {}).get('unit')
    status = '✓' if pdf_unit == json_unit else '✗'
    if pdf_unit != json_unit:
        mismatches.append(dpt_id)
        print(f"  {status} {dpt_id}: PDF={pdf_unit!r:16s} JSON={json_unit!r}")

print(f"\n  Total mismatches: {len(mismatches)}")
print(f"  Matching: {len(pdf_units) - len(mismatches)}/{len(pdf_units)}")
