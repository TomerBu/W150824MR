from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
punctuation = '#$%+*'


# Get user input
length = int(input('Enter the length of the password: '))

include_lower = input('Include lowercase letters? (y/n): ').lower() == 'y'
include_upper = input('Include uppercase letters? (y/n): ').lower() == 'y'
include_digits = input('Include digits? (y/n): ').lower() == 'y'
include_punctuation = input('Include punctuation? (y/n): ').lower() == 'y'

# all the letters for the password
letters = ''
password = ''

# add user choice to the letters list
if include_lower:
    letters += ascii_lowercase #letters = 'abcdefghijklmnopqrstuvwxyz'
if include_upper:
    letters += ascii_uppercase #letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
if include_digits:
    letters += digits #letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
if include_punctuation:
    letters += punctuation #letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%+*'

for _ in range(length):
    password += choice(letters)

print(password)