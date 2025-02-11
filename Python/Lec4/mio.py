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

def get_letter(message = "Enter a single letter: "):
   #loop until we get a single letter
   while True:
       char = input(message).strip()
       if len(char) == 1 and char.isalpha():
           return char
       print("Invalid input, please try again")

def my_sum(*numbers):
    return sum(numbers)

def my_min(*numbers):
    return min(numbers)

def my_max(*numbers):
    return max(numbers)

def max_diff(*numbers):
    return max(numbers) - min(numbers)


def get_number_recursive(message = "Enter a number: "):
   try:
       num = int(input(message))
       return num
   except ValueError:
       print("Invalid input.")
       return get_number_recursive(message)


def get_decimal(message = "Enter a decimal number: "):
    while True:
       try:
            num = float(input(message))
            return num
       except ValueError:
            print("Invalid input.")
    
def get_number(message = None, start = 1, end = 4):
    if message is None:
        message = f"Enter a number between {start} and {end}: "
    while True:
        try:
            num = int(input(message))
            if start <= num <= end:
                return num
            else:
                print(f"Number must be between {start} and {end}")
        except ValueError:
            print("Invalid input")
 




students = {
    'Elsa': [90, 85, 95],
    'Anna': [70, 75, 80],
    'Olaf': [100, 100, 100]
}



