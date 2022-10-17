import random

random.seed(20221012)
nums = random.sample(range(20,40), 12)
nums.sort()
print(nums)

### look behind loop
# **skip the first item!**

for i, n in enumerate(nums):
    if i == 0: # skip first i pos
        continue
    else:
        before = nums[i - 1]
        now = n
        print(before, now)

## look ahead loop
# ** skip the last one!

for i, n in enumerate(nums):
    if i == len(nums) - 1: #ugh WHY 1970s bros
        continue
    else:
        now = n
        after = nums[i + 1] # next is a function, don't use it
        print(now, after)

## look behind and ahead

triples = []
for i, n in enumerate(nums):
    if i == 0:
        continue # skip first
    elif i == len(nums) - 1:
        continue # skip last
    else:
        before = nums[i - 1]
        now = n
        after = nums[i + 1]
        triples.append([before, now, after])

print(triples)

## but you may want to do something else when it's the first or last

