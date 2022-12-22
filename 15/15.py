# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')
#targetY = 10
targetY = 2000000

# Part 1 #################################
signals = []
for line in input_lines:
    clauseSensor = line.split(":")[0]
    sensorX = int(clauseSensor.split(",")[0].split("=")[1])
    sensorY = int(clauseSensor.split(",")[1].split("=")[1])
    clauseBeacon = line.split("is at ")[1]
    beaconX = int(clauseBeacon.split(",")[0].split("=")[1])
    beaconY = int(clauseBeacon.split(",")[1].split("=")[1])
    #print(line)
    #print("sensor:"+str(sensorX)+","+str(sensorY)+"; beacon:"+str(beaconX)+","+str(beaconY))
    signals.append([(sensorX, sensorY), (beaconX, beaconY)])
#print(signals)

xExclusions = set()
for signal in signals:
    #print(signal)
    sensor = signal[0]
    beacon = signal[1]
    manDist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    #print(manDist)
    xRange = manDist - abs(targetY - sensor[1])
    #print(xRange)
    if xRange > 0:
        for i in range(sensor[0] - xRange, sensor[0] + xRange + 1):
            if beacon[1] == targetY and beacon[0] == i:
                continue
            xExclusions.add(i)

#print(xExclusions)
print(len(xExclusions))


# Part 2 #################################
