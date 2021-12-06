inputFile = open("day15.txt", mode="r")

nums = []
for num in inputFile.readline().split(","):
    nums.append(int(num))

#Task2
print("progress:",end=" ",flush=True)

numsApp = {n: i for i, n in enumerate(nums)}
lastNum = nums[-1]
for i in range(len(numsApp), 30000000):
    if lastNum not in numsApp:
        new = 0
    else:
        new = i - numsApp[lastNum] - 1
    numsApp[lastNum] = i - 1
    lastNum = new

    if not i%1000000:
        print("#",end="",flush=True)

print("\nTask2:", lastNum)

"""
while len(nums) < 2020:
    lenght = len(nums)
    if nums[-1] in nums[:-1]:
        nums.append(nums[-2::-1].index(nums[-1]) + 1)
    else:
        nums.append(0)

print("Task1:",nums[-1])
"""