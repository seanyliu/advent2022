# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################

# construct the graph
class Valve:
    def __init__(self, name, neighbors, rate):
        self.name = name
        self.neighbors = neighbors
        self.rate = rate

valves = {}

for line in input_lines:
    name = line.split(" has ")[0].split(" ")[1]
    line = line.replace("valves ", "valve ")
    neighbors = line.split(" to valve ")[1].split(", ")
    rate = int(line.split("=")[1].split(";")[0])
    valve = Valve(name, neighbors, rate)
    valves[name] = valve

q = []
q.append(["AA", 0, 0, set()]) # node name, total pressure, min passed, opened set
maxPressure = 0
visited = {}
'''
[AA] = {
  time:pressure,
  time2:pressure}
'''
openableValveCount = 0
for v in valves.keys():
    if valves[v].rate > 0:
        openableValveCount += 1

while len(q) > 0:
    node = q.pop(0)
    name = node[0]
    valve = valves[name]
    pressure = node[1]
    time = node[2]
    opened = node[3]
    #print("at node "+name+" pressure "+str(pressure)+" time "+str(time)+" opened "+str(opened))

    # add to visited list
    pruned = False
    if name in visited:
        #print("name:"+name)
        #print(visited[name].keys())
        #print("time1="+str(time))
        if time > min(visited[name].keys()):
            #print("time2="+str(time))
            # check if we're at the same node with a lower pressure, but at a later time
            for t in visited[name].keys():
                #print("t="+str(t)+"; time="+str(time))
                if (t <= time):
                    if visited[name][t] >= pressure:
                        #print("prune")
                        pruned = True
                        break
            visited[name][time] = pressure
            #print("add to visited")
            #print(visited)
        else:
            visited[name][time] = pressure
            #print("add to visited")
            #print(visited)
    else:
        visited[name] = {}
        visited[name][time] = pressure
    if (pruned):
        continue
    #print(visited)

    if time >= 30 or len(opened) >= openableValveCount:
        if pressure > maxPressure:
            maxPressure = pressure
            continue

    for neighbor in valve.neighbors:
        #print(neighbor)
        n = valves[neighbor]

        # open valve
        if valve.rate > 0 and time <= 30 - 1 and valve.name not in opened:
            nopened = opened.copy()
            nopened.add(valve.name)
            q.append([n.name, pressure+valve.rate*(30 - time - 1), time+2, nopened])

        # move, without opening
        q.append([n.name, pressure, time+1, opened])

    q.sort(key=lambda x:x[1])

    #print(q)

print(maxPressure)

# Part 2 #################################
