number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")

if number % 3 == 0:
    print("It is divisible by 3")
else:
    print("It is not divisible by 3")

print("Welcome to the roller coaster!")
height = int(input("Enter your height in cm: "))

# if height >= 120:
#     print("You can purchase the ticket for the ride!")
#     photo = input("Do you want a photo? 'Yes' or 'No': ")
#     age = int(input("Enter you age? "))
#     if photo == 'Yes' or 'yes' or 'YES':
#         if age < 12:
#             print("Your ticket fee is $8.")
#         elif 12 <= age < 18:
#             print("Your ticket fee is $10.")
#         else:
#             print("Your ticket fee is $15.")
#     else:
#         if age < 12:
#             print("Your ticket fee is $5.")
#         elif 12 <= age < 18:
#             print("Your ticket fee is $7.")
#         else:
#             print("Your ticket fee is $12.")
# else:
#     print("Sorry, you can't ride the roller coaster.")
bill = 0
if height >= 120:
    print("You can purchase the ticket for the ride!")
    age = int(input("Enter you age? "))

    if age < 12:
        bill = 5
        print("Your ticket fee is $5.")
    elif 12 <= age < 18:
        bill = 7
        print("Your ticket fee is $7.")
    elif 45 <= age <= 55:
        print("You can join us, it's a free ride.")
    else:
        bill = 12
        print("Your ticket fee is $12.")

    photo = input("Do you want a photo? 'Y' or 'N': ")
    if photo == 'Y':
        bill += 3

        print(f"Your total bill is ${bill}")
else:
    print("Sorry, you can't ride the roller coaster.")
