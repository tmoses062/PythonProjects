import random
from game_data import data

list_drawn = []         # Created a empty list for appending two dictionaries to be compared
def list_drawing():
    """List drawn for comparison"""
    list_drawn.append(random.choice(data))

def display_data():
    """Displays daa to be compared"""
    for data in list_drawn:
        index = list_drawn.index(data)
        if index == 0:
            person = 'A'
            value = 'Compare'
        else:
            person = 'B'
            value = 'Against'
        print(f"{value} {person}: {list_drawn[index]['name'], list_drawn[index]['description'], list_drawn[index]['country']}\n")

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

for num in range(2):
    list_drawing()

game_continues = True
while game_continues:
    display_data()
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    score = comparison(list_drawn, answer, score)
    if type(score) == list:
        print(f"Sorry, you're wrong. Final_score: {score[1]}")
        game_continues = False
    else:
        del(list_drawn[0])
        list_drawing()
        print(f"You're right! Current score: {score}\n")
