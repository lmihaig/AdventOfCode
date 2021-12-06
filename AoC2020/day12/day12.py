inputFile = open("day12.txt", mode="r")

east = 0
north = 0
facing = 0 #east = 0; north = 1; west = 2; south = 3;

lines = []
for line in inputFile:
    lines.append(line.strip())


for l in lines:
    action = l[0]
    value = int(l[1:])
    if action == 'N':
        north += value
    elif action == 'S':
        north -= value
    elif action == 'E':
        east += value
    elif action == 'W':
        east -= value
    elif action == 'L':
        facing = (facing + value // 90)%4
    elif action == 'R':
        facing = (facing - value // 90)%4
    elif action == 'F':
        if facing == 0:
            east += value
        elif facing == 1:
            north += value
        elif facing == 2:
            east -= value
        elif facing == 3:
            north -= value

print("Task1:", abs(north)+abs(east))

east = 0
north = 0
waypointEast = 10
waypointNorth = 1
#facing = 0 #east = 0; north = 1; west = 2; south = 3;

for l in lines:
    action = l[0]
    value = int(l[1:])
    if action == 'N':
        waypointNorth += value
    elif action == 'S':
        waypointNorth -= value
    elif action == 'E':
        waypointEast += value
    elif action == 'W':
        waypointEast -= value
    elif action == 'L':
         for i in range(value // 90):
            aux = waypointEast
            waypointEast = -waypointNorth
            waypointNorth = aux
    elif action == 'R':
        for i in range(value // 90):
            aux = waypointEast
            waypointEast = waypointNorth
            waypointNorth = -aux
    elif action == 'F':
        east += waypointEast * value
        north += waypointNorth * value

print("Task2:", abs(north)+abs(east))