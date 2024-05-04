import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '<', '>', '|']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))

password = []
for num in range(0, nr_letters):
    info = letters[random.randint(0, len(letters) - 1)]
    password.append(info)
    
for num in range(0, nr_symbols):
    info = symbols[random.randint(0, len(symbols) - 1)]
    password.append(info)

for num in range(0, nr_numbers):
    info = numbers[random.randint(0, len(numbers) - 1)]
    password.append(info)

print('Your password is: ', end = '')

str_password = ""
for item in password:
    str_password += item

print(str_password)