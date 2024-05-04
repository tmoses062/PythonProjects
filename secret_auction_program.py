from art import logo2
print(logo2)

print("Welcome to the secret auction program")

bidders = {}

new_bidder = True
while new_bidder:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == 'no':
        new_bidder = False

highest_bid = 0
highest_bidder = ""
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        highest_bidder = bidder
print(f"The highest bidder is {highest_bidder.title()} with a bid of ${highest_bid}")
