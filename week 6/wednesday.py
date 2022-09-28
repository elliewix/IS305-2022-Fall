import random


options = ['cats', 'dogs', 'snakes', 'clay', 'legos', 'adafruit']

# overlap_values = []
#
# for sim in range(100000):
#     d = {}
#     for _ in range(100):
#         key = str(random.randint(1,100)).zfill(3)
#         value = random.choice(options) + " " + random.choice(options)
#         # print(key, value)
#         d[key] = value
#     overlap_values.append(100 - len(d))
#
# print(sum(overlap_values) / len(overlap_values))

d  = {}
options = ['cats', 'dogs', 'snakes', 'clay', 'legos', 'adafruit']

desired = 50
for _ in range(1000):
    key = str(random.randint(1,100)).zfill(3)
    value = random.choice(options) + " " + random.choice(options)
    # print(key, value)
    if not key in d:
        d[key] = value
    if len(d) >= desired:
        break

import pathlib
for k, v in d.items():
    p = pathlib.Path(k + ".txt")
    print(p)
