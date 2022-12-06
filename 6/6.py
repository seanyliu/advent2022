# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
charBuffer = []
fullChars = []
for char in input_lines[0]:
    fullChars.append(char)
    charBuffer.append(char)
    if len(charBuffer) > 14:
        charBuffer.pop(0)
    if len(charBuffer) == 14:
        unique = True
        for b in range(len(charBuffer)):
            testList = charBuffer[:b]
            testList.extend(charBuffer[b+1:])
            if charBuffer[b] in testList:
                unique = False
        if unique:
            break

print(len(fullChars))

# Part 2 #################################
