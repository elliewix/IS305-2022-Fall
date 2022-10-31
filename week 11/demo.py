# bag of words!!!!!

import csv
import string

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    csvin = csv.reader(infile)
    headers, *data = csvin

# for r in data:
#     desc_words = r[2].lower().split()
#     cleaned = [w.strip(string.punctuation) for w in desc_words]
#     print(cleaned)

def get_desc_words(desc):
    desc = r[2].lower().split()
    cleaned = [w.strip(string.punctuation) for w in desc]
    return cleaned

# so the headers are all the unique words across the corpus
## we want a flat structure here

allwords = []
for r in data:
    allwords += get_desc_words(r[2]) # using list concat

# now needs to be just the uniques

unique_words = list(set(allwords)) # I could do a fancy list or just cast it to a set

print(len(allwords), len(unique_words))

# not perfect but good enough

# maybe we want to remove the pokemon names??

for r in data:
    name = r[1].lower().strip(string.punctuation)
    pass # print(name, unique_words.count(name))

# so we want to get rid of the empty string

unique_words.remove('')

for r in data:
    name = r[1].lower().strip(string.punctuation)
    count = unique_words.count(name)
    if count > 0: # only see the positive counts
        pass #print(name, unique_words.count(name))

# there's a lot, and it's for sure a tell that it matches if the name is there


# we've seen how we can remove things from a list with remove....
# but remove will throw an error if it isn't in there....

for r in data:
    name = r[1].lower().strip(string.punctuation)
    count = unique_words.count(name)
    if count > 0: # only see the positive counts
        unique_words.remove(name)
        # print(name, unique_words.count(name))

# and done!

# now our headers are done
print(len(unique_words))

# here is where you may want to do more cleaning
# for w in unique_words:
#     if len(w) < 2:
#         print(w)


# now that we have the headers, we can calculate the rows
# for each pokemon

# we want to loop over unique words because we want answers for each
# word in the corpus

for r in data:
    d = get_desc_words(r[2])
    results = [d.count(w) for w in unique_words]
    # print(results)

# cool but we want the pokemon name in there too

all_counts = []
for r in data:
    d = get_desc_words(r[2])
    results = [d.count(w) for w in unique_words]
    # print(sum(results))
    # some are empty and that's okay!
    results.insert(0, r[0])
    results.insert(1, r[1])
    all_counts.append(results)

# now make new headers...

headers = unique_words.copy()
headers.insert(0, "pokedex")
headers.insert(1, "name")

with open('pokemon_bog.csv', 'w', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(all_counts)

biggests = []
for p in all_counts:
    max_count = max(p[3:])
    if max_count == 0:
        continue
    for i, count in enumerate(p):
        if count == max_count:
            # print(p[1], headers[i], count)
            biggests.append(headers[i])

# print(biggests)
# now we may want to go back and do some cleaning

from collections import Counter

counted = Counter(biggests)

trimmed_words = unique_words.copy()

# this is a pretty brutal tactic here, you should use
# more nuance and best practices for the data you are using
top = counted.most_common(20)

for word, count in top:
    trimmed_words.remove(word)

# now let's run the process again
trimmed_results = []

all_counts = []
for r in data:
    d = get_desc_words(r[2])
    results = [d.count(w) for w in trimmed_words]
    # print(sum(results))
    # some are empty and that's okay!
    results.insert(0, r[0])
    results.insert(1, r[1])
    trimmed_results.append(results)


headers = trimmed_words.copy()
headers.insert(0, "pokedex")
headers.insert(1, "name")

with open('pokemon_bog_trimmed.csv', 'w', encoding='utf-8') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(trimmed_results)

biggests = []
for p in trimmed_results:
    max_count = max(p[3:])
    if max_count == 0:
        continue
    for i, count in enumerate(p):
        if count == max_count:
            print(p[1], headers[i], count)
            biggests.append(headers[i])

# print(biggests)


# experiments
# loosely based on https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
decs = {r[0] + r[1]: " ".join(get_desc_words(r[2])) for r in data}

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(decs)
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)
df.to_csv('tfidf.csv')
