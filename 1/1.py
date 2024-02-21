# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
sum = 0
for line in input_lines:
    firstdigit = ""
    lastdigit = ""
    for character in line:
        if character.isnumeric():
            if firstdigit == "":
                firstdigit = character
            lastdigit = character
    sum += int(firstdigit + lastdigit)
print(sum)

# Part 2 #################################
