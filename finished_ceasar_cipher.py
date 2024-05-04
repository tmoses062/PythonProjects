alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   

def ceasar(text, shift, direction):
    if direction == 'decode':
        shift *= -1
    ceasar_text = ""
    for letter in text:
        if letter not in alphabets:
            not_letter = letter
            ceasar_text += not_letter
             
        else:
            position = alphabets.index(letter)
            new_position = position + shift
            if new_position <= 25:
                new_position = new_position
            else:
                new_position -= 26
                
            ceasar_letter = alphabets[new_position]
            ceasar_text += ceasar_letter

    print(f"The {direction}d text is '{ceasar_text}'")
    
from art import logo
print(logo)

go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    ceasar(text = text, shift = shift, direction = direction)

    should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if should_continue == 'no':
        go_again = False
        print('Goodbye')