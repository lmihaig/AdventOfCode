inputFile = open("day14.txt", mode="r")

numere1 = {}
numere2 = {}

def write(memory, mask, address, value):
    if "X" in mask:
        i = mask.index("X")
        write(memory, mask[:i] + "0" + mask[i+1:], address, value)
        write(memory, mask[:i] + "1" + mask[i+1:], address, value)
    else:
        memory[int(mask, 2) | address] = value

for line in inputFile:
    line = line.strip().split(" = ")
    if line[0] == "mask":
        mask = line[1]
    else:
        adress = int(line[0][4:-1])
    
        numere1[adress] = (int(line[1]) & int(mask.replace("1", "0").replace("X", "1"), 2)) | int(mask.replace("X", "0"), 2)

        adress = adress & int(mask.replace("0", "1").replace("X", "0"), 2)
        write(numere2, mask, adress, int(line[1]))

print("Task1:", sum(numere1.values()))
print("Task2:", sum(numere2.values()))