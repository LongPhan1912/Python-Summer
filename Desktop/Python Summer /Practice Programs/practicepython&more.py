#######################################################
## A mix of practicepython.org and personal programs ##
#######################################################

import time
t = time.localtime()
print(time.strftime("%d/ %m/ %Y", t))

## Create a Python project that plays the "Rock, Paper, Scissors" game
## This practice question is from Exercise 8 (practicepython.org)
import random
def rps():
    choices = ['rock', 'paper', 'scissors']
    LIMIT = 3
    ct = 0
    wins = 0
    while (LIMIT > 0):
        LIMIT -= 1
        ct += 1
        comp_choice = random.choice(choices)
        user_choice = input('Rock, paper, scissors, go! Enter your choice: ').lower()

        if user_choice in choices:
            wins += rps_result(user_choice, comp_choice)
        else:
            print('Wrong input. Please enter again!')
            user_choice = input('Rock, paper, scissors, go! Enter your choice: ').lower()
            wins += rps_result(user_choice, comp_choice)

        print(str(LIMIT)+' chances left.')
        prompt = input('Try again? Yes or No ').lower()
        if (prompt == 'y' or prompt == 'yes'): continue
        elif (prompt == 'n' or prompt == 'no' or LIMIT == 0):
            print('Thanks for playing! You have won '+str(wins)+' times out of '+str(ct)+' times')
            break

def rps_result(user_choice, comp_choice):
    a = 0
    if user_choice == comp_choice: print("It's a tie")
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'scissors' and comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'rock'):
        print('You win!')
        a+=1
    else: print('You lose!')
    return a

# Run the function:
rps()

## This is a personal program, not from practicepython.org
## By using a dictionary, the function returns the list of indices
## where the character entered can be found.
## Read about appending a dict with a list as its values here:
## https://stackoverflow.com/questions/17755996/python-list-as-default-value-for-dictionary
def word_appearances(char, word):
    word_dict = dict()
    word = word.upper()
    each_letter = [c for c in word]
    for i in range(len(each_letter)):
        key = each_letter[i]
        word_dict.setdefault(key, []).append(i)
    return word_dict[char]

# Test:
word_appearances('a', 'banana')

## Create a Python project that will check to see if a number is prime
def prime_num(num):
    return_value = True
    if num <= 1: return_value = False # corner case
    for i in range(2, num):
        if (num % i == 0):
            return_value = False
            break
    print(str(num)+" is a prime number!") if return_value else print(str(num)+" is not a prime number :(")

## Tests:
prime_num(9)
prime_num(2)
prime_num(1)
prime_num(1481)
prime_num(31)

## Create a Python program that asks the user how many Fibonnaci numbers to generate and then generates them.
## This practice question is from Exercise 13 (practicepython.org)
def fibonnaci(num):
    if (num <= 1): return num
    return fibonnaci(num - 2) + fibonnaci(num - 1)

def fib_list(num):
    f_list = []
    for i in range(1, num+1):
        f_list.append(fibonnaci(i))
    return f_list

# Tests:
# print(fib_list(1))
# print(fib_list(3))
# print(fib_list(7))

## Extra: remove repetitive values in a list using sets
fib_5 = list(set(fib_list(5)))
# Tests:
# print(fib_5)
# print(list(set([1,1,2,4,5,7,9,7,4,3,23,4,5,6])))

## Create a Python program that generates a random password generator
# Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
import string
def password_generator(len):
    # all = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
    all = string.printable
    print(''.join(random.sample(all, len)))

# Run the function:
password_generator(14)
password_generator(5)

## Suggested solution from practicepython.org
# import random
# s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 14
# p =  "".join(random.sample(s,passlen))
# print(p)

## Create a Python program that creates a list of overlapping numbers between two txt files
## This practice question is from Exercise 23 (practicepython.org)
## The first file is a list of prime numbers: http://www.practicepython.org/assets/primenumbers.txt
## The second is a list of happy numbers: http://www.practicepython.org/assets/happynumbers.txt
def lines_to_list(file):
    list = []
    with open(file) as f:
        line = f.readline()
        while line:
            list.append(int(line))
            line = f.readline()
    return list

def overlap_files(f1, f2):
    prime_list = lines_to_list(f1)
    happy_list = lines_to_list(f2)

    overlap = []
    for x in prime_list:
        if x in happy_list: overlap.append(x)
    print(overlap)

# Run the function:
overlap_files('primenumbers.txt', 'happynumbers.txt')
