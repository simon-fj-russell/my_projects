from random import randint
from collections import Counter


def get_key(val, given_dict):
    for key, value in given_dict.items():
        if val == value:
            return key


def step(monster_locations, world_map):
    for key, value in monster_locations.items():
        for city in world_map:
            if city[0] == value and len(city) > 1:
                direction = randint(1, len(city) - 1)
                monster_locations[key] = city[direction].split("=")[1]

    return monster_locations


def monster_fight(monster_locations, move):
    temp_list = []
    for key, value in monster_locations.items():
        temp_list.append(value)
        cont = Counter(temp_list)

    temp_cities = []
    for key, value in cont.items():
        if value >= 2:
            temp_cities.append(key)

    if len(temp_cities) > 0:
        print("")
        print("At move {} some monsters were in the same city.".format(move))

    for j in temp_cities:
        monster_1 = get_key(j, monster_locations)
        del monster_locations[monster_1]
        monster_2 = get_key(j, monster_locations)
        del monster_locations[monster_2]
        print("{} has been destroyed by monster {} and {}!".format(j, monster_1, monster_2))

    if len(temp_cities) > 0:
        print("Monsters left: {}".format(len(monster_locations)))

    return monster_locations, temp_cities


def remove_cities(cities_to_drop, world_map):
    for dest in cities_to_drop:
        for city in world_map:
            if dest == city[0]:
                del world_map[world_map.index(city)]
                for row in world_map:
                    for j in row[1:]:
                        if dest == j.split("=")[1]:
                            city_wm = world_map.index(row)
                            crossroad = row.index(j)
                            del world_map[city_wm][crossroad]

    return world_map

def starting_conditions():
    # Reads in the world map and creates a list of list
    with open('world_map_medium.txt', 'r') as f:
        world_map = []
        for line in f:
            world_map.append(line.strip('\n').split(" "))

    # Gets the number of monsters user wants
    print("There are {} cities.".format(len(world_map)))
    num_of_monsters = int(input("How many monsters would you like Lord? "))
    if num_of_monsters > len(world_map):
        num_of_monsters = int(input("Maybe too many monsters, pick again: "))

    # Places the monsters in the world at random.
    # Making sure that no 2 monsters are put in the same city
    placement = []
    while len(placement) < num_of_monsters:
        new_cell = randint(0, len(world_map) - 1)
        if new_cell not in placement:
            placement.append(new_cell)

    monster_locations = {}
    for i, x in zip(range(1, num_of_monsters + 1), placement):
        monster_locations[i] = world_map[x][0]

    return monster_locations, world_map

# Main code.
# Moves 10,000 times or until less then 2 monster are left.
# Moves the monsters using step function
# Checks if any monsters are in the same city, removes the monsters and gets a list of cities to drop
# Removes the city from the map
monster_locations, world_map = starting_conditions()
moves = 1
cities_destroyed = []
while moves < 10001 and len(monster_locations) > 1:
    monster_locations = step(monster_locations, world_map)
    monster_locations, cities_to_drop = monster_fight(monster_locations, moves)
    cities_destroyed.append(cities_to_drop)
    world_map = remove_cities(cities_to_drop, world_map)
    moves += 1
    if moves == 10001:
        print("")
        print("Reason for end:")
        print("Ran out of moves")
    elif len(monster_locations) == 1:
        print("")
        print("Reason for end:")
        print("There is only 1 monster left.")
    elif len(monster_locations) == 0:
        print("")
        print("Reason for end:")
        print("All the monsters are dead")

print("")
print("There are {} cities left and {} monsters.".format(len(world_map), len(monster_locations)))
