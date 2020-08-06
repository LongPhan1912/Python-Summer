# add all numbers in the file(s) together through regular expressions
import re

#text = open('regex_sum_42.txt') #gives 445833
text = open('regex_sum_773678.txt') #gives 357810

sum = 0
for line in text:
    line = line.rstrip()
    num_list = re.findall('[0-9]+', line)
    for num in num_list:
        sum += int(num)

print(sum)
