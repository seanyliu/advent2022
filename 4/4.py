# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
count = 0
overlap = 0
for line in input_lines:
    elf1 = line.split(",")[0]
    elf2 = line.split(",")[1]
    s1 = set()
    s2 = set()
    for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1):
        s1.add(i)
    for j in range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1):
        s2.add(j)
    inter = s1.intersection(s2)
    if len(inter) == min(len(s1), len(s2)):
        count += 1

    if len(inter) > 0:
        overlap += 1
print(count)
print(overlap)

# Part 2 #################################
