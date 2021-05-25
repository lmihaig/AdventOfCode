import copy
inputFile = open("day11.txt", mode="r")

seats = []
adjecency = [(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]
#row, column

for line in inputFile:
    seats.append(list(line.strip()))

initialSeats = copy.deepcopy(seats)
newSeats = copy.deepcopy(seats)
n = len(seats)
m = len(seats[0])

def adjecenedOccupied(row, column):
    count = 0
    for x,y in adjecency:
        if (0 <= (row + x) < n) and (0 <= (column + y) < m):
            if seats[row + x][column + y] == '#':
                count += 1
    return count

def seek(row, column):
    count = 0
    for x,y in adjecency:
        i = 1
        while (0 <= (row + x*i) < n) and (0 <= (column + y*i) < m):
            if seats[row + x*i][column + y*i] != '.':
                if seats[row + x*i][column + y*i] == '#':
                    count += 1
                break
            i += 1
    return count

def occupiedSeats(seats):
    return sum(seats[i][j] == '#' for i in range(n) for j in range(m))

check = False
while check == False:
    check = True
    for i in range(n):
        for j in range(m):
            adjecened = adjecenedOccupied(i, j)
            if seats[i][j] == 'L' and adjecened == 0:
                newSeats[i][j] = '#'
                check = False
            elif seats[i][j] == '#' and adjecened >= 4:
                newSeats[i][j] = 'L'
                check = False
            else:
                newSeats[i][j] = seats[i][j]
    seats = copy.deepcopy(newSeats)

print("Task1:",occupiedSeats(seats))

seats = copy.deepcopy(initialSeats)
newSeats = copy.deepcopy(initialSeats)
check = False
while check == False:
    check = True
    for i in range(n):
        for j in range(m):
            adjecened = seek(i, j)
            if seats[i][j] == 'L' and adjecened == 0:
                newSeats[i][j] = '#'
                check = False
            elif seats[i][j] == '#' and adjecened >= 5:
                newSeats[i][j] = 'L'
                check = False
            else:
                newSeats[i][j] = seats[i][j]
    seats = copy.deepcopy(newSeats)

print("Task2:",occupiedSeats(seats))