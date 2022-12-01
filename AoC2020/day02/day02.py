import re
inputFile = open("day02.txt", mode="r")

key1 = 0
key2 = 0

for line in inputFile:
    # 5-6 v: vvvgvb

    words = re.split('-| |: |\n', line)

    minChar = int(words[0])
    maxChar = int(words[1])
    reqChar = words[2]
    string = list(words[3])
    countChar = 0

    for char in string:
        if reqChar == char:
            countChar += 1

    if minChar <= countChar <= maxChar:
        key1 += 1

    if (string[minChar - 1] == reqChar) ^ (string[maxChar - 1] == reqChar):
        key2 += 1

print("Task1 : {}\nTask2 : {}".format(key1, key2))
