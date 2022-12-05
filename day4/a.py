with open('a.txt') as f:
    lines = f.readlines()
countFullyOverlappingElves = 0
for assignment in lines:
    elf1,elf2 = [x.split("-") for x in assignment.strip().split(",")]
    elf1start = int(elf1[0])
    elf1end = int(elf1[1])
    elf2start = int(elf2[0])
    elf2end = int(elf2[1])
    if elf1start >= elf2start and elf1end <= elf2end:
        countFullyOverlappingElves += 1
        continue
    if elf2start >= elf1start and elf2end <= elf1end:
        countFullyOverlappingElves += 1
print(countFullyOverlappingElves)
