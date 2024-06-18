# step 1
from logo import cipher_logo
# print(cipher_logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt your message, type 'decode' to decrypt your message: ")
message = input("Type message: ").lower()
shift_number = int(input("Enter a shift number: "))


# define a function that take two input - text and shift
def encode(text, shift_amount):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        # print(position)
        new_position = shift_amount + position
        new_letter = alphabet[new_position]
        cipher_text = cipher_text + new_letter
    print(f"Your encoded message is: {cipher_text}")


def decode(encoded_text, shift_amount):
    decode_text = ""

    for letter in encoded_text:
        # get the index of each letter
        position = alphabet.index(letter)
        # get the new position of the letter
        new_position = position - shift_amount
        new_text = alphabet[new_position]
        decode_text = decode_text + new_text
    print(f"Your decoded text is: {decode_text}")


if direction == 'encode':
    encode(text=message, shift_amount=shift_number)
elif direction == 'decode':
    decode(encoded_text=message, shift_amount=shift_number)
else:
    print("Incorrect input provided")



