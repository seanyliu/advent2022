# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
cycles_to_complete = {
    "noop" : 1,
    "addx" : 2
}

X = 1
V = 0
cycle = 0
actionQ = []
actionCycle = 0
i = 0
isActionPending = False

sum = 0
grid = helpers.init_grid(39, 5, ".")
gridY = -1
pixelX = 0

while i < len(input_lines) or isActionPending is True:
    cycle += 1
    #print("begin cycle: "+str(cycle)+"; x="+str(X))
    
    # read next instruction
    if isActionPending is False:
        line = input_lines[i]
        instruction = line.split(" ")[0]
        actionCycle = cycle + cycles_to_complete[instruction] - 1
        actionQ.append(line)
        match (instruction):
            case "addx":
                V = int(line.split(" ")[1])
        i += 1
        isActionPending = True
        #print("Q: "+str(actionQ))

    if cycle == 20 or (cycle - 20) % 40 == 0:
        print("cycle:"+str(cycle))
        print(str(cycle * X))
        sum += cycle * X

    if cycle % 40 == 1:
        gridY += 1

    # check if cursor and pixel overlap
    if pixelX in range(X-1,X+2):
        grid[pixelX][gridY] = "#"
    pixelX += 1
    pixelX = pixelX % 40
        

    if cycle >= actionCycle:
        # take previous action
        if len(actionQ) > 0:
            line = actionQ.pop(0)
            instruction = line.split(" ")[0]
            match (instruction):
                case "addx":
                    X = X + V
            isActionPending = False

    #print("end cycle: "+str(cycle)+"; x="+str(X))
    #print("==")
       
helpers.print_grid(grid)

print ("end")
print("X="+str(X))
print("V="+str(V))
print(sum)

# Part 2 #################################
