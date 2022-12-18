from collections import deque


def getViableNextSteps(maze, step):
    nextSteps = []
    if step[0] > 0:
        nextSteps += [(step[0] - 1, step[1])]
    if step[0] + 1 < len(maze):
        nextSteps += [(step[0] + 1, step[1])]
    if step[1] > 0:
        nextSteps += [(step[0], step[1] - 1)]
    if step[1] + 1 < len(maze[0]):
        nextSteps += [(step[0], step[1] + 1)]
    return nextSteps


def getStartPoint(maze, finalDestinationMarker):
    startPoint = None
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] < 0:
                if maze[i][j] == finalDestinationMarker:
                    startPoint = (i, j, 26)
                    maze[i][j] = 0
                else:
                    maze[i][j] = 1
    return startPoint


finalDestinationMarker = ord('E') - ord('a') + 1
with open("a.txt") as f:
    maze = [[ord(c) - ord('a') + 1 for c in line.strip()]
            for line in f.readlines()]
steps = 1
minimalSteps = 0
queue = deque()
queue.append(getStartPoint(maze, finalDestinationMarker))
while not minimalSteps:
    iterationSize = len(queue)
    while iterationSize:
        iterationSize -= 1
        step = queue.popleft()
        for nextStep in getViableNextSteps(maze, step):
            nextHeight = maze[nextStep[0]][nextStep[1]]
            if nextHeight and nextHeight >= step[2] - 1:
                if nextHeight == 1:
                    minimalSteps = steps
                queue.append((nextStep[0], nextStep[1], nextHeight))
                maze[nextStep[0]][nextStep[1]] = 0
    steps += 1
print(minimalSteps)
