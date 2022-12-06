with open('a.txt') as f:
    line = f.readlines()[0]
i = 4
while len(set(line[(i - 4):i])) < 4:
    i += 1
print(i)
