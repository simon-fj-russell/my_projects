from collections import Counter
from random import randint


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
