# count = 0
# for i in range(10):
#     count += 1
#
# print(count)

# count = 15
# i = 0
#
# while i < 10:
#     count *= 2 # count = count * 2
#     i += 1
#     print(count)

import random

# loop to add nums until we get to 100



random.seed(1)
results = {}

# not a great idea ,but possible with more thought....

# def run_it():
#     while total <= target:
#         pick = random.randint(0, 10) # inclusively select 0-10, each equal chance
#         total += pick
#         iterations += 1
#         all_picks.append(pick)
for run in range(100000): # run sim 100 times
    total = 0 # counting this up to 100
    iterations = 0 # counting how many times we've looped
    target = 100
    all_picks = []
    run_it()
    results[str(run).zfill(3)] = {'total': total, 'iterations': iterations, 'all_picks': all_picks}
    # print("total", total, "iterations", iterations)

# for k, v in results.items():
#     print(k,v)

for run_number, run_info in results.items():
    run_total = run_info['total']
    run_iters = run_info['iterations']
    # print(run_number, run_total, run_iters)

all_totals = [info['total'] for info in results.values()]
iters = [info['iterations'] for info in results.values()]

print(max(all_totals), min(all_totals))
print(max(iters), min(iters))

# print(all_totals.count(110), all_totals.count(100))
#
#
# for run in results.values():
#     if run['total'] == 110:
#         print(run)
