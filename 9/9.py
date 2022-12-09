# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

def updateTail(H, T):
    deltaX = H[0] - T[0]
    deltaY = H[1] - T[1]
    if abs(deltaX) >= 2 and abs(deltaY) >= 2:
        T = (T[0] + deltaX - int(deltaX/abs(deltaX)), T[1] + deltaY - int(deltaY/abs(deltaY)))
    elif abs(deltaX) >= 2 and abs(deltaY) >= 1:
        T = (T[0] + deltaX - int(deltaX/abs(deltaX)), T[1] + deltaY)
    elif abs(deltaX) >= 1 and abs(deltaY) >= 2:
        T = (T[0] + deltaX, T[1] + deltaY - int(deltaY/abs(deltaY)))
    elif abs(deltaX) >= 2:
        T = (T[0] + deltaX - int(deltaX/abs(deltaX)), T[1])
    elif abs(deltaY) >= 2:
        T = (T[0], T[1] + deltaY - int(deltaY/abs(deltaY)))
    return T
    

# Part 1 #################################
visited = set()

rope = []
for i in range(10):
    rope.append((0, 0))

visited.add(rope[len(rope)-1])

for line in input_lines:
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    H = rope[0]
    for i in range(distance):
        match direction:
            case "R":
                H = (H[0]+1, H[1])
            case "U":
                H = (H[0], H[1]+1)
            case "L":
                H = (H[0]-1, H[1])
            case "D":
                H = (H[0], H[1]-1)
        rope[0] = H

        for i in range(len(rope)-1):
            T = updateTail(rope[i], rope[i+1])
            rope[i+1] = T
        
        #print ("H: "+str(H)+", T: "+str(rope[len(rope)-1]))
        #print (rope)
        visited.add(rope[len(rope)-1])
        
    #print (direction + " " + str(distance))

l = []
for visit in visited:
    l.append(visit)
l.sort()

print("visited: ")
print(l)
print(len(visited))

# Part 2 #################################
