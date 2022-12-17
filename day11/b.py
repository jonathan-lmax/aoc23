class Sequence:
    def __init__(self):
        self.count = 0

    def get(self):
        self.count += 1
        return self.count


class Item:
    def __init__(self, worry, sequence):
        self.initialWorry = worry
        self.id = sequence.get()
        self.tests = {}

    def addTests(self, testMods):
        for testMod in testMods:
            self.tests[testMod] = self.initialWorry % testMod

    def apply(self, operation):
        for testMod in self.tests:
            worry = self.tests[testMod]
            self.tests[testMod] = operation.apply(worry) % testMod
            # print("worry %d -> %d -> %d (%% %d)" %
            #       (worry, operation.apply(worry), self.tests[testMod], testMod))

    def test(self, testMod):
        return not self.tests[testMod]


class Throw:
    def __init__(self, item, targetMonkeyIndex):
        self.item = item
        self.targetMonkeyIndex = targetMonkeyIndex
        # print("Throws %d to %d" % (item.id, targetMonkeyIndex))

    def to(self, monkeys):
        monkeys[self.targetMonkeyIndex].catch(self.item)


class Monkey:
    def __init__(self, items, operation, testMod, successIndex, failIndex):
        self.items = items
        self.operation = operation
        self.testMod = testMod
        self.successIndex = successIndex
        self.failIndex = failIndex
        self.inspectionCount = 0

    def addTests(self, testMods):
        for item in self.items:
            item.addTests(testMods)

    def turn(self):
        throws = []
        for item in self.items:
            item.apply(self.operation)
            testResult = item.test(self.testMod)
            targetIndex = self.successIndex if testResult else self.failIndex
            throws += [Throw(item, targetIndex)]
            self.inspectionCount += 1
        self.items = []
        return throws

    def catch(self, item):
        self.items += [item]

    def getInspectionCount(self):
        return self.inspectionCount


class MultiplyOperation:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def apply(self, multiplicand):
        return multiplicand * self.multiplier


class AddOperation:
    def __init__(self, addend):
        self.addend = addend

    def apply(self, augend):
        return augend + self.addend


class SquareOperation:
    def apply(self, opend):
        return opend * opend


class Parser:
    def parse(self, lines):
        monkeys = []
        testMods = []
        line = 0
        itemCount = Sequence()
        while line < len(lines):
            startingItems = [Item(int(worry), itemCount) for worry in lines[line + 1].strip()
                             [len("starting items: "):].split(",")]
            operator = lines[line + 2][len("  Operation: new = old ")]
            operand = lines[line +
                            2].strip()[len("Operation: new = old + "):]
            if operator == '+':
                operation = AddOperation(int(operand))
            elif operand == 'old':
                operation = SquareOperation()
            else:
                operation = MultiplyOperation(int(operand))
            testMod = int(lines[line + 3].strip()[len("Test: divisible by "):])
            testMods += [testMod]
            successIndex = int(
                lines[line + 4].strip()[len("If true: throw to monkey "):])
            failIndex = int(
                lines[line + 5].strip()[len("If false: throw to monkey "):])
            monkeys += [Monkey(startingItems, operation,
                               testMod, successIndex, failIndex)]
            line += 7
        for monkey in monkeys:
            monkey.addTests(testMods)
        return monkeys


class KeepAway:
    def __init__(self, monkeys):
        self.monkeys = monkeys

    def playRound(self):
        throws = []
        m = 0
        for monkey in self.monkeys:
            m += 1
            for throw in monkey.turn():
                throw.to(self.monkeys)


with open("a.txt") as f:
    monkeys = Parser().parse(f.readlines())
    game = KeepAway(monkeys)
    for i in range(0, 10000):
        print(i)
        game.playRound()
    inspectionCounts = [m.getInspectionCount() for m in monkeys]
    inspectionCounts.sort(reverse=True)
    print(inspectionCounts[0] * inspectionCounts[1])
