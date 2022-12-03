with open('a.txt') as f:
    lines = f.readlines()
prioritySum = 0
elfInGroup = 1
groupSharedItems = []
for rucksack in lines:
    if elfInGroup == 1:
        groupSharedItems = set(rucksack.strip())
    elif elfInGroup == 2:
        groupSharedItems = groupSharedItems.intersection(set(rucksack.strip()))
    elif elfInGroup == 3:
        badge = groupSharedItems.intersection(set(rucksack.strip())).pop()
        if ord(badge) >= ord('a'):
            prioritySum += ord(badge) - ord('a') + 1
        else:
            prioritySum += ord(badge) - ord('A') + 27
    elfInGroup = elfInGroup % 3 + 1
print(prioritySum)
