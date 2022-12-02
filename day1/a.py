with open('a') as f:
    lines = f.readlines()
calories = 0
maxCalories = 0
for line in lines:
    if len(line.strip()) > 0:
        calories += int(line.strip())
    else:
        maxCalories = max(calories, maxCalories)
        calories = 0
print(max(calories, maxCalories))

