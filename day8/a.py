class TreeColumn:
    def __init__(self, height):
        self.height = height
        self.above = TreeHeightCount()
        self.below = TreeHeightCount()
        self.above.add(height, self)
    
    def add(self, nextHeight):
        self.height = nextHeight
        self.below.clear(nextHeight, False)
        if self.above.anyAsHighAs(nextHeight):
            return False
        else:
            self.above.add(nextHeight, self)
            return True

    def maybeVisibleFromBelow(self):
        self.below.add(self.height, self)

    def getVisibleFromBottom(self):
        return self.below.getTotal()

class TreeHeightCount:
    def __init__(self):
        self.heightCount = [None, None, None, None, None, None, None, None, None, None]

    def add(self, height, tree):
        self.heightCount[height] = tree

    def clear(self, height, fromRight):
        for i in range(0, height + 1):
            if self.heightCount[i]:
                if fromRight:
                    self.heightCount[i].maybeVisibleFromBelow()
                self.heightCount[i] = None

    def getTotal(self):
        return sum([bool(t) for t in self.heightCount])

    def anyAsHighAs(self, height):
        return sum([bool(t) for t in self.heightCount[height:]])

class Day8:
    def __init__(self):
        self.lines = []
        self.columns = []

    def solve(self):
        with open('a.txt') as f:
            self.lines += [l.strip() for l in f.readlines()]
        self.columns += [TreeColumn(int(height)) for height in self.lines[0]]
        visible = len(self.columns)
        for row in self.lines[1:]:
            column = 0
            heightFromLeft = -1 
            potentialVisibleFromRight = TreeHeightCount()
            for tree in [int(cell) for cell in row]:
                treeAbove = self.columns[column]
                potentialVisibleFromRight.clear(tree, True)
                if treeAbove.add(tree) or heightFromLeft < tree:
                    visible += 1
                    heightFromLeft = max(heightFromLeft, tree)
                else:
                    potentialVisibleFromRight.add(tree, treeAbove)
                column += 1
            visible += potentialVisibleFromRight.getTotal()
        visible += sum([t.getVisibleFromBottom() for t in self.columns])
        print(visible)

day8 = Day8()
day8.solve()

