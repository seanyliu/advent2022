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

def is_symbol(x):
    if x.isnumeric():
        return False
    if x == ".":
        return False
    return True

def is_symbol_adjacent(x, y, grid):
    if y-1 in grid[x] and is_symbol(grid[x][y-1]):
        return True
    elif y+1 in grid[x] and is_symbol(grid[x][y+1]):
        return True
    elif x-1 in grid and is_symbol(grid[x-1][y]):
        return True
    elif x+1 in grid and is_symbol(grid[x+1][y]):
        return True
    elif x-1 in grid and y-1 in grid[x-1] and is_symbol(grid[x-1][y-1]):
        return True
    elif x-1 in grid and y+1 in grid[x-1] and is_symbol(grid[x-1][y+1]):
        return True
    elif x+1 in grid and y-1 in grid[x+1] and is_symbol(grid[x+1][y-1]):
        return True
    elif x+1 in grid and y+1 in grid[x+1] and is_symbol(grid[x+1][y+1]):
        return True
    return False

def get_number_at(x, y, grid):
    output = grid[x][y]

    i = x - 1
    while i in grid and str(grid[i][y]).isnumeric():
        output = grid[i][y] + output
        i = i-1

    i = x + 1
    while i in grid and str(grid[i][y]).isnumeric():
        output = output + grid[i][y]
        i = i+1

    return output

def get_number_start(x, y, grid):
    output = grid[x][y]

    i = x - 1
    while i in grid and str(grid[i][y]).isnumeric():
        output = grid[i][y] + output
        i = i-1
    return i+1

min_x = helpers.get_grid_min_x(grid)
max_x = helpers.get_grid_max_x(grid)
min_y = helpers.get_grid_min_y(grid)
max_y = helpers.get_grid_max_y(grid)

numbers = set()
    
for y in range(min_y, int(max_y)+1):
  for x in range(min_x, max_x+1):
    if (x in grid and y in grid[x]):
      if grid[x][y].isnumeric():
          if is_symbol_adjacent(x, y, grid):
              #print(grid[x][y])
              numbers.add((get_number_start(x, y, grid), y, get_number_at(x, y, grid)))

sum = 0
for item in numbers:
    sum += int(item[2])
print(sum)

# Part 2 #################################

def is_gear(x, y, grid):
    neighbors = set()
    
    if y-1 in grid[x] and grid[x][y-1].isnumeric():
        neighbors.add((get_number_start(x, y-1, grid), y-1))
    if y+1 in grid[x] and grid[x][y+1].isnumeric():
        neighbors.add((get_number_start(x, y+1, grid), y+1))
    if x-1 in grid and grid[x-1][y].isnumeric():
        neighbors.add((get_number_start(x-1, y, grid), y))
    if x+1 in grid and grid[x+1][y].isnumeric():
        neighbors.add((get_number_start(x+1, y, grid), y))
    if x-1 in grid and y-1 in grid[x-1] and grid[x-1][y-1].isnumeric():
        neighbors.add((get_number_start(x-1, y-1, grid), y-1))
    if x-1 in grid and y+1 in grid[x-1] and grid[x-1][y+1].isnumeric():
        neighbors.add((get_number_start(x-1, y+1, grid), y+1))
    if x+1 in grid and y-1 in grid[x+1] and grid[x+1][y-1].isnumeric():
        neighbors.add((get_number_start(x+1, y-1, grid), y-1))
    if x+1 in grid and y+1 in grid[x+1] and grid[x+1][y+1].isnumeric():
        neighbors.add((get_number_start(x+1, y+1, grid), y+1))

    product = 1
    if len(neighbors) >= 2:
        for n in neighbors:
            product = product * int(get_number_at(n[0], n[1], grid))

    return product
    

sum = 0
for y in range(min_y, int(max_y)+1):
  for x in range(min_x, max_x+1):
    if (x in grid and y in grid[x]):
      if grid[x][y] == "*":
          product = is_gear(x, y, grid)
          if (product > 1):
              sum += product

print(sum)
