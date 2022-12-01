inputFile = open("day09.txt", mode="r")

nums = []

for line in inputFile:
    nums.append(int(line.strip()))

preambleSize = 25

for i in range(preambleSize, len(nums) + 1):
    check = False
    for x in range(i - preambleSize, i):
        for y in range(x + 1, i):
            if nums[i] == nums[x]+nums[y]:
                check = True
    if not check:
        check = nums[i]
        print("Task1: ", nums[i])
        break

found = False
for i in range(len(nums)):
    if not found:
        for j in range(i + 1, len(nums)):
            numberSum = nums[i:j]
            if sum(numberSum) == check:
                print("Task2: ", min(numberSum) + max(numberSum))
                found = True
