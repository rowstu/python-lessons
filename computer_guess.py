import random

# another number guessing game

def guess(number):
    low = 1
    high = number
    answer = ''

    while answer != 'c':
        guess = random.randint(low, high)
        print(f'Think of a number between {low} and {high} and then answer my questions with either L, H or C')
        print('')
        answer = input(f'''Is {guess} lower(L) or higher(H) than your number, 
        or is it a correct (C) guess? ''').lower()

        if answer == 'h':
            high = guess - 1
        elif answer == 'l':
            low = guess + 1

    print(f'I guessed your number was {guess}')


guess(100)
