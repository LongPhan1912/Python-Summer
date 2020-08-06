## count the number of characters (character frequency) in a string.
sample = 'google.com'
ct = dict()
for char in sample:
    ct[char] = ct.get(char, 0) + 1
print(ct)

## get a string made of the first 2 and the last 2 chars from a given a string.
## If the string length is less than 2, return instead of the empty string.
ex1 = 'w3resource'
ex2 = 'w3'
ex3 = 'w'
def repeat_two(str):
    if len(str) < 2: return 'empty string'
    else: return str[:2] + str[len(str)-2:]
print(repeat_two(ex2))
print(repeat_two(ex3))

## get a string from a given string where all occurrences of its first char
## have been changed to '$', except the first char itself.
ex4 = 'restarter'
ex4 = ex4[0] + ex4[1:].replace(ex4[0],'$')
print(ex4)

## Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
## if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
str = 'The lyrics is not that poor!'
str1 = 'The lyrics is good!'
def replace_str(s):
    if 'not' in s:
        pos = s.find('not')
        rest = s[pos:]
        if 'poor' in rest: s = s[:pos] + rest.replace(s[pos:], 'good')
    elif 'good' in s:
        pos = s.find('good')
        rest = s[pos:]
        s = s[:pos] + rest.replace(s[pos:], 'poor!')
    return s
print(str1+'\n'+replace_str(str1))

## remove the nth index character from a nonempty string.
def remove_nth(str, index):
    if len(str) <= 0: return 'empty!'
    else:
        str = str[:index] + str[index+1:]
    return str
print(remove_nth('massachusetts', 2))

## Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def exchange_first_last(str):
    last = len(str) - 1
    str = str[last] + str[1:last] + str[0]
    return str
print(exchange_first_last('hannah montana'))

## Write a Python program that accepts a comma separated sequence of words
## as input and prints the unique words in sorted form (alphanumerically).
def unique_ascending(seq):
    l = seq.split(', ')
    d = dict()
    for each in l:
        d[each] = d.get(each, 0) + 1
    return ', '.join(sorted(d))
print(unique_ascending('red, white, black, red, green, black'))

## Write a Python function to create the HTML string with tags around the word(s).
def add_tags(tag, str):
    return "<%s>%s</%s>" % (tag, str, tag)
print(add_tags('i', 'Python'))

## Write a Python function to insert a string in the middle of a string.
def str_in_middle(str, mid):
    split = int(len(str) / 2)
    return str[:split] + mid + str[split:]
print(str_in_middle('{{}}', 'PHP'))
print(str_in_middle('<<>>', 'HTML'))

## Rotate left by n characters
def rotate_left_by_n(str, n):
    end = -(n + 1)
    str = str[len(str) + end:] + str[:end]
    return str
print(rotate_left_by_n('cs125', 2))

## Write a Python function to reverses a string if it's length is a multiple of 4.
def rev4(str):
    if len(str) % 4 == 0: str = str[::-1]
    return str
print(rev4('ruby'), rev4('bananarama22'))

## Write a Python program to swap cases of a given string.
def swap_cases(str):
    combine = ""
    for s in str:
        if s.isupper(): combine += s.lower()
        elif s.islower(): combine += s.upper()
        elif s == ' ': combine += s
    return combine
print(swap_cases('pYTHON eXERCISES'))
print(swap_cases('jAVA'))

## Write a Python program to print four values
## decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.
from decimal import *
def four_val(num):
    print('Decimal value:', Decimal(num))
    print('Octal value:', oct(num)[2:])
    print('Hexadecimal value:', hex(num)[2:])
    print('Binary value:', bin(num)[2:])
four_val(25)

## Write a Python program to wrap a given string into a paragraph of given width.
# sentence = input('Enter sentence: ')
# width = int(input('Enter width: ').strip())
# output = ''
# i = 0
# for word in sentence:
#     output += word
#     i += 1
#     if (i % width == 0 and i != len(sentence)): output += '\n'
# print(output)

## Write a Python program to find smallest and largest word in a given string.
def smallest_largest(str):
    maxx = max(str.split(), key=len)
    minn = min(str.split(), key=len)
    return minn, maxx
print(smallest_largest('Write a Java program to sort an array of given integers using Quick sort Algorithm.'))

## Write a Python program to display formatted text (width=50) as output.
import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
def display_w50(str):
    return textwrap.fill(str, 50)
print(display_w50(sample_text))

## Write a Python program to remove existing indentation from all of the lines in a given text.
indent_free = textwrap.dedent(sample_text)
## Write a Python program to add a prefix text to all of the lines in a string.
print(textwrap.indent(display_w50(indent_free), "> "))

## Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
import math
print('%+.2f' % math.pi)
print('%.0f' % math.pi) ## no decimal places

## Write a Python program to display a number with a comma separator.
print("{:,}".format(3005))

## Write a Python program to format a number with a percentage.
print("{:.2%}".format(0.4567))

## Write a Python program to strip a set of characters from a string.
str = 'The quick brown fox jumps over the lazy dog.'
omit = 'a,e,i,o,u'
print(''.join(char for char in str if char not in omit))

## Write a Python program to check if a string contains all letters of the alphabet.
import string
print(set(str.lower()) >= set(string.ascii_lowercase))

## Write a Python program to capitalize first and last letters of each word of a given string.
def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]

print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))

## Write a Python program to find the second most repeated word in a given string.
def second_most_rep(str):
    d = dict()
    words = str.split(' ')
    for s in words: d[s] = d.get(s, 0) + 1
    dd = sorted(d.items(), key=lambda kv : kv[1])
    return dd[-2]

print(second_most_rep("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))

## Write a Python program to print all permutations with given repetition number of characters of a given string.
from itertools import product
def permutations(str, repeats):
    lol = list(str)
    print(list(product(lol, repeat = repeats)))

permutations("abcd", 3)
