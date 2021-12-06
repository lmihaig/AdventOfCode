file = open("day1.txt", "r")

lines = file.readlines()
lines = [int(line.rstrip()) for line in lines]

# count = 0
# for i in range(len(lines)):
#     if lines[i] > lines[i-1]:
#         count += 1
count = sum([a < b for a, b in zip(lines, lines[1:])])
print("Part1: ", count)

# count = 0
# lastwindow = sum(lines[0:0+3])
# for i in range(len(lines)):
#     window = sum(lines[i:i+3])
#     if window > lastwindow:
#         count += 1
#     lastwindow = window
count = sum([a < b for a, b in zip(lines, lines[3:])])
print("Part2: ", count)
