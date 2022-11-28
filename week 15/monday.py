import random


pokemon = [ ['pikachu', 'electric'],
            ['snivy','grass'],
            ['eevee', 'normal'],
            ['snom','ice']]


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


