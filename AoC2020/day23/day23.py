from numpy.core.records import array


inputFile = open("day23.txt", mode="r")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


arr = []
for line in inputFile:
    for char in line:
        arr.append(int(char))
lenght = len(arr)

n = 100
nodes = {}
for i in range(lenght):
    nodes[arr[i]] = Node(arr[i])

for x, y in zip(arr, arr[1:]):
    nodes[x].next = nodes[y]
nodes[arr[-1]].next = nodes[arr[0]]

head = nodes[arr[0]]

for _ in range(n):
    pickupStart = head.next
    pickupEnd = head.next.next.next
    vals = [pickupStart.data, pickupStart.next.data, pickupEnd.data]
    if head.data > 1:
        goal = head.data - 1
    else:
        goal = lenght
    while goal in vals:
        goal -= 1
        if goal < 1:
            goal = lenght

    head.next = pickupEnd.next
    pickupEnd.next = nodes[goal].next
    nodes[goal].next = pickupStart

    head = head.next

ans = ""
head = nodes[1].next
for _ in range(lenght-1):
    ans += str(head.data)
    head = head.next

print("Part1: ", ans)

# Part Deux
arr = arr + [i for i in range(10, 1000001)]
lenght = len(arr)
n = 10000000
nodes = {}
for i in range(lenght):
    nodes[arr[i]] = Node(arr[i])

for x, y in zip(arr, arr[1:]):
    nodes[x].next = nodes[y]
nodes[arr[-1]].next = nodes[arr[0]]

head = nodes[arr[0]]

for _ in range(n):
    pickupStart = head.next
    pickupEnd = head.next.next.next
    vals = [pickupStart.data, pickupStart.next.data, pickupEnd.data]
    if head.data > 1:
        goal = head.data - 1
    else:
        goal = lenght
    while goal in vals:
        goal -= 1
        if goal < 1:
            goal = lenght

    head.next = pickupEnd.next
    pickupEnd.next = nodes[goal].next
    nodes[goal].next = pickupStart

    head = head.next

ans = nodes[1].next.data * nodes[1].next.next.data
print("Part2: ", ans)
