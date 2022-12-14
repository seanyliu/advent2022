# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
grid = {}
for line in input_lines:
    points = line.split(" -> ")
    for i in range(1,len(points)):
        ox = int(points[i-1].split(",")[0])
        oy = int(points[i-1].split(",")[1])
        px = int(points[i].split(",")[0])
        py = int(points[i].split(",")[1])
        for x in range(min(ox, px), max(ox, px)+1):
            for y in range(min(oy, py), max(oy, py)+1):
                helpers.add_to_grid(x, y, "#", grid)

sandStart = (500, 0)

abyssY = helpers.get_grid_max_y(grid)

'''
isAbyss = False

sandCount = 0
while(True):
    
    #print(i)
    sandCurrentPos = sandStart
    newPos = None
    while True:
        x = sandCurrentPos[0]
        y = sandCurrentPos[1]

        if (x in grid and y+1 in grid[x]) and (grid[x][y+1] == "#" or grid[x][y+1] == "o"):
            if (x-1 in grid and y+1 in grid[x-1]) and (grid[x-1][y+1] == "#" or grid[x-1][y+1] == "o"):
                if (x+1 in grid and y+1 in grid[x+1]) and (grid[x+1][y+1] == "#" or grid[x+1][y+1] == "o"):
                    newPos = (x, y)
                    break
                else:
                    newPos = (x+1, y+1)
            else:
                newPos = (x-1, y+1)
        else:
            newPos = (x, y+1)

        sandCurrentPos = newPos
        if y > abyssY:
            isAbyss = True
            break

    if (isAbyss):
        print(sandCount)
        break

    sandCount += 1
    helpers.add_to_grid(sandCurrentPos[0], sandCurrentPos[1], "o", grid)
    #helpers.print_grid(grid)
'''
    

# Part 2 #################################
sandFloor = abyssY+2
sandCount = 0
isDone = False
while(True):
    sandCurrentPos = sandStart
    newPos = None
    while True:
        x = sandCurrentPos[0]
        y = sandCurrentPos[1]
        if ((x in grid and y+1 in grid[x]) and (grid[x][y+1] == "#" or grid[x][y+1] == "o")) or (y+1 >= sandFloor):
            if ((x-1 in grid and y+1 in grid[x-1]) and (grid[x-1][y+1] == "#" or grid[x-1][y+1] == "o")) or (y+1 >= sandFloor):
                if ((x+1 in grid and y+1 in grid[x+1]) and (grid[x+1][y+1] == "#" or grid[x+1][y+1] == "o")) or (y+1 >= sandFloor):
                    newPos = (x, y)
                    break
                else:
                    newPos = (x+1, y+1)
            else:
                newPos = (x-1, y+1)
        else:
            newPos = (x, y+1)

        sandCurrentPos = newPos
        
    sandCount += 1
    helpers.add_to_grid(sandCurrentPos[0], sandCurrentPos[1], "o", grid)
    
    if (newPos[0] == sandStart[0]) and (newPos[1] == sandStart[1]):
        print("done")
        print(sandCount)
        #helpers.print_grid(grid)
        isDone = True
        break
