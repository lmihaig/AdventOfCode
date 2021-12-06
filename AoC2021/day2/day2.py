file = open("day2.txt", "r")

lines = file.readlines()
lines = [line.rstrip() for line in lines]

horizontal = 0
depth = 0
aim = 0
movdic = {"up": -1, "down": 1, "forward": 1}

for line in lines:
    direction, num = line.split()
    num = int(num)
    if direction == "up" or direction == "down":
        aim += num * movdic[direction]
    else:
        horizontal += num * movdic[direction]
        depth += aim * num * movdic[direction]

print(f"horizontal: {horizontal}, depth: {depth}, aim: {aim}")
print("Part1: ", horizontal*aim)

print("Part2: ", horizontal*depth)
