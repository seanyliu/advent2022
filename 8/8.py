# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
grid = helpers.get_grid_from_lines(input_lines)
#helpers.print_grid(grid)

def isVisible(tree, x, y, grid):
    min_y = min(grid[0].keys())
    max_y = max(grid[0].keys())
    min_x = min(grid.keys())
    max_x = max(grid.keys())
    # check left
    visibleFromLeft = True
    for xTest in range(min_x, x):
        testTree = grid[xTest][y]
        if testTree >= tree:
            visibleFromLeft = False
            break

    visibleFromRight = True
    for xTest in range(x+1, max_x+1):
        testTree = grid[xTest][y]
        if testTree >= tree:
            visibleFromRight = False
            break

    visibleFromTop = True
    for yTest in range(min_y, y):
        testTree = grid[x][yTest]
        if testTree >= tree:
            visibleFromTop = False
            break

    visibleFromBottom = True
    for yTest in range(y+1, max_y+1):
        testTree = grid[x][yTest]
        if testTree >= tree:
            visibleFromBottom = False
            break
    return visibleFromLeft or visibleFromRight or visibleFromTop or visibleFromBottom


def getScenicScore(tree, x, y, grid):
    tree = int(tree)
    
    min_y = min(grid[0].keys())
    max_y = max(grid[0].keys())
    min_x = min(grid.keys())
    max_x = max(grid.keys())
    # check left
    leftCount = 0
    for xTest in range(min_x, x):
        testTree = int(grid[x - xTest - 1][y])
        leftCount += 1
        if testTree >= tree:
            break

    rightCount = 0
    for xTest in range(x+1, max_x+1):
        testTree = int(grid[xTest][y])
        rightCount += 1
        if testTree >= tree:
            break

    topCount = 0
    for yTest in range(min_y, y):
        testTree = int(grid[x][y - yTest - 1])
        topCount += 1
        #print(str(x) + "," + str(y - yTest) + "testTree "+str(testTree))
        if testTree >= tree:
            break

    bottomCount = 0
    for yTest in range(y+1, max_y+1):
        testTree = int(grid[x][yTest])
        bottomCount += 1
        if testTree >= tree:
            break

    #print ("left: "+str(leftCount))
    #print ("right: "+str(rightCount))
    #print ("top: "+str(topCount))
    #print ("bottom: "+str(bottomCount))
    

    return leftCount * rightCount * topCount * bottomCount


    
count = 0
min_y = min(grid[0].keys())
max_y = max(grid[0].keys())
for y in range(min_y, max_y+1):
  line = ""
  min_x = min(grid.keys())
  max_x = max(grid.keys())
  for x in range(min_x, max_x+1):
      tree = grid[x][y]
      if isVisible(tree, x, y, grid):
          count += 1
      #print(tree)

print(count)

# Part 2 #################################

viewingGrid = helpers.copy_grid(grid)

#print(getScenicScore("5", 2, 3, grid))

min_y = min(grid[0].keys())
max_y = max(grid[0].keys())
for y in range(min_y, max_y+1):
  line = ""
  min_x = min(grid.keys())
  max_x = max(grid.keys())
  for x in range(min_x, max_x+1):
      tree = grid[x][y]
      viewingGrid[x][y] = getScenicScore(tree, x, y, grid)

#helpers.print_grid(viewingGrid)


alltrees = []
min_y = min(viewingGrid[0].keys())
max_y = max(viewingGrid[0].keys())
for y in range(min_y, max_y+1):
  line = ""
  min_x = min(viewingGrid.keys())
  max_x = max(viewingGrid.keys())
  for x in range(min_x, max_x+1):
      alltrees.append(viewingGrid[x][y])

print(max(alltrees))
