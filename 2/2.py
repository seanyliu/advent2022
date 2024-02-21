# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
    }

sum = 0

for line in input_lines:
    game_id = int(line.split(":")[0].split(" ")[1])
    draws = line.split(": ")[1].split("; ")
    game_is_valid = True
    for draw in draws:
        for cubes in draw.split(", "):
            count = int(cubes.split(" ")[0])
            color = cubes.split(" ")[1]
            if count > bag[color]:
                game_is_valid = False
    if game_is_valid:
        sum += game_id

# print(sum)

# Part 2 #################################

sum = 0

for line in input_lines:
    game_id = int(line.split(":")[0].split(" ")[1])
    draws = line.split(": ")[1].split("; ")
    fewest = {
        'red': 0,
        'green': 0,
        'blue': 0
        }

    for draw in draws:
        for cubes in draw.split(", "):
            count = int(cubes.split(" ")[0])
            color = cubes.split(" ")[1]
            if count > fewest[color]:
                fewest[color] = count
    power = 1
    for color in fewest:
        power = power * fewest[color]
    sum += power

print(sum)


