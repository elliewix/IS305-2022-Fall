## write a program that loops through a list of numbers
# collecting sublists of all individual even numbers or groups or
# consecutive (not sequential) even numbers

# eg [1, 2, 3, 4, 6, 7, 8]

# do we want a look ahead or look behind?
### look behind, because just knowing now doesn't tell us things
### we only want to add once we've seen now

# * look behind check
# * checking if even number
# * checking if consecutive even numbers
# * collection and resetting

import random
random.seed(20221017)
nums = random.sample(range(100,120), 20)
# nums = [2, 1, 2, 3, 4, 6, 7, 8]
print(nums)
end_i = len(nums) - 1
all_groups = []
current_group = []

for i, n in enumerate(nums):
    # protection part
    if i == 0:
        continue
    #  this part will execute only for after first...

    # setup part
    before = nums[i - 1]
    before_even = before % 2 == 0
    now = n
    now_even = now % 2 == 0

    # traversing part
    if before_even and now_even:
        current_group.append(before)
    elif before_even and not now_even:
        current_group.append(before)
        all_groups.append(current_group)
        current_group = []

    # wrapup part
    if now_even and i == end_i:
        current_group.append(now)
        all_groups.append(current_group)



# this one is stupid
# for i, n in enumerate(nums):

    # # create and seed before situation
    # if i == 0: # beginning
    #     before_even = n  # seed with false
    #     continue # skip ahead, nothing to compare
    # else:
    #     before = nums[i - 1]
    #     before_even = before % 2 == 0
    #
    # now_even = n % 2 == 0
    # if before_even and now_even:
    #     current_group.append(before)
    # elif before_even and not now_even:
    #     current_group.append(before)
    #     all_groups.append(current_group)
    #     current_group = []
    # elif not before_even and now_even:
    #     # we only care if this is the end....
    #     if i == len(nums) - 1:
    #         all_groups.append([n])
    # elif not before_even and not now_even:
    #     continue



# for i, n in enumerate(nums):
#     if i == 0:
#         continue
#     now = n
#     before = nums[i - 1]
#     now_even = now % 2 == 0
#     before_even = before % 2 == 0
#     if before_even and now_even: # TT
#         current_group.append(before)
#         print("hi", now)
#         if i == len(nums) - 1:
#             current_group.append(now)
#             all_groups.append(current_group)
#     elif before_even and not now_even:
#         current_group.append(before)
#         all_groups.append(current_group)
#         current_group = []

print(all_groups)

