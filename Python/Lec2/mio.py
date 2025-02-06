from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice

def random_lower():
    return choice(ascii_lowercase)

def random_upper():
    return choice(ascii_uppercase)

def random_digit():
    return choice(digits)

def random_punctuation():
    return choice(punctuation)



# def input_a_single_letter():
#     char = input("Enter a single letter: ").strip()
#     is_valid = len(char) == 1 

#     while not is_valid:
#         char = input("Enter a single letter: ").strip()
#         is_valid = len(char) == 1

#     return char

def get_letter(message = "Enter a single letter: "):
   #loop until we get a single letter
   while True:
       char = input(message).strip()
       if len(char) == 1 and char.isalpha():
           return char
       print("Invalid input, please try again")

letter = get_letter("enter your guess:")
print(letter)