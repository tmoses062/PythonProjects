from art import logo
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))   


def ceasar(text, shift, direction):
    if direction == 'decode':
        shift *= -1
    ceasar_text = ""
    for letter in text:
        position = alphabets.index(letter)
        new_position = position + shift
        if new_position <= 26:
                new_position = new_position
        else:
                new_position -= 26
                
        ceasar_letter = alphabets[new_position]
        ceasar_text += ceasar_letter

    print(f"The {direction}d text is '{ceasar_text}'")

    
ceasar(text = text, shift = shift, direction = direction)