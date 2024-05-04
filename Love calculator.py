print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your lover's name? \n")

name = name1 + name2
lowercase = name.lower()

TRUE = lowercase.count('t') + lowercase.count('r') + lowercase.count('u') + lowercase.count('e')

LOVE = lowercase.count('l') + lowercase.count('o') + lowercase.count('v') + lowercase.count('e')

love_score = int(str(TRUE) + str(LOVE))

if 40 <= love_score <= 50:
    print(f"Your score is {love_score}%, you are alright together.")
elif (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}%, you go together like coke and mentos.")
else:
    print(f"Your score is {love_score}%.")
