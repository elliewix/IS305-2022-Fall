

# infile = open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8')
# text = infile.read()
# infile.close()

# with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
#     text = infile.read()
#
# print(text)


filename = 'data/raw/pokemon_names_and_descriptions.csv'
# print(filename.split('/')[2].split('.')[0]) #old, booooo

import pathlib
p = pathlib.Path(filename)
# print(p, p.name, p.stem)
# print(p)
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.parts)
# print(filename.split("/"))
# print(p.exists(), p.name)

# pretend this is the beginning of a new file...

import pathlib

filename = 'pokemon_names_and_descriptions.csv'

p = pathlib.Path(filename)

print(p)
print(p.exists())
print(p.absolute())
print(p.is_file())

# with open(p, 'r', encoding='utf-8') as infile:
#     text = infile.read()
#
# print(text)

text = p.open().read()
print(text)

foldername = "stuff"
f = pathlib.Path(foldername)
# pathlib.Path(foldername).mkdir()
if not f.exists():
    f.mkdir()
print(f / p)

f.rmdir()
