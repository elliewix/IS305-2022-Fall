import csv
import string

# step 1 is read in your

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    csvin = csv.reader(infile)
    headers, *data = csvin

def get_desc_words(desc):
    words = desc.lower().split()
    words = [w.split('[')[0] for w in words]
    clean_words = [w.strip(string.punctuation) for w in words]
    return clean_words

all_words = []
for r in data:
    desc = r[2]
    desc_words = get_desc_words(desc)
    # print(desc_words)
    # all_words.append(desc_words) # nope! we need to concat
    all_words += desc_words

print(len(all_words))

unique_words = list(set(all_words)) # making a set gets unique, then make it a list again

print(len(unique_words))

# print(unique_words)

unique_words.remove('pokémon')
unique_words.remove('pokemon')
unique_words.remove('')
for r in data:
    name = r[1]
    cname = get_desc_words(name)
    if len(cname) > 0:
        cname = cname[0]
        if cname in unique_words:
            unique_words.remove(cname)
    # if len(cname) > 0 and cname[0] in unique_words:
    #     # print("removed", cname)
    #     unique_words.remove(cname[0])

print(len(unique_words))

headers = unique_words.copy()

headers.insert(0, "pokedex")
headers.insert(1, "name")

print(headers)

# ready to fill out the data!

all_rows = []

for r in data:
    row = [r[0], r[1]] # get dex and name
    desc = r[2]
    desc_words = get_desc_words(desc)
    for w in unique_words:
        word_count = desc_words.count(w)
        row.append(word_count)
    all_rows.append(row)
    # print(row)

with open('monday_bog.csv', 'w', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(all_rows)
