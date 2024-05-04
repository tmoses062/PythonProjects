import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number 1 and 100.")

def choose_difficulty():
    """Chooses difficulty. Returns attempt."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    else:
        return 5

attempts = choose_difficulty()
computer_guess = random.randint(1, 100)

guess = int(input("Make a guess: "))
while attempts != 0:
    attempts -= 1
    if guess == computer_guess:
        print(f"\nYou guessed it right. It was {computer_guess}")
        break
    elif guess > computer_guess:
        print("Too high")
    else:
        print("Too low")
    print(f"You have {attempts} guesses remaining.\n")
    if guess != computer_guess:
        guess = int(input("Guess again: "))
else:
    print("\nYou've used up your guesses, You lose.")
    print(f"The number was {computer_guess}.")