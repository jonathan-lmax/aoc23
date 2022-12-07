class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directSize = 0
        self.indirectSize = 0
        self.files = {}
        self.directories = {}

    def getDirectory(self, directoryName):
        return self.directories[directoryName]

    def getParent(self):
        return self.parent

    def addDirectory(self, name, parent):
        self.directories[name] = Directory(name, parent)

    def addFile(self, size, name):
        self.directSize += size
        self.files[name] = size

    def populateIndirectSize(self):
        self.indirectSize = self.directSize
        print(self.name)
        print(self.directSize)
        if self.files:
            print(str(len(self.files)) + " files")
        for file in self.files:
            print(self.files[file])
        if self.directories:
            print(str(len(self.directories)) + " directories")
            self.indirectSize += sum([directory.populateIndirectSize() for directory in list(self.directories.values())])
        print(self.indirectSize)
        return self.indirectSize

    def getSignificantSize(self):
        significantSize = self.indirectSize if self.indirectSize <= 100000 else 0
        if self.directories:
            significantSize += sum([directory.getSignificantSize() for directory in list(self.directories.values())])
        return significantSize

    def visit(self, visitor):
        visitor.onCandidate(self.indirectSize)
        for directory in self.directories:
            self.directories[directory].visit(visitor)

    def __str__(self):
        return str(self.directSize) + " " + self.name

class DeleteCandidateVisitor:
    def __init__(self, threshold):
        self.threshold = threshold
        self.minimumCandidate = None

    def onCandidate(self, size):
        if size > self.threshold:
            if self.minimumCandidate:
                self.minimumCandidate = min(self.minimumCandidate, size)
            else:
                self.minimumCandidate = size

    def getDeletionSize(self):
        return self.minimumCandidate

class Day7:
    def __init__(self):
        self.lines = []
        self.rootDirectory = Directory("/", None)

    def solve(self):
        with open('a.txt') as f:
            self.lines += f.readlines()
        self.parse()
        usedSize = self.rootDirectory.populateIndirectSize()
        targetUsedSize = 70000000 - 30000000
        deleteThreshold = usedSize - targetUsedSize
        visitor = DeleteCandidateVisitor(deleteThreshold)
        self.rootDirectory.visit(visitor)
        print(visitor.getDeletionSize())

    def parse(self):
        currentDirectory = None
        for line in self.lines:
            if line.startswith('$ cd'):
                directoryName = line[5:-1]
                if directoryName == "/":
                    currentDirectory = self.rootDirectory
                elif directoryName == "..":
                    currentDirectory = currentDirectory.getParent()
                else:
                    currentDirectory = currentDirectory.getDirectory(directoryName)
            elif line.startswith('$ ls'):
                continue
            elif line.startswith('dir'):
                directoryName = line[4:-1]
                currentDirectory.addDirectory(directoryName, currentDirectory)
            else:
                file = line.strip().split(' ')
                currentDirectory.addFile(int(file[0]), file[1])

day7 = Day7()
day7.solve()

