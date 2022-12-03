# regular imports ########################
import math
import os, sys
import itertools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
sum = 0
for line in input_lines:
    first = line[0:int(len(line)/2)]
    second = line[int(len(line)/2):]
    for char in first:
        if char in second:
            val = 0
            if (char.isupper()):
                val = ord(char) - ord('A') + 27
            else:
                val = ord(char) - ord('a') + 1
            sum += val
            break;

print(sum)

# Part 2 #################################

sum = 0

for i in range(0, len(input_lines), 3):
    first = input_lines[i]
    second = input_lines[i+1]
    third = input_lines[i+2]
    for char in first:
        if (char in second) and (char in third):
            val = 0
            if (char.isupper()):
                val = ord(char) - ord('A') + 27
            else:
                val = ord(char) - ord('a') + 1
            sum += val
            break;

print(sum)

'''
comb = list(itertools.combinations(input_lines, 3))

print (len(comb))

badges = []
for c in comb:
    first = c[0]
    second = c[1]
    third = c[2]
    badgeFound = False
    for char in first:
        if (char in second) and (char in third):
            badgeFound = True
            badges.append(char)
            break;

print(len(badges))
'''

