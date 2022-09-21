import pathlib
import csv

f = pathlib.Path('pokemon_names_and_descriptions.csv')

with open(f, 'r', encoding='utf-8') as infile:
    csvin = csv.reader(infile) # makes the CSV reader object
    headers = next(csvin)
    data = [line for line in csvin]
    # data = []
    # for line in csvin:
    #     data.append(line)

print(len(data))
print(len(data[0]))
print(data[0])

for line in data:
    print(line[0])

print([line[0] for line in data])

