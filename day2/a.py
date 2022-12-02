with open('a.txt') as f:
    lines = f.readlines()
scores = {
    "A X": 4, # Rock vs Rock
    "A Y": 8, # Rock vs Paper
    "A Z": 3, # Rock vs Scissors
    "B X": 1, # Paper vs Rock
    "B Y": 5, # Paper vs Paper
    "B Z": 9, # Paper vs Scissors
    "C X": 7, # Scissors vs Rock
    "C Y": 2, # Scissors vs Paper
    "C Z": 6, # Scissors vs Scissors
    }
score = 0
for line in lines:
    score += scores[line.strip()]
print(score)
