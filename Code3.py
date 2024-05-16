"""
You are goint to write a program that calculates the highest score
from a List of scores.
Important!
Your are not allowed to use the max or min functions.
The output words must match the example.
print(f"The highest score in the class is: {highestScore})
78 65 89 86 55 91 64 89
"""

# Input a list of student scores
student_scores = input().split()
# Write your code below this row
print(student_scores)
highestScore = 0
for score in student_scores:
    if highestScore < int(score):
        highestScore = int(score)

print(f"The highest score in the class is: {highestScore}")