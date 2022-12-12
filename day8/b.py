class Tree:
    def __init__(self, height, row, column):
        self.height = height
        self.row = row
        self.column = column
        self.height = height
        self.scoreAbove = 0
        self.scoreLeft = 0
        self.scoreRight = 0
        self.scoreBelow = 0

    def addScoreAbove(self, score):
        self.scoreAbove += score

    def addScoreLeft(self, score):
        self.scoreLeft += score

    def addScoreRight(self, column):
        self.scoreRight += column - self.column

    def addScoreBelow(self, row):
        self.scoreBelow += row - self.row

    def getScore(self):
        return self.scoreAbove * self.scoreLeft * self.scoreRight * self.scoreBelow

    def __str__(self):
        return str(self.row) + " " + str(self.column) + " " + str(self.scoreAbove) + " " + str(self.scoreLeft) + " " + str(self.scoreRight) + " " + str(self.scoreBelow)


class TreeLine:
    def __init__(self):
        self.trees = {}

    def add(self, tree, position):
        if not self.trees.has_key(position):
            self.trees[position] = []
        self.trees[position] += [tree]


class TreesByHeight:
    def __init__(self):
        self.trees = [[], [], [], [], [], [], [], [], [], []]

    def nextHeight(self, tree, height):
        completedTrees = []
        for i in range(0, height + 1):
            completedTrees += self.trees[i]
            self.trees[i] = []
        self.trees[height] += [tree]
        return completedTrees


class DistanceToLastHeight:
    def __init__(self):
        self.distance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def nextHeight(self, height):
        distance = min(self.distance[height:10])
        for i in range(0, 10):
            self.distance[i] += 1
        self.distance[height] = 1
        return distance


class Day8:
    def __init__(self):
        self.lines = []

    def read(self):
        with open('a.txt') as f:
            self.lines += [l.strip() for l in f.readlines()]

    def solve(self):
        columnsFromTop = []
        columnsFromBottom = []
        for height in [int(cell) for cell in self.lines[0]]:
            scoreFromTop = DistanceToLastHeight()
            scoreFromTop.nextHeight(height)
            columnsFromTop += [scoreFromTop]
            columnsFromBottom += [TreesByHeight()]
        highScore = 0
        row = 0
        for line in self.lines[1:]:
            column = 0
            scoreFromLeft = DistanceToLastHeight()
            scoreFromRight = TreesByHeight()
            for height in [int(cell) for cell in line]:
                tree = Tree(height, row, column)
                tree.addScoreAbove(columnsFromTop[column].nextHeight(height))
                tree.addScoreLeft(scoreFromLeft.nextHeight(height))
                for oldTree in scoreFromRight.nextHeight(tree, height):
                    oldTree.addScoreRight(column)
                for oldTree in columnsFromBottom[column].nextHeight(tree, height):
                    oldTree.addScoreBelow(row)
                    highScore = max(highScore, oldTree.getScore())
                column += 1
            row += 1
            for oldTree in scoreFromRight.nextHeight(tree, 9):
                oldTree.addScoreRight(column - 1)
        for columnFromBottom in columnsFromBottom:
            for oldTree in columnFromBottom.nextHeight(None, 9):
                oldTree.addScoreBelow(row - 1)
                highScore = max(highScore, oldTree.getScore())
        print(highScore)


day8 = Day8()
day8.read()
day8.solve()
