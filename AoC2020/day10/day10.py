inputFile = open("day10.txt", mode="r")

adapters = []
joltage = 0
singleJoltDiff= 0
threeJoltDiff = 0

arrangementList = {}

def arrangements(adapter):
    ans = 0
    if adapter in arrangementList:
        return arrangementList[adapter]
    if adapter == len(adapters) - 1:
        return 1
    for i in range(adapter + 1, len(adapters)):
        if adapters[i] - 3 <= adapters[adapter]:
            ans += arrangements(i)
    arrangementList[adapter] = ans
    return ans

for line in inputFile:
    adapters.append(int(line.strip()))

adapters.append(0)
adapters.sort()
adapters.append(max(adapters) + 3)

for adapter in adapters:
    if adapter != 0:
        if adapter - 3 <= joltage:
            if adapter - 1 == joltage:
                singleJoltDiff += 1
            elif adapter - 3 == joltage:
                threeJoltDiff += 1
            joltage = adapter

print("Task1: ", singleJoltDiff * threeJoltDiff)
print("Task2: ", arrangements(0))