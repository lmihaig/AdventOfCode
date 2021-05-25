import re
inputFile = open("day19.txt", mode="r")
rules = {}
messages = []

L = inputFile.read().split("\n\n")


def matchRule(rules, ruleNumbers, message):
    if not ruleNumbers:
        return not message
    ruleNumber, *ruleNumbers = ruleNumbers
    rule = rules[ruleNumber]
    if isinstance(rule, str):
        return (message.startswith(rule) and matchRule(rules, ruleNumbers, message[len(rule):]))
    else:
        return any(matchRule(rules, option + ruleNumbers, message) for option in rule)


for line in L[0].split("\n"):
    line = line.strip()
    groups = re.match(
        r"(\d*): (?:\"([a-z])\"|(\d+(?: \d+)*(?: \| \d+(?: \d+)*)*))", line)
    rule = int(groups.group(1))
    if groups.group(2):
        rules[rule] = groups.group(2)
    elif groups.group(3):
        numbers = groups.group(3).split('|')
        rules[rule] = [list(map(int, re.findall(r'\d+', option)))
                       for option in numbers]

for line in L[1].split("\n"):
    messages.append(line.strip())

count = 0
for message in messages:
    if matchRule(rules, [0], message):
        count += 1

print("Task1:", count)

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
count = 0
for message in messages:
    if matchRule(rules, [0], message):
        count += 1
print("Task2:", count)
