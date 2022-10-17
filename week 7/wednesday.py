# choice = input("say yes or no")
#
# while choice != "yes":
#     choice = input("say yes or no")
# else:
#     print("thanks")

import random
target = "a"
target_found = False
iteration_count = 0

while not target_found:
    pick = random.choice(['a', 'b', 'c', 'd'])
    if pick == target:
        target_found = True
    iteration_count += 1
    # print(pick, iteration_count)


######

# target = 5
# target_found = False
#
# while not target_found:
#     pick = random.randint(1,10)
#     target_found = pick == target
#     print(pick)



letters = {'a': .1, 'b': .1, 'c':.2, 'h':.05, 'e':.3, 'z': .25}

picks = []
probs = []

for k, v in letters.items():
    picks.append(k)
    probs.append(v)
# not great to use
# picks = letters.keys()
# probs = letters.values()

# print(picks)
# print(probs)


#print(sum(letters.values())) # check that it's 1

my_letters = random.choices(picks, weights = probs, k = 100)
# print(my_letters.count('h'))

picks, probs = zip(*letters.items())
print(picks)
print(probs)


