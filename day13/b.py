from enum import Enum


class SearchStatus(Enum):
    FAILED = 1
    ONGOING = 2
    SUCCEEDED = 3


class Packet:
    def __init__(self, root):
        self.root = root

    def lessOrEqual(self, other):
        return self.root.lessOrEqual(other.root) == SearchStatus.SUCCEEDED

    def __repr__(self):
        return str(self.root)


class List:
    def __init__(self, items):
        self.items = items

    def lessOrEqual(self, other):
        if isinstance(other, Integer):
            return self.lessOrEqual(List([other]))
        i = 0
        while i < len(self.items):
            if i == len(other.items):
                return SearchStatus.FAILED
            itemResult = self.items[i].lessOrEqual(other.items[i])
            if itemResult != SearchStatus.ONGOING:
                return itemResult
            i += 1
        return SearchStatus.ONGOING if i == len(other.items) else SearchStatus.SUCCEEDED

    def __repr__(self):
        return str(self.items)


class Integer:
    def __init__(self, value):
        self.value = value

    def lessOrEqual(self, other):
        if isinstance(other, List):
            return List([self]).lessOrEqual(other)
        if self.value < other.value:
            return SearchStatus.SUCCEEDED
        if self.value > other.value:
            return SearchStatus.FAILED
        return SearchStatus.ONGOING

    def __repr__(self):
        return str(self.value)


class Parser:
    def __init__(self, lines):
        self.lines = lines

    def parse(self):
        i = 0
        packets = []
        while i < len(self.lines):
            packets += [self.parsePacket(i), self.parsePacket(i + 1)]
            i += 3
        return packets

    def parsePacket(self, index):
        return Packet(self.parseList(self.lines[index].strip()[1:])[0])

    def parseList(self, data):
        i = 0
        items = []
        while i < len(data):
            if data[i] == '[':
                (subList, length) = self.parseList(data[i + 1:])
                items += [subList]
                i += length
            elif data[i] == ']':
                return (List(items), i + 1)
            elif data[i] != ',':
                (integer, length) = self.parseInteger(data[i:])
                items += [integer]
                i += length - 1
            i += 1

    def parseInteger(self, data):
        i = 0
        number = ""
        while not data[i] in "[,]":
            number += data[i]
            i += 1
        return (Integer(int(number)), len(number))


with open("a.txt") as f:
    packets = Parser(f.readlines()).parse()

i = 0
keys = Parser(["[[2]]", "[[6]]"]).parse()
keyIndex1 = 1
keyIndex2 = 2
while i < len(packets):
    if packets[i].lessOrEqual(keys[0]):
        keyIndex1 += 1
    if packets[i].lessOrEqual(keys[1]):
        keyIndex2 += 1
    i += 1
print(keyIndex1 * keyIndex2)
