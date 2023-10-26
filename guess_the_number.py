'''
Simple Python program to demonstrate the use numbers, loops and conditions
'''

import random

def guess(number):

    random_number = random.randint(1, number)
    
    guess = 0

    while guess != random_number:
        
        guess = int(input(f'Enter a number between 1 and {number}: '))

        if guess < random_number:
            print('Guess again, too low!')
        elif guess > random_number:
            print('Guess again, too high')
    
    print(f'Well done! You guessed the correct number, which was {random_number}.')

guess(100)
