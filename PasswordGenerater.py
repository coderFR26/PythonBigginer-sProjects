import string
import random

def passwordGenerator(min_length, number=True, special=True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special:
        characters += punctuation

    psw = ''
    has_number = False
    has_special = False
    meets_criteria = False
    while len(psw) < min_length or not meets_criteria:
        new_char = random.choice(characters)
        psw += new_char

        if new_char in digits:
            has_number = True
        elif new_char in punctuation:
            has_special = True

        meets_criteria = True
        if has_number:
            meets_criteria = has_number
        if has_special:
            meets_criteria = meets_criteria and has_special

    return psw

min_length = int(input('Enter minimum length of password: '))
has_number = input('Are you want your password to has numbers? (y/n): ').lower() == 'y'
has_special = input('Are you want your password to has punctuations? (y/n): ').lower() == 'y'
print(f'Your password: {passwordGenerator(min_length, has_number, has_special)}')
