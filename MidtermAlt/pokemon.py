# Given the pokemon.json file, complete the following:
#  1. Output all the types and the total count of pokemon for that type
#    For example - Grass: 14, Poison: 33, etc.
#    There are 15 types in total
#  2. Output all the pokemon names and weights who have a weight >= 50kg
#    For example - Venusaur: 100, Blastoise: 85.5, etc.
#    There are 47 heavy pokemon

import json

pok_types = {'Grass':0, 'Poison':0, 'Fire':0, 'Flying':0, 'Bug':0, 'Water':0, 'Normal':0,'Electric':0, 'Ground':0, 'Psychic':0, 'Dragon':0, 'Ice':0, 'Rock':0, 'Fighting':0, 'Ghost':0}

try:
    with open('pokemon.json') as file:
        content = json.load(file)
    # Output all the types and the total count of pokemon for that type
    for item in content['pokemon']:
        for type in item['type']:
            pok_types[type] += 1
    poke_output = {"Pokemon types": len(pok_types), "Types are": pok_types}
    print(json.dumps(poke_output, indent=4))

    # Output all the pokemon names and weights who have a weight >= 50kg
    print("Here is a list of all the heavy pokemon:")
    hvy_count = 0
    for name in content['pokemon']:
        if not name['name']:
            continue
        weight = float(name['weight'].strip(" kg"))
        if weight >= 50:
            hvy_count += 1
            print("Name of pokemon is: {}, their weight is: {}".format(name['name'], name['weight']))
    print("There are {} heavy pokemon".format(hvy_count))
except Exception as err:
    print("An error occured")
