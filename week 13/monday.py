import csv
import random
import string
from collections import Counter

with open('corrected_pokemon_names.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# get all the names

names = [r[1].lower() for r in data if not r[1].startswith('Mega')]
# print(names)
# make our own probabilities
# print(len(names))

all_letters = []
for n in names: # loop through all the names
    for letter in n: # loop through all the characters in each name
        all_letters.append(letter)

# a shorter functional style, just fyi
# shorter = []
# [shorter.extend(list(n)) for n in names]


# print(shorter)
# play in the random space

for outer in range(5): # do this five times
    name = ""
    for inner in range(7): # make a name 7 letters long
        # this code selects letters with equal across alphabet
        # letter = random.choice(string.ascii_lowercase)
        # this code samples from all the letters the appear
        letter = random.choice(all_letters)
        name += letter
    # print(name)

# let's inspect our population of letters

# all_letters has all of them

counted_letters = dict(Counter(all_letters))

# print(counted_letters)
total = sum(list(counted_letters.values()))
# print(total)
# for letter, count in counted_letters.items():
#     print(letter, count / total)

# NEVER EVER DO THIS
# letters = list(counted_letters.keys())
# probs = list(counted_letters.values())

letters = []
probs = []

results = [(letters.append(letter), probs.append(count / total)) for letter, count in counted_letters.items()]

# print(letters)
# print(probs)
# print(results) # full of nuns

for _ in range(5): # make 5 names
    result = random.choices(letters, weights=probs, k = 5)
    print("".join(result).title())

# we need to generate a random length

