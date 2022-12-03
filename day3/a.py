with open('a.txt') as f:
    lines = f.readlines()
prioritySum = 0
for rucksack in lines:
    compartmentSize = int(len(rucksack) / 2)
    compartmentA = set(rucksack[:compartmentSize])
    compartmentB = set(rucksack[compartmentSize:-1])
    misplacedItem = compartmentA.intersection(compartmentB).pop()
    if ord(misplacedItem) >= ord('a'):
        prioritySum += ord(misplacedItem) - ord('a') + 1
    else:
        prioritySum += ord(misplacedItem) - ord('A') + 27
print(prioritySum)
