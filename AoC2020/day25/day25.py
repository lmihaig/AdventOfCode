inputFile = open("day25.txt", mode="r")

a, b = [int(line) for line in inputFile]


def bruteforce(x):
    i = 1
    while i:
        if pow(7, i, 20201227) == x:
            return i
        i += 1


print(pow(a, bruteforce(b), 20201227))
