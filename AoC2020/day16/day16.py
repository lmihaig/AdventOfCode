import re

inputFile = open("day16.txt", mode="r")
L = inputFile.read().split("\n\n")
invalid = []
tickets = []
myTicket = [int(x) for x in L[1].split("\n")[1].split(",")]

rules = re.findall("(.*): (.*)-(.*) or (.*)-(.*)", L[0])
rules = {name: list(range(int(a), int(b)+1)) + list(range(int(c), int(d)+1)) for name, a, b, c, d in rules}
rulesColumn = {name: [] for name in re.findall("(.*):", L[0])}
deleteList = []

for ticket in L[2].split("\n")[1:]:
    ticket = [int(x) for x in ticket.split(",")]
    tickets.append(ticket)

for ticket in tickets:
    for number in ticket:
        validity = False
        for rule in rules:
            if number in rules.get(rule):
                validity = True
        if not validity:
            invalid.append(number)
            deleteList.append(ticket)

print("Task1:", sum(invalid))

for ticket in deleteList:
    tickets.remove(ticket)
numRules = len(rules) 
numTickets = len(tickets)

for rule in rules:
    for j in range(numRules):
        columnValidity = True
        for i in range(numTickets):
            if tickets[i][j] not in rules[rule]:
                columnValidity = False
        if columnValidity:
                rulesColumn[rule].append(j)

sort = sorted(rulesColumn, key=lambda k: len(rulesColumn[k]))
for rule in sort:
    remove = rulesColumn[rule][0]
    for i in sort:
        if i != rule:
            if remove in rulesColumn[i]:
                rulesColumn[i].remove(remove)

prod = 1
departureList = [rulesColumn[k][0] for k in ["departure location", "departure station", "departure platform", "departure track", "departure date", "departure time"]]
for i in departureList:
    prod *= myTicket[i]

print("Task2:", prod)
