# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')
#targetY = 10
#targetY = 2000000
maxXY = 4000000
#maxXY = 20

# Part 1 #################################
signals = []
for line in input_lines:
    clauseSensor = line.split(":")[0]
    sensorX = int(clauseSensor.split(",")[0].split("=")[1])
    sensorY = int(clauseSensor.split(",")[1].split("=")[1])
    clauseBeacon = line.split("is at ")[1]
    beaconX = int(clauseBeacon.split(",")[0].split("=")[1])
    beaconY = int(clauseBeacon.split(",")[1].split("=")[1])
    signals.append([(sensorX, sensorY), (beaconX, beaconY)])

# create a giant set:
distress = []
for y in range(0, maxXY+1):

    targetY = y

    xExclusions = []
    for signal in signals:
        #print("signal:"+str(signal))
        sensor = signal[0]
        beacon = signal[1]
        manDist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        xRange = manDist - abs(targetY - sensor[1])
        if xRange > 0:
            exclL = sensor[0] - xRange
            exclR = sensor[0] + xRange
            #print("xrange:"+str(exclL)+","+str(exclR))

            '''
            # update the exclude left by expanding to match the lowest existing range
            for interval in xExclusions:
                if exclL < interval[0]:
                    break
                exclL = interval[0]

            # update exclude right by expanding to match the highest existing range
            for interval in xExclusions:
                if exclR > interval[1]:
                    break
                exclL = interval[1]
            print(str(exclL)+","+str(exclR)+" (updated)")
            '''

            updateExclusions = []
            for interval in xExclusions:
                #print("interval:"+str(interval))
                # case: the interval is completely to the left of the new exclusion range
                if (interval[1] < exclL):
                    updateExclusions.append(interval)
                    continue

                # case: the interval's right edge catches the left of the new exclusion range
                if (exclL <= interval[1] and interval[0] <= exclL and interval[1] <= exclR):
                    exclL = interval[0]
                    continue

                # case: the interval is entirely within the exclusion range
                if (exclL <= interval[0] and interval[1] <= exclR):
                    continue

                # case: the interval entirely subsumes the new exclusion range
                if (interval[0] <= exclL and interval[1] >= exclR):
                    exclL = interval[0]
                    exclR = interval[1]
                    continue

                # case: the interval's left edge catches the right of the exclusion range
                if interval[0] >= exclL and interval[0] <= exclR and interval[1] >= exclR:
                    exclR = interval[1]
                    continue

                # case: the interval is completely to the right of the new exclusion range
                if interval[0] >= exclR:
                    updateExclusions.append(interval)
                    continue

                print("ERROR: interval:"+str(interval)+" exclL:"+str(exclL)+" exclR:"+str(exclR))
                
            updateExclusions.append((exclL, exclR))
            xExclusions = updateExclusions

            # clean up the exclusion range
            xExclusions.sort(key=lambda x: x[0])

            #print("xExclusions" + str(xExclusions))

    # truncate to 0 -> maxXY
    updateExclusions = []
    for interval in xExclusions:
        if interval[1] < 0:
            continue
        elif interval[0] < 0 and interval[1] <= maxXY:
            updateExclusions.append((0, interval[1]))
        elif interval[0] > maxXY:
            continue
        elif interval[0] < 0 and interval[1] >= maxXY:
            updateExclusions.append((0, maxXY))
        else:
            updateExclusions.append((interval[0], interval[1]))
    xExclusions = updateExclusions
    
    distress.append(xExclusions)

print("Finished building distress set")

# search for the single beacon
for y in range(len(distress)):
    xExclusions = distress[y]
    if len(xExclusions) > 1:
        print(y)
        print(xExclusions)
    #print(xExclusions)
    

'''
print(xExclusions)
#print(len(xExclusions))

sum = 0
for x in xExclusions:
    sum += (x[1] - x[0]) + 1

print(sum)
'''

# ANSWER: 2655411*4000000+3166538 = 1062164716653810621647166538


# Part 2 #################################
