#######################################
## Python Mini-Projects (w3resource) ##
#######################################

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
# Call the function:
# guess_num(1, 1, 3)

## 4. Create a Python project that prints out every line of the song "99 bottles of beer on the wall."
# Note: Try to use a built in function instead of manually type all the lines.
def ninety_nine_bottles():
    START_NUM = 5 # change to 99 if you want
    while (START_NUM > 0):
        print(str(START_NUM)+' bottles of beer on the wall.')
        START_NUM -= 1
        print('Take one down and pass it around, '+ str(START_NUM)+' bottles of beer on the wall.')
        if START_NUM == 0: print('No more bottles of beer on the wall, no more bottles of beer.\n'+
'Go to the store and buy some more, 99 bottles of beer on the wall.')
# ninety_nine_bottles()

## A different method (provided solution on w3resource)
# for i in range(99, 0, -1):
#     if(i == 2):
#         print("{} bottles of beer on the wall.\nTake one down, pass it around, {} bottle of beer on the wall".format(i, i, i-1))
#     elif(i == 1):
#         print("{} bottle of beer on the wall.\nTake one down, pass it around, no bottles of beer on the wall".format(i, i))
#     else:
#         print("{} bottles of beer on the wall.\nTake one down, pass it around, {} bottles of beer on the wall".format(i, i, i-1))
