import random


pokemon = [ ['pikachu', 'electric'],
            ['snivy','grass'],
            ['eevee', 'normal'],
            ['snom','ice']]

all_friends = []

for _ in range(10):
    my_friend = {}
    pokemon_choice = random.choice(pokemon)
    # species = pokemon_choice[0]
    # type = pokemon_choice[1]
    species, type = pokemon_choice # equiv

    my_friend['name'] = species
    my_friend['type'] = type
    my_friend['nickname'] = "you do this one"

    modifier = random.random()
    # print(modifier)
    level = random.randint(1, 30)
    hp = 5 * level * modifier # possible max: 5 * 30 * 1, min: 5 * 1 * .000001

    hp = max(hp, 5)

    my_friend['base_hp'] = hp
    my_friend['current_hp'] = hp
    my_friend['wins'] = 0
    my_friend['losses'] = 0
    # print(my_friend)
    all_friends.append(my_friend)

print(all_friends)

import json

# writing out json
with open('pokemon_friends.json', 'w', encoding='utf-8') as outfile:
    json.dump(all_friends, outfile, indent=4)

#reading in json
with open('pokemon_friends.json', 'r', encoding='utf-8') as infile:
    friend_data = json.load(infile)

print(friend_data)


with open('name_meta_info.json', 'r', encoding='utf-8') as infile:
    name_meta = json.load(infile)

print(len(name_meta['duos']), len(name_meta['lens']))
