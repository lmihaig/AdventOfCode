inputFile = open("day21.txt", mode="r")

dictionary = {}
allIngredients = []

for line in inputFile:
    line = line.strip().strip(")").split(" (contains ")
    ingredients = line[0].split()
    allergens = line[1]
    allIngredients.append(ingredients)
    allergens = allergens.split(", ")
    for allergen in allergens:
        if allergen not in dictionary:
            dictionary[allergen] = set(ingredients)
        else:
            dictionary[allergen] = dictionary[allergen] & set(ingredients)

identified = {}
while dictionary:
    for allergen, ingredients in dictionary.items():
        if len(ingredients) == 1:
            break
    if not ingredients:
        break
    [ingredient] = ingredients
    identified[allergen] = ingredient
    for ingredients in dictionary.values():
        ingredients -= {ingredient}

count = 0
for ingredients in allIngredients:
    for ingredient in ingredients:
        if ingredient not in identified.values():
            count += 1

print("Task1:", count)

dangerousIngredient = []
identifiedKeys = sorted(identified)
for item in identifiedKeys:
    dangerousIngredient.append(identified[item])

print("Task2:", *dangerousIngredient, sep = ',')