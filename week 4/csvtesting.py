import csv
import pathlib

f = pathlib.Path('pokemon_names_and_descriptions.csv')

with open(f, 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

print(data)
print(headers)
