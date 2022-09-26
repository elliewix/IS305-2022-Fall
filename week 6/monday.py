#dicts

empty_dict = {} # dict() also used

# pokenames = {'1': [0, []], '2': [0, []]}

d = {}

# prepopulating a dict
default_value = [0, []]
# print(id(default_value))
for i in range(100):
    key = str(i).zfill(3)
    # use copy to return a new object
    d[key] = default_value.copy()


# update an int value in a list...that's a
# value in a dict

# print(d['044'][0] + 1)
# print(d['044'])
d['044'][0] += 1
d['044'][0] += 1
d['044'][0] += 1
# print(d['044'])

# updating a list...in a list...in a dict

print(d['044'])
# checking all the ids to see if they're dif...
# print(id(default_value), id(d[]))
# for v in d.values():
#     print(id(v))

d['044'][1].append('cats')
print(d['044'])

# you can save it as a separate variable...
# but when you act on it, it'll update the main one
stuff = d['044'][1]
stuff.append('dogs')
print(stuff)

print(d['044'])


# testing membership

# print('044' in d)
# d['044'] = "hahah no"

# print(d)

if not '100' in d:
    d['100'] = "hahah no"

# handling overlaps...

import random
# randomly create an overlapping key...
# but only 50% chance


for _ in range(5):
    pick = str(random.randint(0,200)).zfill(3)
    print(pick)
    if not pick in d:
        d[pick] = "here's a new one!"

print(d)
