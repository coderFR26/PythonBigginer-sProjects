import random

def spin():
    symbols = ['🍒', '🎃', '🔔', '💵', '🥎']
    choices = random.choices(symbols, k=3)
    return choices

def get_pay(rows):
    prizes = {'🍒': 3, '🎃': 5, '🔔': 10, '💵': 20, '🥎': 7}
    pay = 0
    if rows[0] == rows[1] == rows[2]:
        pay = prizes[rows[0]] * 3
    return pay


def main():
    balance = 100
    while True:
        bet = int(input('How much money would you like to bet? '))
        if bet > balance or bet <= 0:
            print('Please enter a valid number.')
        balance -= bet
        print('Spinning...\n')

        rows = spin()
        print(rows, sep=' | ')
        pay = get_pay(rows)

        if pay > 0:
            print(f'You won ${pay}!!!')
        balance += pay
        print(f'Your balance is ${balance}')

        play_again = input('Would you like to play again? (y/n) ')
        if play_again == 'y':
            continue
        else:
            print('Thank you for playing!')
            break

print('***********************************')
print('Welcome to Python SlotMachine')
print(f'Symbols are: 🍒, 🎃, 🔔, 💵, 🥎')
print('***********************************')

if __name__ == '__main__':
    main()