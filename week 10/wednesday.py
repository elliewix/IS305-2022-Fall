import csv

# infile = open....
# .read() or .readlines()....
# .close()

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    # getting .close() for free
    # do stuff with infile....
    csvin = csv.reader(infile)
    # for _ in range(10): # force it to go a specific number of times
    #     next(csvin)
    header = next(csvin)
    # all_rows =  [] # we usually call this data
    # for row in csvin:
    #     all_rows.append(row)
    # equivalent in list comp
    all_rows = [row for row in csvin]

# print(all_rows)

# smaller list comp example

text = "cats"

results =  [character for character in text] # loop over a strings
results = [ord(character) for character in text] # get something back about the thing
results = ['x' for character in text] # or nothing at all about it
results = [[ord(c.lower()), ord(c.upper())] for c in text] # or make something more complex

# print(results)

# indexing and enumerate

## we can do it manually.....
# i = 0
# for c in text:
#     print("manually:", i, c)
#     i += 1

## or we can use enumerate....
## we can just see the stuff this way....
# for pair in enumerate(text):
#     print("enumerate:", pair)
#
# print(list(enumerate(text)))

for pair in enumerate(text):
    index = pair[0]
    character = pair[1]
    print(index, character)

# a shorthand....

for index, character in enumerate(text):
    print(index, character)

## tuples...

tuppy = ('a', 'b', 'c')

# print(tuppy)
# print(tuppy[1]) #index like normal
# print(tuppy[1:]) #slice like normal

# tuppy.append('d')  #nope
# tuppy[1] = 'B' # also nope

a = (1, 4)  # friend a lives
b = (2, -3)  # friend b lives

data = {a: 'A', b: 'B'}

# print(data)
# print(data[(1, 4)])
# for key, value in data.items(): # yes but gross
#     x, y = key
#     print(x, y, value)

# for row in all_rows:
#     print(row)


# 2d lists

nums = [ [30, 31, 32],
         [40, 41, 42],
         [50, 51, 52]]

for r in nums:
    print(r[1]) # get the middle column of data

print(nums[1]) # get the 1th list
print(nums[1][1]) # get 41 so (1th, 1th)

a = [30, 31, 32]

print(a, nums[0])
print(a == nums[0]) # yup! content wise they match
print(id(a), id(nums[0]))
# thus
print(a is nums[0])

b = nums[1] # will give that list the variable name b, but not make a new one
print(id(b), id(nums[1]))
print(b == nums[1])
print(b is nums[1])
b.append(100)
print(nums)

c = nums[2].copy() # how to make an unlinked copy
# you may also see it as nums[2][:], same thing
print(id(c), id(nums[2]))
c.append(200)
print(nums)
