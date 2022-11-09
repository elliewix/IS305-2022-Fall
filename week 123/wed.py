name = "pikachu"
num = 3 # because we want a bigram
grams = []

def get_positions(i, n):
    positions = []
    for look_ahead_index in range(n):
        # print("i", i, "j", look_ahead_index, "makes", i + look_ahead_index)
        positions.append(i + look_ahead_index)
    return positions
# for i, letter in enumerate(name):
#     # don't do the last one
#     skip = num - 1
#     if i == len(name) - skip:
#         break
#     # pair = letter + name[i + 1]
#     # group = ""
#     # for pos in get_positions(i, num):
#     #     group += name[pos]
#     # group = name[positions[0]: positions[-1] + 1]
#     # print(get_positions(i, num), group)
#     # for j in range(num):
#     #     group += name[i + j]
#     # all this sucks but maybe here's a shorter one
#     all_positions = get_positions(i, num)
#     start_pos = all_positions[0]
#     stop_pos = all_positions[-1] + 1
#     grams.append(name[start_pos:stop_pos])

# print(grams)
num = 4
for i, letter in enumerate(name):
    start = i
    stop = i + num
    if stop > len(name):
        break
    print(name[start:stop])
    print(name[i: i + num]) # same thing without making new names



# for i in range(len(name)):
#     if i + num > len(name):
#         break
#     grams.append(name[i:i + num])
