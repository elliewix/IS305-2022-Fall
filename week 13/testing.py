import csv
import string
from collections import Counter
import random

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


with open('corrected_pokemon_names.csv', 'r', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

names = [r[1] for r in data]

pairs = []

[pairs.extend(ngram_letters(name, 2)) for name in names]
[pairs.extend(ngram_letters(name, 3)) for name in names]

counted_pairs = dict(Counter(pairs))

# print(counted_pairs)

total = sum(counted_pairs.values())

probs = [[pair, count / total] for pair, count in counted_pairs.items()]

options = [p[0] for p in probs]
weights = [p[1] for p in probs]

beginning_letters = {p[0]: {} for p in pairs}

for pair, count in counted_pairs.items():
    first = pair[0]
    beginning_letters[first][pair] = count

# print(beginning_letters)
generated_names = []

starting_letters = [n[0].lower() for n in names if len(n) > 0]
# print(starting_letters)
for _ in range(10):
    name = ""
    start = random.choice(starting_letters)
    for _ in range(3):
        last = start[-1]
        first_letter_options = beginning_letters[last]
        total = sum(first_letter_options.values())
        probs = [[pair, count / total] for pair, count in first_letter_options.items()]

        options = [p[0] for p in probs]
        weights = [p[1] for p in probs]
        name += random.choices(options, weights = weights, k = 1)[0]
    generated_names.append(name)

for n in generated_names:
    print(n.title())
