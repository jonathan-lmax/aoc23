with open('a.txt') as f:
    lines = f.readlines()
scores = {
    "A X": 3, # Rock vs Scissors
    "A Y": 4, # Rock vs Rock
    "A Z": 8, # Rock vs Paper
    "B X": 1, # Paper vs Rock
    "B Y": 5, # Paper vs Paper
    "B Z": 9, # Paper vs Scissors
    "C X": 2, # Scissors vs Paper
    "C Y": 6, # Scissors vs Scissors
    "C Z": 7, # Scissors vs Rock
    }
score = 0
for line in lines:
    score += scores[line.strip()]
print(score)
