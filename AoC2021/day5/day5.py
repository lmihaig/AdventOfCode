from collections import defaultdict
with open("day5.txt", 'r') as file:
    lines = file.read().strip().split("\n")

diagram = defaultdict(lambda: 0)
diagramDiags = defaultdict(lambda: 0)
for line in lines:
    x1, y1 = [int(num) for num in line.split()[0].split(",")]
    x2, y2 = [int(num) for num in line.split()[2].split(",")]
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                diagram[(x, y)] += 1
    else:
        dx = 1 if x1 < x2 else -1
        dy = 1 if y1 < y2 else -1

        while x1 != x2 and y1 != y2:
            diagramDiags[(x1, y1)] += 1
            x1 += dx
            y1 += dy
        diagramDiags[(x1, y1)] += 1


ans = sum(value > 1 for value in diagram.values())
print("Part1: ", ans)

for coord in diagram:
    diagramDiags[coord] += diagram[coord]
ans = sum(value > 1 for value in diagramDiags.values())
print("Part2:", ans)
