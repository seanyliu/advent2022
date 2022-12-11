# regular imports ########################
import math
import os, sys
from math import gcd
from functools import reduce
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################
class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.operator = ""
        self.operand = 1
        self.test = 1
        self.trueMonkey = False
        self.falseMonkey = False
        self.inspects = 0
    def __repr__(self):
        return "Monkey "+str(self.name)+": "+str(self.items)+"; "+str(self.operator)+"; "+str(self.operand)+"; "+str(self.test)+"; "+str(self.trueMonkey)+"; "+str(self.falseMonkey)+"; "+str(self.inspects)

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

monkeys = []
currMonkey = False
for line in input_lines:
    if "Monkey" in line:
        m = Monkey(line.split(" ")[1].split(":")[0])
        monkeys.append(m)
        currMonkey = m
    elif "Starting" in line:
        items = line.split(": ")[1].split(", ")
        currMonkey.items = items
    elif "Operation" in line:
        currMonkey.operator = line.split(" = ")[1].split(" ")[1]
        currMonkey.operand = line.split(" = ")[1].split(" ")[2] # can be "old"
    elif "Test" in line:
        currMonkey.test = int(line.split("divisible by ")[1])
    elif "true" in line:
        currMonkey.trueMonkey = int(line.split("to monkey ")[1])
    elif "false" in line:
        currMonkey.falseMonkey = int(line.split("to monkey ")[1])

divisList = []
for m in monkeys:
    divisList.append(m.test)
lcm = lcm(divisList)

for round in range(0, 10000):
    #print(round)
    for m in monkeys:
        # inspect item
        while len(m.items) > 0:
            item = int(m.items.pop(0))
            m.inspects += 1
            #print ("inspecting "+str(item))
            match(m.operator):
                case "+":
                    match(m.operand):
                        case "old":
                            item = item + item
                        case _:
                            item = item + int(m.operand)
                case "*":
                    match(m.operand):
                        case "old":
                            item = item * item
                        case _:
                            item = item * int(m.operand)
            # item = int(int(item) / 3) # part 2
            item = int(item) % lcm
            #print(item)

            if item % int(m.test) == 0:
                monkeys[m.trueMonkey].items.append(item)
            else:
                monkeys[m.falseMonkey].items.append(item)
        #print(m)
print(monkeys)

inspects = []
for m in monkeys:
    inspects.append(m.inspects)
inspects.sort()
print(inspects)

print(inspects[len(inspects)-1] * inspects[len(inspects)-2])

# Part 1 #################################

# Part 2 #################################
