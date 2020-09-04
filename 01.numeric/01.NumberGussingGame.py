'''
For this exercise
~~~~~~~~~~~~~~~~~
1. Write a function (guessing_game) that takes no arguments.
2. When run, the function chooses a random integer between 10 and 20 (inclusive).
3. Then ask the user to guess what number has been chosen.
4. Each time the user enters a guess, the program indicates one of the following:
    - Too high
    - Too low
    - Just right
5. If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
6. The program only exits after the user guesses correctly.
'''

import random


def guessing_name() -> None:
    '''
    guess number program
    '''
    number = random.randint(10,20)
    while True:
        guess = int(input('Guess a number between 10-20 (inclusive) : '))
        if guess == number:
            print('Awesome')
            break
        elif number < guess:
            print(f'Number less than {guess}')
        else:
            print(f'Number greater than {guess}')


guessing_name()
