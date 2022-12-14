class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def navigate(self, direction):
        match direction:
            case 'R':
                return Spot(self.x + 1, self.y)
            case 'U':
                return Spot(self.x, self.y + 1)
            case 'L':
                return Spot(self.x - 1, self.y)
            case 'D':
                return Spot(self.x, self.y - 1)

    def follow(self, other):
        moveX= False
        moveY = False
        if abs(self.x - other.x) > 1:
            moveX = True
            if self.y != other.y:
                moveY = True
        if abs(self.y - other.y) > 1:
            moveY = True
            if self.x != other.x:
                moveX = True
        x = self.x
        y = self.y
        if moveX:
           x = self.x + 1 if self.x < other.x else self.x - 1
        if moveY:
           y = self.y + 1 if self.y < other.y else self.y - 1
        return Spot(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "%s, %s" % (self.x, self.y)

    def __repr__(self):
        return "%s, %s" % (self.x, self.y)


class Day9:
    def __init__(self):
        self.lines = []
        self.answer = 0

    def read(self, file):
        with open(file) as f:
            self.lines = f.readlines()

    def solve(self):
        head = Spot(500, 500)
        tail = Spot(500, 500)
        visited = { head }
        for line in self.lines:
            direction = line[0]
            amount = int(line[2:-1])
            while amount:
                head = head.navigate(direction)
                tail = tail.follow(head)
                visited.add(tail)
                amount = amount - 1
        self.answer = len(visited)

    def write(self):
        print(self.answer)


day9 = Day9()
day9.read("test1.txt")
day9.solve()
day9.write()
day9.read("a.txt")
day9.solve()
day9.write()

