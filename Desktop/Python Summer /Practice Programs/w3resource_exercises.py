a = 'Twinkle, twinkle, little star,'
b = 'How I wonder what you are!'
c = 'Up above the world so high,'
d = 'Like a diamond in the sky.'
## tabs and new lines
# print(a + "\n\t" + b + "\n\t\t" + c + "\n\t\t" + d +"\n"+a+"\n\t"+b+"\n")

## how to print out the current time
from datetime import datetime
# print('Current date and time :'+"\n"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

import math
r = 1.1
## calculate the area of a circle
# print('Circle area is ' + str(r*r*math.pi))
## calculate the volume of a sphere
# print('Sphere volume is ', r**3 * math.pi * 4/3)

# first = input('Please enter your first name ')
# last = input('Please enter your last name ')
# print(last + ' ' + first)

## print out a list and a tuple from a string
sample = '3, 5, 7, 23'
l = sample.split(', ')
# print('List: ', l)
t = tuple(l)
# print('Tuple ', t)

## turn a string list into an int list
for i in range(len(l)):
    l[i] = int(l[i])

## compute product of a list without using a loop
from functools import reduce
pr = reduce( (lambda x, y: x*y), l )
print(pr)

sp = 'abc.java'
# print(sp[sp.find('.')+1:]) # find the text after the full-stop
# print(sp.count('a')) # count the occurence of a letter in a string

color_list = ["Red","Green","White","Black"]
## print the first and last elements of the list
# print(color_list[0], color_list[-1])

## join color_list
# print(' / '.join(color_list))

## check whether there are any uppercase letters in the first element of the color_list
print(any(char.isupper() for char in color_list[0]))

exam_st_date = (11, 12, 2014)
# print('The examination will start from :', exam_st_date[0], '/', exam_st_date[1], '/', exam_st_date[2])
# print('The examination will start from : %i/ %i/ %i'%exam_st_date)

## print the documentation of a built-in function
# print(abs.__doc__)
# print(sum.__doc__)

## shows you the calendar for a particular month
# import calendar
# y = int(input('Enter the year: '))
# m = int(input('Enter the month: '))
# try:
#     print(calendar.month(y, m))
# except:
#     print('Please enter the month again.')
#     m = int(input('Re-enter the month: '))
#     print(calendar.month(y, m))

## gives the difference between two separate days
date_one = datetime(2020, 7, 29)
date_two = datetime(2020, 8, 21)
delta = date_two - date_one
# print(delta.days, 'days')

## checks if a number is within 100 of 1000
# num = int(input('Please enter a number: '))
# print(abs(1000 - num) <= 100)

def repeat_string(str, n):
    result = ''
    for i in range(n): result += str
    return result
# print(repeat_string('na ', 8)+'batman')

def odd_or_even(numero):
    if (numero % 2 != 0): return 'odd'
    else: return 'even'
# print('The number you entered is:', odd_or_even(7))

def repeat_first_two(str, n):
    result = ''
    for i in range(n):
        if len(str) < 4: result += str + ' '
        else: result += str[:4] + ' '
    return result
# print(repeat_first_two('pikachu', 3))

def vowel_or_not(str):
    vowels = 'aeiou'
    return str in vowels
# print(vowel_or_not('c'), vowel_or_not('a'))

def contains_vowel(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in vowels: return v in str
# print(contains_vowel('cat'), contains_vowel('nllptr'))

## creates histogram from list of integers
def histogram(items):
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times -= 1
        print(output)
##########
# histogram([2, 3, 5, 7])

## print all even numbers that comes before the number 237 appears; print 237 too;
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
def even_in_order(items):
    l = list()
    for n in items:
        if n == 237:
            l.append(n)
            break
        elif n % 2 == 0: l.append(n)
    return l
# print(even_in_order(numbers))

## print the items that appear in the first list, but not the second
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
lil = list()
for item in color_list_1:
    if item not in color_list_2: lil.append(item)

# print('This prints a list:', lil)
# print('This prints a set:', color_list_1.difference(color_list_2))

## finds the distance between two coordinates
pos1 = (1, 2)
pos2 = (3, 4)
# print(math.sqrt( (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) )

def gcd(a, b):
    num = 1
    for i in range(1, a+1):
        if (b % i == 0.0): num = i
    return num
# print(gcd(27, 9))

def lcm(a, b):
    # min = b if (a > b) else a
    # max = b if (a <= b) else a
    minimum = min(a, b)
    maximum = max(a, b)
    for i in (1, minimum):
        product = i * maximum
        if (product % a == 0 and product % b == 0): break
    return product
# print(lcm(7, 4))

def sum_if_int(a, b):
    if not (isinstance(a, int) and isinstance(b, int)): raise TypeError("Must be an integer.")
    return a + b
# print(sum_if_int(4, 5.0))
# print(sum_if_int(4, 5))

def max_n_min(numero_list):
    maxx = max(numero_list)
    minn = min(numero_list)
    return maxx, minn
# print(max_n_min([0,9,4,5,32,56,44,78,2,1,3]))

## sum the cubed product of all integers before the input number
def sum_of_cubes(n):
    sum = 0
    for i in range(n): sum += i**3
    return sum
# print(sum_of_cubes(8))

def odd_product(r):
    odd_list = list()
    for i in range(len(r)):
        for j in range(len(r)):
            if (i != j) and (i*j % 2 != 0) and (i*j not in odd_list): odd_list.append(i*j)
    return odd_list
# print(odd_product([2, 4, 6, 3, 5, 1]))

def empty_variable(var):
    print('emptied', type(var)())

num = 20
dict = {"x":200}
list = [1,3,5]
tuple = (5,7,8)
empty_variable(list)


#### cool features ####

## sees if a file exists
import os.path
open('hello.py', 'w')
# print('Does this file exist?', os.path.isfile('hello.py'))

## determine if a Python shell is executing in 32bit or 64bit mode on OS.
import struct
# print(struct.calcsize("P") * 8)
# For 32 bit it will return 32 and for 64 bit it will return 64

## get OS name, platform and release information.
import platform
import os
# print('OS name:',os.name)
# print('Platform:',platform.system())
# print('Release info:',platform.release())

## get the size of a file
print('The size of the file is',os.path.getsize('intro-short.txt'),'bytes')

## locate Python site-packages.
import site;
# print(site.getsitepackages())

## get the path and name of the file that is currently executing.
import os
# print("Current File Name:",os.path.realpath(__file__))

## find out the number of CPUs using.
import multiprocessing
# print(multiprocessing.cpu_count())

## determine profiling of Python programs.
## A profile is a set of statistics that describes how often
## and for how long various parts of the program executed.
## These statistics can be formatted into reports via the pstats module.
import cProfile
def sum_profile():
    print(1+2)
# cProfile.run('sum_profile()')

## get an absolute file path
def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')
# print("Absolute file path: ",absolute_file_path("test.txt"))

## get file creation and modification date/times.
import os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("w3resource_exercises.py")))
# print("Created: %s" % time.ctime(os.path.getctime("w3resource_exercises.py")))

## get copyright information
import sys
# print("\nPython Copyright Information")
# print(sys.copyright)
# print()

## get the size of an object in bytes
aa = 'hello'
ab = ', '
bb = 'world'
bc = '0'
cc = '1'
# print('aa:',sys.getsizeof(aa),'ab:',sys.getsizeof(ab),'bb:',sys.getsizeof(aa),'\n')
# print('bc:',sys.getsizeof(bc),'cc:',sys.getsizeof(cc))

## get the ASCII value of a character
# print(ord('A'))

## clear the terminal
# os.system('clear')
