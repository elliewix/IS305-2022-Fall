# collect groups of even numbers

# nums = [1, 2, 8, 7, 8, 10, 11, 12, 15]
nums = [2, 2, 1, 2, 8, 7, 8, 10, 10, 11, 12, 15, 18, 16, 20, 2]



## desire: [ [2, 8], [8, 10], [12] ]

all_groups = [] # outer list
current_group = [] # inner list, will be reset
for i, n in enumerate(nums):
    # looking behind, so skip the first one
    if i == 0:
        continue
    # setup
    before = nums[i - 1]
    now = n
    before_even = before % 2 == 0
    now_even = now % 2 == 0
    end_i = len(nums) - 1
    # print(before, now, before_even, now_even)
    # print(current_group, all_groups)


    # traverse the internal section
    # collect only before
    # continue on: collect number, move on
    # wrapup: collect number, collect current group, reset current group

    if before_even and now_even: # TT
        current_group.append(before)
    elif before_even and not now_even: # T, F same as now_even == False
        current_group.append(before)
        all_groups.append(current_group)
        current_group = []
    # elif not before_even and now_even and i == end_i: maybe cover elsewhere
    #     all_groups.append( [now] )
    # elif before_even and now_even and i == end_i:  # hmmm too much...
    #     current_group.append()

    # endgame section
    # F F -> do nothing
    # T F -> do nothing ,wrapup already done
    # F T -> do nothing, handled
    # T T...... how to do it?

    if now_even and i == end_i:
        current_group.append(now)
        all_groups.append(current_group)

print(all_groups)
