import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for l in range(1, nr_letters+1):
    password += letters[random.randint(0, len(letters)-1)]
for n in range(1, nr_symbols+1):
    password += symbols[random.randint(0, len(symbols)-1)]
for s in range(1, nr_numbers+1):
    password += numbers[random.randint(0, len(numbers)-1)]
print(password)

# Hard Level - Order of chanracters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwordList = []
for i in password:
    passwordList.append(i)

hardPassword = ""
for i in range (0, len(password)):
    rnNumber = random.randint(0, len(passwordList)-1)
    hardPassword += passwordList[rnNumber]
    passwordList.remove(passwordList[rnNumber])
print(hardPassword)