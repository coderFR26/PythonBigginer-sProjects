import random

print('<<<Guess the number game>>>')

def guess_number():
    low = int(input('Choose a low number: '))
    high = int(input('Choose a high number: '))
    attept = 0
    while low > high:
        print('Mistake in choosing numbers')
        low = int(input('Choose a low number: '))
        high = int(input('Choose a high number: '))
    number = random.randint(low, high)
    while True:
        guess = int(input(f'Guess a number between {low} and {high}: '))
        attept += 1
        if guess == number:
            break
        elif guess < number:
            print('Too low!')
            low = guess + 1
        elif guess > number:
            print('Too high!')
            high = guess - 1
    return number, attept

number, attept = guess_number()
print(f'Congrats, You guessed the number <{number}> with {attept} attempts')

