## Create the Hangman game
## This practice question was taken from Exercise 30, 31, and 32 (practicepython.org)
## Link for the file to be used: http://norvig.com/ngrams/sowpods.txt

## Pick a random word for Exercise 30
## Bit more expanded: the helper function lets the user pick the length of the word they want to guess
import random
def pick_random_word(file, length):
    word = ''
    final_list = list()
    all = list()
    with open(file) as f:
        line = f.read().strip()
        all = line.split('\n')
        for w in all:
            if len(w) == length: final_list.append(w)
    word = random.choice(final_list)
    return word

# The 7 different drawings of the hangman game (Start to End)

STAGE = ['''
    *---*
    |   |
        |
        |
        |
        |
        =========''', '''
    *---*
    )   |
    0   |
        |
        |
        |
        =========''', '''
    *---*
    (   |
    0   |
    |   |
    |   |
        |
        =========''', '''
    *---*
    )   |
    0   |
   /|   |
    |   |
        |
        =========''', '''
    *---*
    (   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''
    *---*
    )   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''
    *---*
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''']


import string
from termcolor import colored
# install termcolor via this command: python -m pip install termcolor

def hangman():
    num = input("\nHow long would you like the word to be? ")
    ## corner cases (check if the input is a digit and greater than 1)
    if num not in string.digits: num = input("Please input a number: ")
    if int(num) <= 1: print("No words with 1 letter or fewer. Please pick a number greater than 1.")
    word = pick_random_word('sowpods.txt', int(num))

    # small test to see if the rest of the code works
    # word = 'banana' # switch it with any other word you like :)

    # the word_list provides a list of each letter in the given random word
    word_list = [char for char in word.upper()]
    # the blank_str gives you the initial state; the player has not guessed anything yet
    blank_str = ['_' for i in range(len(word_list))]

    already_guessed_words = []
    incorrect_guesses = []
    player_wins = False
    LIMIT = 6

    ## time complexity is O(n^2), which is ~okay~
    ## is there a faster way to do this???
    while (LIMIT > 0):
        # make the hangman graphic magenta (change color if you'd like)
        print(colored(STAGE[6 - LIMIT], "magenta"))
        print('%s guesses to go' % LIMIT)
        # shows the user their progress and all wrong guesses so far
        print("PROGRESS: " + " ".join(blank_str))
        print("INCORRECT GUESS: " + ", ".join(incorrect_guesses))

        guess = input('Pick a letter: ').upper()
        # this is to stop the user from typing something other than a letter
        if guess not in string.ascii_letters:
            print('Not a letter. Pick again')
        # this is to stop the user from entering an already existing letter
        if guess in already_guessed_words:
            print("\t\tYou've already guessed this letter :)")
        else:
            already_guessed_words.append(guess)
            if guess in word_list:
                # updates the correct guesses thus far
                for i in range(len(word)):
                    if word[i] == guess: blank_str[i] = guess
                # checks if the player wins before they run out of tries
                if (LIMIT >= 0 and "".join(blank_str) == word):
                    player_wins = True
                    break
            else:
                LIMIT -= 1
                incorrect_guesses.append(guess)
                print('\nWRONG GUESS!')
                continue

    print(colored(STAGE[6 - LIMIT], "magenta"))
    print("---------------------------------------------")
    if (player_wins): print("GG! You are correct, the word is %s" % word)
    else: print("GAME OVER! The final word is actually %s" % word)

def many_rounds_of_hangman():
    ct = 1
    print("-------------------------------")
    print("| Welcome! Let's play Hangman |")
    print("-------------------------------")
    end = False
    hangman()
    while not end:
        proceed = input("\nWould you like to play another round? ").lower()
        if (proceed == 'n' or proceed == 'no'):
            end = True
            break
        elif (proceed == 'y' or proceed == 'yes'):
            ct+=1
            hangman()
        else:
            print("Please enter Y or Yes to continue. If not, please type N or No.")
            continue

    if ct == 1: print("Thanks for playing %i round with me :)" % ct)
    else: print("Thanks for playing %i rounds with me :)" % ct)

# Call the function to play hangman multiple times
many_rounds_of_hangman()
