import random
from game_data import data

list_drawn = []         # Created a empty list for appending two dictionaries to be compared
def list_drawing(account):
    """List drawn for comparison"""
    list_drawn.append(account)

def display_data(account):
    """Displays data to be compared"""
    return f"{account['name']}, a {account['description']} from {account['country']}"

score = 0
def comparison(list, answer, score):
    """Compares the number of followers"""
    dict = {}
    for data in list:
        index = list.index(data)
        if index == 0:
            person = 'A'
        else:
            person = 'B'
        
        dict[person]= list[index]['follower_count']

    highest = 0
    for followers_count in dict:
        if dict[followers_count] > highest:
            highest = dict[followers_count]
    
    if dict[answer] == highest:
        score += 1
        return score
    else:
        final_score = score
        return [1000, final_score]

account_a = random.choice(data)
account_b = random.choice(data)
if account_b == account_a:
    account_b = random.choice(data)
list_drawing(account_a)
list_drawing(account_b)

game_continues = True
while game_continues:
    print(f"Compare A: {display_data(account_a)}")
    print('\nVS\n')
    print(f"Against B: {display_data(account_b)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    score = comparison(list_drawn, answer, score)
    if type(score) == list:
        print(f"Sorry, you're wrong. Final_score: {score[1]}")
        game_continues = False
    else:
        del(list_drawn[0])
        account_a = list_drawn[0]
        account_b = random.choice(data)
        if account_b == account_a:
            account_b = random.choice(data)
        list_drawing(account_b)
        print(f"You're right! Current score: {score}\n")
