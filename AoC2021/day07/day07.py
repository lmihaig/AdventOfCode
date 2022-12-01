import statistics
import math

with open("day07.txt", 'r') as file:
    lines = file.read().strip().split(",")

positions = [int(position) for position in lines]

median = int(statistics.median(positions))
fuelcost = sum([abs(x - median) for x in positions])
print("Part1:", fuelcost)


def gauss(num):
    return num*(num+1)//2


mean = statistics.mean(positions)
mean1, mean2 = math.floor(mean), math.ceil(mean)
for mean in [mean1, mean2]:
    fuelcost = sum([gauss(abs(x-mean)) for x in positions])
    print(f"Part2 with mean={mean}: {fuelcost}")
