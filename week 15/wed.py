import json

with open('example.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

print(data['children'])

data['children'].append("Fluffy")

print(data['children'])

with open('example-updated.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent = 2)
