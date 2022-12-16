class Machine:
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.signalStrength = 0

    def noop(self):
        self.cycle += 1
        if (self.cycle - 20) % 40 == 0:
            self.signalStrength += self.cycle * self.X
            print(self.cycle, self.X, self.signalStrength)

    def addX(self, amount):
        self.noop()
        self.noop()
        self.X += amount

    def getSignalStrength(self):
        return self.signalStrength


class Day10:
    def __init__(self):
        self.lines = []
        self.machine = Machine()

    def read(self, file):
        with open(file) as f:
            self.lines += [l.strip() for l in f.readlines()]

    def solve(self):
        for l in self.lines:
            input = l.split(' ')
            command = input[0]
            if command == "noop":
                self.machine.noop()
            elif command == "addx":
                self.machine.addX(int(input[1]))

    def write(self):
        print(self.machine.getSignalStrength())


day10 = Day10()
day10.read("a.txt")
day10.solve()
day10.write()
