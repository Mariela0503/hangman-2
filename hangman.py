import random
from words import words # download words.py 
from hangman_visual import lives_visual_dict #download hangman visuals
import string


def get_valid_word(words, min_length, max_length):
    valid_words = []
    for word in words:
        if len(word) >= min_length and len(word) <= max_length:
            valid_words.append(word)

    return random.choice(valid_words).upper()


def hangman():
    word = get_valid_word(words, 7, 8)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 7 # determine how many lives the user should have 

    while len(word_letters) > 0 and lives > 0:

        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list)) # make sure that visuals print according to user inputs

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__': # where does this come in?
    hangman()
