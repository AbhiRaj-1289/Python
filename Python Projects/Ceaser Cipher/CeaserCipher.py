import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Input Parameters
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26



#Encryption Function
def encrypt(or_text, shift_amount):
    cipher_text = ""
    for letter in or_text:
        if letter in alphabet:
            or_position = alphabet.index(letter)
            new_position = or_position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

#Decryption Function
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            or_position = alphabet.index(letter)
            new_position = or_position - shift_amount
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter
    print(f"The decoded text is {plain_text}")


if direction.lower() == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
