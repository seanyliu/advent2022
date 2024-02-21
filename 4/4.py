# regular imports ########################
import math
import os, sys
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
def countMatching(line):
    line = re.sub(r"\s\s+" , " ", line)
    card = line.split(":")[0].split(" ")[1]
    winning = line.split(":")[1].split(" | ")[0].split()
    winSet = set()
    for w in winning:
        winSet.add(int(w))
    have = line.split(":")[1].split(" | ")[1].split()
    count = 0
    for h in have:
        if int(h) in winSet:
            count += 1
    return count


sum = 0
for line in input_lines:
    score = int(math.pow(2,countMatching(line)-1))
    sum += score

print(sum)

print("Begin part 2")

# Part 2 #################################

instances = {}
for j in range(0, len(input_lines)):
    instances[j+1] = 1

cardFound = True
i = 1
while i in instances:
    cardFound = False
    card = input_lines[i-1]
    for j in range(0, countMatching(card)):
        key = i+j+1
        instances[key] += 1 * instances[i]
        cardFound = True
    i += 1
    #print(countMatching(card))
    #print(card)

count = 0
for key in instances:
    count += instances[key]
print(count)

    
    
