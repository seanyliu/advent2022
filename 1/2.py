# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

def find_num(line):
    digits = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    for digit in digits:
        if line.find(digits[digit]) == 0:
            return digit
    return -1
        

# Part 2 #################################
sum = 0
for line in input_lines:
    first_digit = ""
    last_digit = ""
    for x in range(len(line)):
        if (line[x].isnumeric()):
            if first_digit == "":
                first_digit = line[x]
            last_digit = line[x]
        else:
            sdigit = find_num(line[x:len(line)])
            if sdigit != -1:
                if first_digit == "":
                    first_digit = str(sdigit)
                last_digit = str(sdigit)

    sum += int(first_digit + last_digit)
print(sum)
