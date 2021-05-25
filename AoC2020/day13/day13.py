from functools import reduce
inputFile = open("day13.txt", mode="r")

time = int(inputFile.readline())
buses = []
earliestArrival = []


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


for line in inputFile:
    buses = (line.strip().split(','))

for bus in buses:
    if bus != 'x':
        bus = int(bus)
        first = (time // bus) + 1
        earliestArrival.append([bus, first*bus])

print("Task1:", (earliestArrival[0][1] - time) * earliestArrival[0][0])

n = []
a = []

for i, bus in enumerate(buses):
    if bus != "x":
        bus = int(bus)
        n.append(bus)
        a.append((-i) % bus)

print("Task2:", chinese_remainder(n, a))
