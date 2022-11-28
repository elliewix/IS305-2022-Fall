import csv

with open('pokemon-names-and-types.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

cleaned = [r for r in data if r[0] != '']

with open('cleaned_pokemon_info.csv', 'w', encoding='utf-8') as outfile:
    out = csv.writer(outfile)
    out.writerow(headers)
    out.writerows(cleaned)
