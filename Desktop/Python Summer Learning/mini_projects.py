## Python Mini-Projects (w3resource)

## 1. Create a Python project to get the value of Pi to n number of decimal places.
# Note: Input a number and the program will generate PI to the 'nth digit
import math
# number = int(input('Please enter a number: '))
number = 3
pi = str(math.pi)
print(float(pi[:2+number]))

## 2. Create a Python project to get the value of e to n number of decimal places.
# Note: Input a number and the program will generate e to the 'nth digit
e = math.exp(1)
# num = int(input('Enter a number: '))
num = 3
print(float(str(e)[:2+num]))

## 3. Create a Python project to guess a number that has randomly selected.
import random
def guess_num(digits, guess, limit):
    end_digit = ''
    for i in range(digits): end_digit += '9'
    rand = random.randint(0, int(end_digit))
    while(guess != rand and limit > 1):
        limit -= 1
        higher_or_lower = 'lower' if (guess > rand) else 'higher'
        guess = int(input('Wrong guess! You have '+str(limit)+' chances left. Go '+higher_or_lower+'! '))
    print('Game over! The correct answer was', str(rand)) if limit == 1 else print('Yay! You got it!')
    return guess == rand

# guess_num(1, 1, 3)

## 4. Create a Python project that prints out every line of the song "99 bottles of beer on the wall."
# Note: Try to use a built in function instead of manually type all the lines.
def ninety_nine_bottles():
    START_NUM = 5
    while (START_NUM > 0):
        print(str(START_NUM)+' bottles of beer on the wall.')
        START_NUM -= 1
        print('Take one down and pass it around, '+ str(START_NUM)+' bottles of beer on the wall.')
        if START_NUM == 0: print('No more bottles of beer on the wall, no more bottles of beer.\n'+
'Go to the store and buy some more, 99 bottles of beer on the wall.')
# ninety_nine_bottles()

## A different method (provided solution)
# for i in range(99, 0, -1):
#     if(i == 2):
#         print("{} bottles of beer on the wall.\nTake one down, pass it around, {} bottle of beer on the wall".format(i, i, i-1))
#     elif(i == 1):
#         print("{} bottle of beer on the wall.\nTake one down, pass it around, no bottles of beer on the wall".format(i, i))
#     else:
#         print("{} bottles of beer on the wall.\nTake one down, pass it around, {} bottles of beer on the wall".format(i, i, i-1))

## 5. Create a Python project of a Magic 8 Ball which is a toy used for fortune-telling or seeking advice.
# Allow the user to input their question.
# Show an in progress message.
# Create 10/20 responses, and show a random response. (Imma create 5)
# Allow the user to ask another question/advice or quit the game.
import time, sys
def magic_8_ball():
    question = input('Ask me anything! ')
    bank = dict()
    responses = ["Not just no, hell no!", "Don't count on it.", "The Universe says maybe.", "I don't see why not.", "Keep doing what you're doing and it'll happen.", "Someday, but not today.", "Pretty, pretty, pretty good!"]
    for i in range(len(responses)): bank[i] = responses[i]
    stop_point = 3
    while (stop_point > 0):
        stop_point -= 1
        # random_ans = bank[random.randint(0, len(responses))]
        # this will cause a key error (happens when a key is not in the dictionary)
        # instead use randrange (takes from a to b - 1 instead of a to b)
        random_ans = bank[random.randrange(0, len(responses))]
        print(random_ans)
        onwards = input('Do you wish to continue? Please type Yes or No: ')
        if onwards.lower() == 'no' or onwards.lower() == 'n':
            print('\n\tThank you for playing Magic 8-Ball. Come again!\n')
            break
        elif onwards.lower() == 'yes' or onwards.lower() == 'y':
            question = input('Ask me something else! ')
            if stop_point == 0:
                 time.sleep(2)
                 print('\n\tCooling down! Thinking...\n')
                 stop_point = 3
            continue
        else:
            print("Please enter Y or Yes if you wish to continue; if not, type N or No")
            onwards = input('Do you wish to continue? Please type correctly this time: ')
            question = input('Ask me something else! ')

# magic_8_ball()

## 6.Create a Python project that will help to print
# colored text, bold, italic, faint, blink (slow/fast), on terminal window.
def custom_text(n,s):
	ansi_color={"bold":1,"faint":2,"italic":3,"underline":4,"blink_slow":5,"blink_fast":6,"negative":7,"conceal":8,"strike_th":9,
	"black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenda":35,"cyan":36,"white":37,
	"b_black":40,"b_red":41,"b_green":42,"b_yellow":43,"b_blue":44,"b_magenda":45,"b_cyan":46,"b_white":47,}
	try:
		num=str(ansi_color[n])
		value="\033["+num+"m"+s+"\033[0m"
        # without the "\033[0m", the terminal will change according to the most recent call of the function
		return value
	except:
		pass

print (custom_text('bold',"Python Project"))
print (custom_text('italic',"Python Project"))
print (custom_text('blink_fast',"Python Project"))
print (custom_text('green',"Python Project"))
#
# from termcolor import colored
# print(colored('Hello', 'red'), colored('World', 'blue'))

##
## NOT w3resource anymore!
##

import time
t = time.localtime()
# print(time.strftime("%d/ %m/ %Y", t))

## Create a Python project that plays the "Rock, paper, scissors" game
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
# rps()

## Create a Python project that will check to see if a number is prime
def prime_num(num):
    return_value = True
    if num <= 1: return_value = False # corner case
    for i in range(2, num):
        if (num % i == 0):
            return_value = False
            break
    print(str(num)+" is a prime number!") if return_value == True else print(str(num)+" is not a prime number :(")
# prime_num(9)
# prime_num(2)
# prime_num(1)
# prime_num(1481)
# prime_num(31)

## Create a Python program that asks the user how many Fibonnaci numbers to generate and then generates them.
def fibonnaci(num):
    if (num <= 1): return num
    return fibonnaci(num - 2) + fibonnaci(num - 1)

def fib_list(num):
    f_list = []
    for i in range(1, num+1):
        f_list.append(fibonnaci(i))
    return f_list

# print(fib_list(1))
# print(fib_list(3))
# print(fib_list(7))

## Extra: remove repetitive values in a list using sets
fib_5 = list(set(fib_list(5)))
# print(fib_5)
# print(list(set([1,1,2,4,5,7,9,7,4,3,23,4,5,6])))

## Create a Python program that generates a random password generator
# Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
import string
def password_generator(len):
    # all = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
    all = string.printable
    print(''.join(random.sample(all, len)))
# password_generator(14)
# password_generator(5)

## Provided solution on practicepython.org
# import random
#
# s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 14
# p =  "".join(random.sample(s,passlen))
# print(p)

## Decode a webpage
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://www.nytimes.com/"
html = urlopen(url, context=ctx).read().decode()
print(html)

soup = BeautifulSoup(html, "html.parser")
# print(soup('span'))
# title = soup.find('span', 'articletitle').string
# print(title)


# import requests
# from bs4 import BeautifulSoup
#
# base_url = 'http://www.cnn.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, "html.parser")
# print(soup('span'))
#
# for story_heading in soup.find_all(class_="story-heading"):
#     if story_heading.a:
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else:
#         print(story_heading.contents[0].strip())
