with open('a.txt') as f:
    lines = f.readlines()
rows = []
stacks = [[], [], [], [], [], [], [], [], []]
startedMoving = False
for line in lines:
    if len(line) > 1 and line[1] == "1":
        while rows:
            row = rows.pop()
            stack = 0
            for block in row:
                if block != ' ':
                    stacks[stack] += [block]
                stack += 1
        continue
    if line.strip() == "":
        startedMoving = True
        continue
    if startedMoving:
        command = line.strip().split(' ')
        moves = int(command[1])
        src = int(command[3]) - 1
        dest = int(command[5]) - 1
        while moves:
            stacks[dest] += [stacks[src].pop()]
            moves -= 1
    else:
        col = 1
        row = []
        while col < len(line):
            row += [line[col]]
            col += 4
        rows += [row]
message = ""
for stack in stacks:
    message += stack.pop()
print(message)

