inputFile = open("day22.txt", mode="r")

L = inputFile.read().split("\n\n")
myDeck = [int(x) for x in L[0].split("\n")[1:]]
crabDeck = [int(x) for x in L[1].split("\n")[1:]]



while myDeck and crabDeck:
    remove = 0
    lenght = min([len(myDeck), len(crabDeck)])
    for cardIndex in range(lenght):
        if myDeck[cardIndex] > crabDeck[cardIndex]:
            myDeck += [myDeck[cardIndex]] + [crabDeck[cardIndex]]
        else:
            crabDeck += [crabDeck[cardIndex]] + [myDeck[cardIndex]]
        remove += 1
    myDeck = myDeck[remove:]
    crabDeck = crabDeck[remove:]

score = 0
i = len(myDeck + crabDeck)
for card in myDeck + crabDeck:
    score += card * i
    i -= 1

print("Task1:", score)

myDeck = [int(x) for x in L[0].split("\n")[1:]]
crabDeck = [int(x) for x in L[1].split("\n")[1:]]

def recursiveCombat(myDeck, crabDeck):
    seen = set()
    while myDeck and crabDeck:
        if (tuple(myDeck),tuple(crabDeck)) in seen:
            return True
        seen.add((tuple(myDeck),tuple(crabDeck)))
        myNewDeck = myDeck.pop(0)
        crabNewDeck = crabDeck.pop(0)
        if len(myDeck) >= myNewDeck and len(crabDeck) >= crabNewDeck:
            winner = recursiveCombat(myDeck[:myNewDeck], crabDeck[:crabNewDeck])
            if winner:
                myDeck += [myNewDeck] + [crabNewDeck]
                
            else:
                crabDeck += [crabNewDeck] + [myNewDeck]
        else:
            if myNewDeck > crabNewDeck:
                myDeck += [myNewDeck] + [crabNewDeck]
            else:
                crabDeck += [crabNewDeck] + [myNewDeck]
    return len(myDeck) > 0

recursiveCombat(myDeck,crabDeck)

score = 0
i = len(myDeck + crabDeck)
for card in myDeck + crabDeck:
    score += card * i
    i -= 1
print("Task2:", score)
