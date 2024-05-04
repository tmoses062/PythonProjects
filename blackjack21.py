import random
from art import logo4
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    start_game = True
    while start_game:
        users_card = []
        dealers_card = []
        ans = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if ans == 'n':
            start_game = False
        else:
            def user():
                """This draws two cards for the user."""
                print(logo4)
                for num in range(2):
                    user_random = random.choice(cards)
                    users_card.append(user_random)
                total_user_card = 0
                for num in users_card:
                    total_user_card += num
                print(f"Your cards: {users_card}")
                print(f"Your current score is {total_user_card}")
                return total_user_card

            def dealer():
                """This draws two cards for the computer."""
                for num in range(2):
                    dealer_random = random.choice(cards)
                    dealers_card.append(dealer_random)
                popped_card = dealers_card.pop()
                print(f"Computer's first card: {dealers_card[0]}")
                dealers_card.append(popped_card)
                total_dealer_card = dealers_card[0] + popped_card
                return total_dealer_card
            
            first_total = user()
            second_total = dealer()

            def another_card(whomever, card_list):
                """This allows another card to be drawn by both parties."""
                user_random = random.choice(cards)
                if user_random == 11:
                    third_total = whomever + user_random
                    card_list.append(user_random)
                    if third_total > 21:
                        third_total -= 11
                        third_total += 1
                        card_list.pop()
                        user_random = 1
                        card_list.append(user_random)
                else:
                    third_total = whomever + user_random
                    card_list.append(user_random)
                return third_total
                
            def compare(one, two, card1, card2):
                """This compares the user's score with the computer's score."""
                if two > 21:
                    if one < 21:
                        print(f"\nYour card list: {card1}, Current score: {one}\nComputer's card list: {card2}, Computer's score: {two}\nYou won.\n")
                    elif one == 21:
                        print(f"\nYour card list: {card1}, Current score: {one}\nComputer's card list: {card2}, Computer's score: {two}\nYou won.\n")
                elif one > 21:
                    print(f"\nYour card list: {card1}, Current score: {one}\nComputer's card list: {card2}, Computer's score: {two}\nYou lose.\n")
                elif two > one:
                    print(f"\nYour card list: {card1}, Current score: {one}\nComputer's card list: {card2}, Computer's score: {two}\nYou lose.\n")
                elif one == two:
                    print(f"\nYour card list: {card1}, Current score: {one}\nComputer's card list: {card2}, Computer's score: {two}\nIt's a draw.\n")
                else:
                    print(f"\nYour card list: {card1}, Current score: {one}\nComputer's card list: {card2}, Computer's score: {two}\nYou won.\n")
            beginning = True
            while beginning:
                if second_total == 21:
                    compare(first_total, second_total, users_card, dealers_card)
                    beginning = False
                elif first_total > 21:
                    compare(first_total, second_total, users_card, dealers_card)
                    beginning = False
                elif first_total == 21:
                    compare(first_total, second_total, users_card, dealers_card)
                    beginning = False
                elif first_total < 21:        
                    continue_drawing = True
                    while continue_drawing:        
                        draw_another = input("Do you want to draw another card? Type 'y' or 'n': ")
                        if draw_another == 'y':
                            total_card = another_card(first_total, users_card)
                            first_total = total_card
                            print(f"\nYour current card list: {users_card}, Current score: {first_total}")
                            if first_total > 21:
                                if second_total < 17:
                                    fourth_total = another_card(second_total, dealers_card)
                                    second_total = fourth_total
                                compare(first_total, second_total, users_card, dealers_card)
                                beginning = False
                            if first_total < 21:
                                if second_total < 17:
                                    fourth_total = another_card(second_total, dealers_card)
                                    second_total = fourth_total
                                continue_drawing = False
                            
                            continue_drawing = False
                        else:
                            compare(first_total, second_total, users_card, dealers_card)
                            continue_drawing = False
                            beginning = False
            
    start_again = input("\nType 'n' to start a new game of blackjack or 'e' to exit the game: ")
    if start_again == 'n':
        blackjack()
    else:
        start_game = False
blackjack()