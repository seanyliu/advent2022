# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

class Folder:
    def __init__(self, name, files, parent):
        self.name = name
        self.files = files
        self.parent = parent
    def __str__(self):
        return f"{self.name}({self.files})"
    def size(self):
        size = 0
        for f in self.files:
            if isinstance(f, File):
                size += f.size
            else:
                size += f.size()
        return size
        

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################

root = False
currFolder = False

for line in input_lines:
    words = line.split(" ")
    match words[0]:
        case "$":
            match words[1]:
                case "cd":
                    match words[2]:
                        case "/":
                            f = Folder("/", [], False)
                            root = f
                            currFolder = f
                        case "..":
                            currFolder = currFolder.parent
                        case _:
                            f = Folder(words[2], [], currFolder)
                            currFolder.files.append(f)
                            currFolder = f
        case "dir":
            x = 1
        case _:
            size = words[0]
            filename = words[1]
            f = File(filename, int(size))
            currFolder.files.append(f)

#print(currFolder.files)

def count_size(folder, counts):
    counts.append(folder.size())
    for f in folder.files:
        if isinstance(f, Folder):
            count_size(f, counts)

counts = []
count_size(root, counts)
print(counts)

sum = 0
for c in counts:
    if c <= 100000:
        sum += c

print(sum)

spaceToFree = 30000000 - (70000000 - root.size())
counts.sort()
print("space to Free: "+str(spaceToFree))
print(counts)

for c in counts:
    if c >= spaceToFree:
        print(c)
        break


# Part 2 #################################
