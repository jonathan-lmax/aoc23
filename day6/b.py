with open('a.txt') as f:
    line = f.readlines()[0]
i = 14
while len(set(line[(i - 14):i])) < 14:
    i += 1
print(i)
