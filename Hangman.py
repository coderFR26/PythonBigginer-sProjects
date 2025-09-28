import random

words = ['scientist', 'computer', 'engineer', 'teacher', 'backpack', 'rainbow']

def pick_word():
    word = random.choice(words)
    return word

def hint(word):
    word_holder = ['_'] * len(word)
    return word_holder

def show_hangman(mistak_number):
    hangman = {0: ('+----+   \n'
                   '|        \n'
                   '|        \n'
                   '|        \n'
                   '|___  '),
               1: ('+----+   \n'
                   '|    o   \n'
                   '|        \n'
                   '|        \n'
                   '|___  '),
               2: ('+----+   \n'
                   '|    o   \n'
                   '|    |   \n'
                   '|        \n'
                   '|___  '),
               3: ('+----+   \n'
                   '|    o   \n'
                   '|   /|   \n'
                   '|        \n'
                   '|___  '),
               4: ('+----+   \n'
                   '|    o   \n'
                   '|   /|\\ \n'
                   '|        \n'
                   '|___  '),
               5: ('+----+   \n'
                   '|    o   \n'
                   '|   /|\\ \n'
                   '|   /    \n'
                   '|___  '),
               6: ('+----+   \n'
                   '|    o   \n'
                   '|   /|\\ \n'
                   '|   / \\ \n'
                   '|___  ')}
    print(hangman[mistak_number])

print('>>>>>>Welcome to Hangman Game<<<<<<')
def main():
    word = pick_word()
    word_holder = hint(word)
    print(word_holder)
    mistakes = 0

    while mistakes < 6 and '_' in word_holder:
        guess = input('Guess a letter: ')
        if guess == word_holder:
            break

        if guess in word:
            print('Right!')
            for i in range(len(word)):
                if word[i] == guess:
                    word_holder[i] = guess

        elif guess not in word:
            print('Wrong!')
            mistakes += 1

        print(word_holder)
        print(f'you have {6 - mistakes} chances left.')

    if mistakes == 6:
        print('You lost!')
    else:
        print('You won!')
    show_hangman(mistakes)


if __name__ == '__main__':
    next = True
    while next:
        main()
        next = input('Do you want to play again? (y/n): ').lower() == 'y'
