import random

choices = ["r", "p", "s"]
symbols = {'r': ['rock', '✊'], 'p': ['paper', '✋'], 's': ['scissors', '🖖']}

wins = 0
ties = 0
loses = 0

def winner(user, computer):
    status = 'draw'
    if user == 'r':
        if computer == 's':
            status = 'win'
        elif computer == 'p':
            status = 'lose'
    elif user == 'p':
        if computer == 's':
            status = 'lose'
        elif computer == 'r':
            status = 'win'
    elif user == 's':
        if computer == 'r':
            status = 'lose'
        elif computer == 'p':
            status = 'win'
    return status


def play():
    global wins, ties, loses, winner
    playing = True
    while playing:
        user = input('Rock, Paper, Scissors (r / p / s): ').lower()
        computer = random.choice(choices)
        print(f'''user: {symbols[user][1]}
computer: {symbols[computer][1]}''')

        winer = winner(user, computer)
        if winer == 'draw':
            print("It's a tie!")
            ties += 1
        elif winer == 'lose':
            print('You lost')
            loses += 1
        elif winer == 'win':
            print('You won!')
            wins += 1

        print(f"""Wins = {wins}
Loses = {loses}
Ties = {ties}""")
        playing = input('Do you want to play again? (y/n): ').lower()
        if playing == 'y':
            playing = True
        elif playing == 'n':
            playing = False
        else:
            playing = input('Do you want to play again? (y/n): ').lower()


play()


