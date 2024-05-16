"""
You are going to write a program that calculates the average student height
from a List of height.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together
and dividing by the total number of heights.
Important!
You should not use the sum() or len() functions in you answer.
You shoudl try to replicate their functionality using what you have
learnt about for loops.
"""

# Input a Python list of student heights
student_heights = input().split(", ")
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# Don't change the code above.

# Write you code below this row.
sumOfHeights = 0
numOfStudents = 0
for height in student_heights:
    sumOfHeights += int(height)
    # sumOfHeights += height # If I use the commented code above
    numOfStudents += 1
average_height = sumOfHeights / numOfStudents
print(f"Average height of students is {average_height}")