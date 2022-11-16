import csv
import random
import string
from collections import Counter

with open('corrected_pokemon_names.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# get all the names

names = [r[1].lower() for r in data if not r[1].startswith('Mega')]

def ngram_letters(name, num):
    name = name.lower()
    nameparts = [n.strip(string.punctuation) for n in name.split()]
    grams = []
    if len(nameparts) > 1:
        for part in nameparts:
            # grams += ngram_letters(part,num)
            grams.extend(ngram_letters(part,num))
    else:
        for i in range(len(name)):
            if i + num > len(name):
                break
            grams.append(name[i:i + num])
    return grams

bigrams = []
for n in names:
    results = ngram_letters(n, 2)
    bigrams.extend(results)

# [ngram_letters(n, 2)) for n in names] would give me a 2d list of the stuff
# below is equiv to the for loop above on line 30
# [bigrams.extend(ngram_letters(n, 2)) for n in names]

for _ in range(10): # make 10 random names
    name = ""
    for _ in range(3): # select 3 pair of letters
        name += random.choice(bigrams)
    print(name.title())



# create list of lengths

name_lengths = [len(n) for n in names]
# print(name_lengths)

for _ in range(10): # make 10 random names
    name = ""
    chosen_length = random.choice(name_lengths)
    while len(name) < chosen_length:
        name += random.choice(bigrams)
    # for _ in range(3): # select 3 pair of letters
    #     name += random.choice(bigrams)
    print(chosen_length, len(name), name[:chosen_length].title())
