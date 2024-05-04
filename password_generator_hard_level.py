import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '.', '+', ',']

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

# print(password)

hard_password = []
for num in range(0, len(password)):
    info1 = password[random.randint(0, len(password) - 1)]
    hard_password.append(info1)
    password.remove(info1)
# print(hard_password)

print('Your password is: ', end = '')
for item in hard_password:
    print(item, end = '')
