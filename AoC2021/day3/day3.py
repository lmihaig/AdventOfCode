from collections import Counter


file = open("day3.txt", "r")

lines = file.readlines()
lines = [line.rstrip() for line in lines]

gamma = ""
epsilon = ""
for b in range(len(lines[0])):
    count = Counter([byte[b] for byte in lines])
    if count["0"] > count["1"]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"


print("Part1: ", int(gamma, 2) * int(epsilon, 2))

oxigen_gen = ""
carbondioxide_scrub = ""

oxigen_list = carbondioxide_list = lines

i = 0
pattern = ""
while(len(oxigen_list) > 1):
    count = Counter([byte[i] for byte in oxigen_list])
    if count["0"] > count["1"]:
        pattern += "0"
    else:
        pattern += "1"
    oxigen_list = [byte for byte in oxigen_list if byte.startswith(pattern)]
    i += 1


i = 0
pattern = ""
while(len(carbondioxide_list) > 1):
    count = Counter([byte[i] for byte in carbondioxide_list])
    if count["1"] < count["0"]:
        pattern += "1"
    else:
        pattern += "0"
    carbondioxide_list = [
        byte for byte in carbondioxide_list if byte.startswith(pattern)]
    i += 1

oxigen_gen = oxigen_list[0]
carbondioxide_scrub = carbondioxide_list[0]
print("Part2: ", int(oxigen_gen, 2) * int(carbondioxide_scrub, 2))
