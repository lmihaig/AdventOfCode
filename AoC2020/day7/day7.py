import re

inputFile = open("day7.txt", mode="r")
lines = [line.strip() for line in inputFile]

containDict = {}
containedIn = {}
holds = []

def isContainedIn(colour):
    for i in containedIn[colour]:
        if i not in holds:
            holds.append(i)
        if i in containedIn:
            isContainedIn(i)

def countBags(colour):
    counter = 0
    if colour in containDict:
        for numBags, containedColour in containDict[colour]:
            counter += numBags
            counter += numBags * countBags(containedColour)
    return counter
   
for line in lines:
    container = re.match("(.*) bags contain", line)[1]
    contains = re.findall("([0-9]) (.*?) bags?[, .]", line)
    
    for numBags, containedColour in contains:
        numBags = int(numBags)

        if containedColour not in containedIn:
            containedIn[containedColour] = []
        containedIn[containedColour].append(container)

        if container not in containDict:
            containDict[container] = []
        containDict[container].append((numBags, containedColour))

isContainedIn("shiny gold")
print("Task1:", len(holds))

shinyGold = countBags("shiny gold")
print("Task2:", shinyGold)

