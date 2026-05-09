import json

with open(r'z:\docpilot_data\RAG.ipynb', 'r', encoding='utf-8-sig') as f:
    nb = json.load(f)

cell = nb['cells'][2]
cell['source'] = [
    line.replace('api_key=""', 'api_key=""')#Paste your key here, between the quotes ok na
    for line in cell['source']
]

src = ''.join(cell['source'])
print('Key present:', 'gsk_z2oYHqCq' in src)

with open(r'z:\docpilot_data\RAG.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Saved OK')
