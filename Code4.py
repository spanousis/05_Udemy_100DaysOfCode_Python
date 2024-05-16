result = 0
for i in range(1, 101, 1):
    result += i
print(result)

# Add all even numbers between 1 and 1000
# e.g. 2 + 4 + .... + 998 + 1000
result = 0
for i in range(2, 1001, 2):
    result += i
print(result)

# Alternative
evenSum = 0
for i in range(1, 1001):
    if i%2 == 0: evenSum += i
print(evenSum)
