class Screen:
    def __init__(self):
        self.rows = []
        self.pixels = ""
        self.cycle = 0

    def render(self, sprite):
        self.pixels += "#" if abs(self.cycle - sprite) <= 1 else "."
        self.cycle += 1
        if self.cycle == 40:
            self.rows += [self.pixels]
            self.pixels = ""
            self.cycle = 0

    def dump(self):
        for row in self.rows:
            print(row)


class Machine:
    def __init__(self, screen):
        self.X = 1
        self.screen = screen

    def noop(self):
        self.screen.render(self.X)

    def addX(self, amount):
        self.noop()
        self.noop()
        self.X += amount


class Day10:
    def __init__(self):
        self.lines = []
        self.screen = Screen()

    def read(self, file):
        with open(file) as f:
            self.lines += [l.strip() for l in f.readlines()]

    def solve(self):
        machine = Machine(self.screen)
        for l in self.lines:
            input = l.split(' ')
            command = input[0]
            if command == "noop":
                machine.noop()
            elif command == "addx":
                machine.addX(int(input[1]))

    def write(self):
        print(self.screen.dump())


day10 = Day10()
day10.read("a.txt")
day10.solve()
day10.write()
