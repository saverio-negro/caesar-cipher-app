# **** Caesar Cipher App ****

from art import logo
import os

def is_linux():
    return os.name == "posix"

def clear():
    os.system("clear") if is_linux() else os.system("cls")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
           end_text += char     
        
    print(f"The {cipher_direction}d text is: {end_text}")

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start_program():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    keep_going = input('Type "yes" if you want to go again. Otherwise, type "no" to exit the program: ')
    if keep_going == "yes":
        clear()
        start_program()
    else:
        clear()
        print("Goodbye.")

start_program()