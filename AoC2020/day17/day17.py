inputFile = open("day17.txt", mode="r")

lines = [l.rstrip('\n') for l in inputFile]

neighList = (-1, 0, 1)

def step(grid):
    newGrid = {}
    for x in range(min(k[0] for k in grid.keys())-1, max(k[0] for k in grid.keys())+2):
        for y in range(min(k[1] for k in grid.keys())-1, max(k[1] for k in grid.keys())+2):
            for z in range(min(k[2] for k in grid.keys())-1, max(k[2] for k in grid.keys())+2):
                    s = grid.get((x,y,z), False)
                    an = 0
                    for dx in neighList:
                        for dy in neighList:
                            for dz in neighList:
                                if dx == dy == dz == 0:
                                    continue
                                if grid.get((x+dx,y+dy,z+dz), False):
                                    an += 1
                    if (s and an in (2, 3)) or (not s and an == 3):
                        newGrid[(x,y,z)] = True
    return newGrid

grid = {}

for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        grid[(row, col, 0)] = ch == '#'


for i in range(6):
    grid = step(grid)
print("Task1:", sum(grid.values()))


def step4d(grid):
    newGrid = {}
    for x in range(min(k[0] for k in grid.keys())-1, max(k[0] for k in grid.keys())+2):
        for y in range(min(k[1] for k in grid.keys())-1, max(k[1] for k in grid.keys())+2):
            for z in range(min(k[2] for k in grid.keys())-1, max(k[2] for k in grid.keys())+2):
                for t in range(min(k[3] for k in grid.keys())-1, max(k[3] for k in grid.keys())+2):
                    s = grid.get((x,y,z,t), False)
                    an = 0
                    for dx in neighList:
                        for dy in neighList:
                            for dz in neighList:
                                for dt in neighList:
                                    if dx == dy == dz == dt == 0:
                                        continue
                                    if grid.get((x+dx,y+dy,z+dz,t+dt), False):
                                        an += 1
                    if (s and an in (2, 3)) or (not s and an == 3):
                        newGrid[(x,y,z,t)] = True
    return newGrid

grid = {}
for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        grid[(row, col, 0, 0)] = ch == '#'

for i in range(6):
    grid = step4d(grid)
print("Task2:", sum(grid.values()))