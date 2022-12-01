inputFile = open("day06.txt", mode="r")
key1 = 0
key2 = 0
groups = inputFile.read().split('\n\n')


for group in groups:
    increment = [0] * 128
    increment2 = [0] * 128
    answers = group.split('\n')
    for ans in answers:
        for letter in ans:
            if 'a' <= letter <= 'z':
                increment[ord(letter)] = 1
                increment2[ord(letter)] += 1

    for letter in range(ord('a'), ord('z')+1):
        key1 += increment[letter]
        if increment2[letter] == len(answers):
            key2 += 1


print("Task1: ", key1)
print("Task2: ", key2)
