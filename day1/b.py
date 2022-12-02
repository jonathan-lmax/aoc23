with open('a') as f:
    lines = f.readlines()
calories = 0
maxCalories = 0
secondCalories = 0
thirdCalories = 0
def addCalories(moreCalories):
    global thirdCalories
    global secondCalories
    global maxCalories
    if (moreCalories >= thirdCalories):
        if (moreCalories >= secondCalories):
            thirdCalories = secondCalories
            if (moreCalories >= maxCalories):
                secondCalories = maxCalories
                maxCalories = moreCalories
                return
            secondCalories = moreCalories
            return
        thirdCalories = moreCalories
        return
for line in lines:
    if len(line.strip()) > 0:
        calories += int(line.strip())
    else:
        addCalories(calories)
        calories = 0
addCalories(calories)
print(max(calories, maxCalories + secondCalories + thirdCalories))

