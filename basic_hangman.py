import random
import string

# basic version of hangman. no concept of scores or validation of the word
# uses the useful word list found with keepassxc

def get_word():
    with open('/usr/share/keepassxc/wordlists/eff_large.wordlist') as f:
        lines = []
        lines = f.read().splitlines()
        word = random.choice(lines)
    return str(word).upper()

word = get_word()
letters = set(word)
alphabet = set(string.ascii_uppercase)
used_letters = set()

while len(letters) > 0:
    print('Used letters: ', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '*' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_guess = input('Guess a letter: ').upper()
    if user_guess in alphabet - used_letters:
        used_letters.add(user_guess)
        if user_guess in letters:
            letters.remove(user_guess)

    elif user_guess in used_letters:
        print('You\'ve already guessed that letter, try another.')

    else:
        print('Invalid character, try again.')

print(f'Well done, you guessed the word, which was {word}, and you guessed the following letters: {used_letters}')
