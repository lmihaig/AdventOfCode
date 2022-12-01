import re
inputFile = open("day04.txt", mode="r")

valid = 0
valid2 = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid'

passports = inputFile.read().split('\n\n')


def validare(passportDict):
    ok = False
    if re.compile("[0-9]").match(passportDict["byr"]) and 1920 <= int(passportDict["byr"]) <= 2002:
        if re.compile("[0-9]").match(passportDict["iyr"]) and 2010 <= int(passportDict["iyr"]) <= 2020:
            if re.compile("[0-9]").match(passportDict["eyr"]) and 2020 <= int(passportDict["eyr"]) <= 2030:
                if re.compile("^#[0-9a-f]{6}$").match(passportDict["hcl"]):
                    if passportDict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        if re.compile(r"^\d{9}$").match(passportDict["pid"]):
                            if "in" in passportDict["hgt"] and 59 <= int(passportDict["hgt"][:-2]) <= 76:
                                ok = True
                            elif "cm" in passportDict["hgt"] and 150 <= int(passportDict["hgt"][:-2]) <= 193:
                                ok = True
    return ok


for passport in passports:
    passportDict = {}
    passportFields = re.split(" |\n", passport)
    passportFields = [i.split(':') for i in passportFields]
    for i in passportFields:
        index = passportFields.index(i)
        passportDict[passportFields[index][0]] = passportFields[index][1]
    if all(passportDict.__contains__(field) for field in fields):
        valid += 1
        if validare(passportDict):
            valid2 += 1


print("Task1: ", valid)
print("Task2: ", valid2)
