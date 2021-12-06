inputFile = open("day3.txt", mode="r") 

Map = []
lenght = 0
trees = 0
key = 1

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

for line in inputFile:
    Map.append(line.strip())

lenght = len(Map)
width = len(Map[0])

for (rightStep,downStep) in slopes:
    y = 0
    x = 0
    trees = 0
    while x < lenght:
        if Map[x][y % width] == '#':
            trees += 1
        y += rightStep
        x += downStep
    key *= trees
    print("Trees for slope ({},{}): {}".format(rightStep, downStep, trees))

print("Task2: ", key)
