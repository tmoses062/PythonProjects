import random

rock = '''
    ________
---'    ____)
       (_____)
       (_____)
       (____)
---.___(___)
'''
paper = '''
    _______
---'   ____)___
          _____)
          ______)
         ______)
---._________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
       (____)
---.___(___)
'''


choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
option = [rock, paper, scissors]
print(option[choice])

computerschoice = random.randint(0, 2)

print('Computer chose:\n')
print(option[computerschoice])

if choice == 0:
    if computerschoice == 0:
        print('A draw')
    elif computerschoice == 1:
        print('You lose')
    elif computerschoice == 2:
        print('You won')
elif choice == 1:
    if computerschoice == 0:
        print('You won')
    elif computerschoice == 1:
        print('A draw')
    elif computerschoice == 2:
        print('You lose')
elif choice == 2:
    if computerschoice == 0:
        print('You lose')
    elif computerschoice == 1:
        print('You won')
    elif computerschoice == 2:
        print('A draw')
        
