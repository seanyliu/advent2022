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
'''
lineIsInitialStacks = True
stacks = {}
for line in input_lines:
    if line == "":
        lineIsInitialStacks = False
        continue
        
    if lineIsInitialStacks:
        if '[' in line:
            for c in range(0, len(line), 4):
                crate = line[c+1]
                if crate != " ":
                    pile = int(c / 4)+1
                    if pile not in stacks:
                        stacks[pile] = []
                    stacks[pile].insert(0, crate)
        else:
            for c in range(0, len(line), 4):
                stack = line[c]
                # do nothing really, since I already accounted for stacks

    else:
        matchObj = re.match(r'move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)', line)
        for i in range(0, int(matchObj.group(1))):
            stacks[int(matchObj.group(3))].append(stacks[int(matchObj.group(2))].pop())

code = ""
for i in range(len(stacks.keys())):
    code = code + stacks[i+1].pop()

print(code)
'''



# Part 2 #################################
lineIsInitialStacks = True
stacks = {}
for line in input_lines:
    if line == "":
        lineIsInitialStacks = False
        continue
        
    if lineIsInitialStacks:
        if '[' in line:
            for c in range(0, len(line), 4):
                crate = line[c+1]
                if crate != " ":
                    pile = int(c / 4)+1
                    if pile not in stacks:
                        stacks[pile] = []
                    stacks[pile].insert(0, crate)
        else:
            for c in range(0, len(line), 4):
                stack = line[c]
                # do nothing really, since I already accounted for stacks

    else:
        matchObj = re.match(r'move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)', line)
        stacks[int(matchObj.group(3))].extend(stacks[int(matchObj.group(2))][int(matchObj.group(1))*-1:])
        stacks[int(matchObj.group(2))] = stacks[int(matchObj.group(2))][:int(matchObj.group(1))*-1]

code = ""
for i in range(len(stacks.keys())):
    code = code + stacks[i+1].pop()

print(code)
