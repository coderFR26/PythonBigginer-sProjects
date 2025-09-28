import random

colors = ['R', 'G', 'B', 'W', 'Y']

def play():
    pallet = random.choices(colors, k=4)
    print(pallet)
    chances = 4

    while chances > 0:
        guess = [color.upper() for color in input(f'Enter a 4 colored pallet from {colors} (with spaces): ').split()]

        if guess == pallet:
            break

        chances -= 1
        if len(guess) != 4 or list(filter(lambda color: color not in colors, guess)):
            print('Invalid input, Please try again.')
            continue


        correct_position = 0
        incorrect_position = 0
        temp = pallet.copy()
        for i in range(4):
            if guess[i] == pallet[i]:
                correct_position += 1
                if guess[i] in guess[:i]:
                    incorrect_position -= 1

            elif guess[i] in temp and guess[i] in temp:
                incorrect_position += 1
                temp.remove(guess[i])

        print(f'Correct position: {correct_position} | Incorrect position: {incorrect_position}')
        print(f'You have {chances} chances left')

    return pallet, chances


playing = True
while playing:
    pallet, chances = play()
    if chances > 0:
        print('You win!')
    else:
        print(f'You lose!, the pallet was {pallet}')

    playing = input('Would you like to play again? (y/n): ').lower() == 'y'