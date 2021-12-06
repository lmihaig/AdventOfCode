inputFile = open("day24.txt", mode="r")

Hexagons = set()

for l in inputFile:
    l = l.strip()
    x, y, z = 0, 0, 0
    i = 0
    while l:
        if l.startswith('e'):
            x += 1
            y -= 1
            l = l[1:]
        elif l.startswith('se'):
            y -= 1
            z += 1
            l = l[2:]
        elif l.startswith('sw'):
            x -= 1
            z += 1
            l = l[2:]
        elif l.startswith('w'):
            x -= 1
            y += 1
            l = l[1:]
        elif l.startswith('nw'):
            z -= 1
            y += 1
            l = l[2:]
        elif l.startswith('ne'):
            x += 1
            z -= 1
            l = l[2:]
        else:
            assert False
    if(x, y, z) in Hexagons:
        Hexagons.remove((x, y, z))
    else:
        Hexagons.add((x, y, z))
print("Part1: ", len(Hexagons))

for _ in range(100):
    newHexagons = set()
    floor = set()
    for (x, y, z) in Hexagons:
        floor.add((x, y, z))
        for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
            floor.add((x+dx, y+dy, z+dz))

    for (x, y, z) in floor:
        blacks = 0
        for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
            if (x+dx, y+dy, z+dz) in Hexagons:
                blacks += 1
        if (x, y, z) in Hexagons:
            if blacks > 0 and blacks < 3:
                newHexagons.add((x, y, z))
        if (x, y, z) not in Hexagons and blacks == 2:
            newHexagons.add((x, y, z))
    Hexagons = newHexagons
print("Part2: ", len(Hexagons))
