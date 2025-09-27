import random


def guess_number():
    low = int(input('Choose a low number: '))
    high = int(input('Choose a high number: '))
    attempts = 0

    while True:
        guess = random.randint(low, high)
        attempts += 1
        answer = input(f'computer guessed the number "{guess}"; is it correct, low or high? (c/l/h): ').lower()
        if answer == 'c':
            break
        elif answer == 'l':
            low = guess + 1
        elif answer == 'h':
            high = guess - 1
    return guess, attempts

number, attempts = guess_number()
print(f'>>>Computer guessed the number "{number}" with {attempts} attempts')

