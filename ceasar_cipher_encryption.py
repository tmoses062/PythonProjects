alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        position = alphabets.index(letter)
        new_position = position + shift
        if new_position <= 26:
            encrypted_letter = alphabets[new_position]
            encrypted_text += encrypted_letter
        else:
            new_position -= 26
            encrypted_letter = alphabets[new_position]
            encrypted_text += encrypted_letter
    print(f"The encoded text is {encrypted_text}")
    
encrypt(text = text, shift = shift)