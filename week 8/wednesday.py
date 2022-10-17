import random

random.seed(20221012)
nums = random.sample(range(100,120), 12)
nums.sort()

# print(list(enumerate(nums)))
# print(nums[1:])

# for i, n in enumerate(nums[1:]): # just as janky
#     i = i + 1
#     print(i,n)
#
# for i, n in enumerate(nums):
#     if i == 0:
#         continue
#         # print("the first!", i, n)
#     else:
#         before = nums[i - 1]
#         now = n
#         diff = now - before
#         if diff == 1:
#             print(before, now)
#         # print(before, now, diff)

## look ahead

# for i, n in enumerate(nums):
#     if i == len(nums) - 1: #ugggh
#         continue
#     else:
#         now = n
#         after = nums[i + 1]
#         print(now, after)

triples = []
for i, n in enumerate(nums):
    if i == 0:
        continue
    elif i == len(nums) - 1:
        continue
    else:
        before = nums[i - 1]
        now = nums[i]
        after = nums[i + 1]
        one_triple = [before, now, after]
        triples.append(one_triple)
        # print(before, now, after)

print(triples)
