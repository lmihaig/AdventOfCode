with open("day06.txt", 'r') as file:
    initialstate = file.read().strip().split(",")

initialfish = [int(x) for x in initialstate]

# nextday = []
# currentday = initialstate
# for _ in range(256):
#     newfish = 0
#     for fish in currentday:
#         if fish == 0:
#             newfish += 1
#             nextday.append(6)
#         else:
#             nextday.append(fish-1)
#         while newfish > 0:
#             nextday.append(8)
#             newfish -= 1
#     currentday = nextday
#     nextday = []

fishes = {i: 0 for i in range(10)}
for fish in initialfish:
    fishes[fish] += 1

for currentday in range(256):
    nextdayFish = {i: 0 for i in range(10)}
    nextdayFish[6] = nextdayFish[8] = fishes[0]
    for fish in range(8):
        nextdayFish[fish] += fishes[fish+1]
    fishes = nextdayFish
    if currentday == 79:
        print("Part1:", sum(fishes.values()))

print("Part2:", sum(fishes.values()))
