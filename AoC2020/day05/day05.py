inputFile = open("day05.txt", mode="r")

seats = []

for value in inputFile:
    firstRow = 0
    lastRow = 127
    firstColumn = 0
    lastColumn = 7
    for letter in value:
        if letter == 'F':
            lastRow = (firstRow + lastRow) // 2
        elif letter == 'B':
            firstRow = ((firstRow + lastRow) // 2) + 1
        elif letter == 'L':
            lastColumn = (firstColumn + lastColumn) // 2
        elif letter == 'R':
            firstColumn = ((firstColumn + lastColumn) // 2) + 1
    seats.append(firstRow * 8 + firstColumn)

print("Task1:", max(seats))

for i in range(min(seats), max(seats)):
    if i not in seats:
        print("Task2:", i)
