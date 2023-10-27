import random

# Teaching functions and conditionals

def is_win(user, computer):
    # rock beats scissors, scissors beats paper, paper beats rock
    if (user == 'r' and computer == 's') \
        or (user == 's' and computer == 'p') \
            or (user == 'p' and computer == 'r'):
        return True
    return False

def play():
    user = input('Please choose Rock (R), Paper (P), or Scissors (S): ').lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a draw'

    if is_win(user, computer):
        return f'You won! Computer chose {computer}'
    
    return f'You lost! Computer chose {computer}'

result = play()
print(result)
