# sentinel loops

## randomly generate a number until you
## generate the target number

import random
target = 68 # set your target
target_found = False # set your sentinel to False
pick_count = 0
while not target_found:
    pick = random.randint(0,100)
    pick_count += 1
    if pick == target:
        target_found = True

# print(pick_count)


def match_target(target, min_pick, max_pick):
    target_found = False # set your sentinel to False
    pick_count = 0
    while not target_found:
        pick = random.randint(min_pick,max_pick)
        pick_count += 1
        if pick == target:
            target_found = True
    return pick_count


all_pick_counts = []

for i in range(1000):
    all_pick_counts.append(match_target(5, 1, 10))

from collections import Counter
counted = dict(Counter(all_pick_counts))
# for count, runs in counted.items():
#     print(count, runs/1000)

def order(pair):
    run_count = pair[0]
    num_runs = pair[1]
    return run_count

ordered = sorted(counted.items(), key=order)

# for num, count in ordered:
#     print(num, round(count/10), "%", round(count / 10) * "*")
#

# sentinel loops and data

## generate some random shitty data

choices = {1: .2, 2: .1, 0: .7}
picks = []
probs = []

# need to get these into separate lists with paired indicies
for num, prob in choices.items():
    picks.append(num)
    probs.append(prob)

for i in range(len(choices)):
    print(picks[i], probs[i])
k = []
v = []
[(k.append(_), v.append(_)) for _,_ in choices.items()]

print(k,v)

print(list(zip(*choices.items())))
