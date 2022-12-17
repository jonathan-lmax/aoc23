class Throw:
    def __init__(self, itemWorry, targetMonkeyIndex):
        self.itemWorry = itemWorry
        self.targetMonkeyIndex = targetMonkeyIndex

    def to(self, monkeys):
        monkeys[self.targetMonkeyIndex].catch(self.itemWorry)


class Monkey:
    def __init__(self, items, operation, test, successIndex, failIndex):
        self.items = items
        self.operation = operation
        self.test = test
        self.successIndex = successIndex
        self.failIndex = failIndex
        self.inspectionCount = 0

    def turn(self):
        throws = []
        for item in self.items:
            worry = self.operation.apply(item) // 3
            targetIndex = self.failIndex if worry % self.test else self.successIndex
            throws += [Throw(worry, targetIndex)]
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
        line = 0
        while line < len(lines):
            startingItems = [int(worry) for worry in lines[line + 1].strip()
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
            test = int(lines[line + 3].strip()[len("Test: divisible by "):])
            successIndex = int(
                lines[line + 4].strip()[len("If true: throw to monkey "):])
            failIndex = int(
                lines[line + 5].strip()[len("If false: throw to monkey "):])
            monkeys += [Monkey(startingItems, operation,
                               test, successIndex, failIndex)]
            line += 7
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
    for i in range(0, 20):
        game.playRound()
    inspectionCounts = [m.getInspectionCount() for m in monkeys]
    inspectionCounts.sort(reverse=True)
    print(inspectionCounts[0] * inspectionCounts[1])
