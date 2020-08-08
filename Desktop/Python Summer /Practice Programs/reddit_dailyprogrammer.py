# ------------------------------------------------------------------
## Challenge #379: [Easy] Progressive taxation
# Link: https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

# The income tax brackets of the nation of Examplia:
# income cap      marginal tax rate
#   ¤10,000           0.00 (0%)
#   ¤30,000           0.10 (10%)
#  ¤100,000           0.25 (25%)
#     --              0.40 (40%)

tax_brackets = {100000 : 0.4,
                30000 : 0.25,
                10000 : 0.1}

def tax(income):
    total_tax = 0
    for cap, rate in tax_brackets.items():
        if income >= cap:
            deductible = income - cap
            total_tax += deductible * rate
            income -= deductible
    return int(total_tax)

# print(tax(56789)) # => 8697
# print(tax(1234567)) # => 473326

def max_tax(index):
    max_tax = 0
    rev = list(tax_brackets.items())
    if index < len(rev):
        max = rev[index][0]
        min = rev[index + 1][0]
        rate = rev[index + 1][1]
        max_tax = (max - min) * rate
    return max_tax
print(max_tax(1))

# total_tax = income * tax_rate
# def get_income(tax_rate):
#
# print(get_income(0.06) == 25000)
# print(get_income(0.09) == 34375)
# print(get_income(0.32) == 256250)

# ------------------------------------------------------------------
## Challenge #381: [Easy] Yahtzee Upper Section Scoring
# Link: https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

def yahtzee_upper(sorted_int_list):
    d = dict()
    max_result = 0
    for key in sorted_int_list:
        d[key] = d.get(key, 0) + 1
        value = d[key]
        if max_result < key * value: max_result = key * value
    print(max_result)

# Run the program:
# yahtzee_upper([2, 3, 5, 5, 6]) # => 10
# yahtzee_upper([1, 1, 1, 1, 3]) # => 4
# yahtzee_upper([1, 1, 1, 3, 3]) # => 6
# yahtzee_upper([1, 2, 3, 4, 5]) # => 5
# yahtzee_upper([6, 6, 6, 6, 6]) # => 30
#
# yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
#     1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
#     30864, 4868, 30864]) # => 123456

# ------------------------------------------------------------------
## Challenge #383: [Easy] Necklace Matching
# Link: https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

## personal answer 1 (too long and complex)
def same_necklace_long(str1, str2):
    if str1 == "" and str2 == "": print(True)
    else:
        permutations = list()
        for i in range(len(str1)):
            perm = rotate_right(str1, i)
            if perm not in permutations:
                permutations.append(perm)
        print(str1 in permutations and str2 in permutations)

def rotate_right(str, count):
    permutations = ''
    for i in range(len(str)):
        mod = (i + count) % len(str)
        if (mod >= len(str)): mod -= len(str)
        permutations += str[mod]
    return permutations

## personal answer 2
def same_necklace(str1,str2):
    ans = False
    if str1 == "" and str2 == "": ans = True
    for i in range(len(str1)):
        if str1 == (str2[i:] + str2[:i]): ans = True
    print(ans)

# Run the program:
# same_necklace("nicole", "icolen") # => true
# same_necklace("nicole", "lenico") # => true
# same_necklace("nicole", "coneli") # => false
# same_necklace("aabaaaaabaab", "aabaabaabaaa") # => true
# same_necklace("abc", "cba") # => false
# same_necklace("xxyyy", "xxxyy") # => false
# same_necklace("xyxxz", "xxyxz") # => false
# same_necklace("x", "x") # => true
# same_necklace("x", "xx") # => false
# same_necklace("x", "") # => false
# same_necklace("", "") # => true

# ------------------------------------------------------------------
## Challenge #384: [Intermediate] Necklace Matching
# Link: https://www.reddit.com/r/dailyprogrammer/comments/g1xrun/20200415_challenge_384_intermediate_necklace/
# For the purpose of this challenge, a k-ary necklace of length n is a sequence of n letters chosen from k options,
# e.g. ABBEACEEA is a 5-ary necklace of length 9. Note that not every letter needs to appear in the necklace.
# Two necklaces are equal if you can move some letters from the beginning to the end to make the other one,
#otherwise maintaining the order. For instance, ABCDE is equal to DEABC.

# Today's challenge is, given k and n, find the number of distinct k-ary necklaces of length n.
# That is, the size of the largest set of k-ary necklaces of length n such that no two of them are equal to each other.
# For example, there are 24 distinct 3-ary necklaces of length 4, so necklaces(3, 4) is 24.
def prime(number): # check if a number is prime
    for i in range(2, number):
        if (number % i == 0): return False
    return True

# Test:
# print(prime(1) == False)
# print(prime(2) == True)
# print(prime(19) == True)
# print(prime(49) == False)

def product(iter):
    p = 1
    for i in iter: p *= i
    return p

# Test:
# print(product([1, 2, 3, 5])) # => 30
# print(product([1, 8, 9])) # => 72

def phi(num): # compute the phi value of a number
    primes = []
    all = [i for i in range(2, num + 1)]
    for a in all:
        if prime(a) and (num % a == 0): primes.append(a)
    return num * (product([i - 1 for i in primes])) // (product(primes))

# Test:
# print(phi(12)) # => 4
# print(phi(2)) # => 1
# print(phi(15)) # => 8
# print(phi(13)) # => 12
# print(phi(11)) # => 10

def factors(num):
    factor_list = []
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i * j == num and (i not in factor_list):
                factor_list.append(i)
    return factor_list

# Test:
# print(factors(10)) # => [1, 2, 5, 10]
# print(factors(49)) # => [1, 7, 49]

def necklaces(k, n):
    result = 0
    for f in factors(n):
        result += phi(f) * k**(n // f)
    return result // n


# Test:
# Easy examples
# print(necklaces(2, 12) == 352)
# print(necklaces(3, 7) == 315)
# print(necklaces(9, 4) == 1665)
# print(necklaces(21, 3) == 3101)
# print(necklaces(99, 2) == 4950)
# Harder examples
# print(necklaces(3, 90) == 96977372978752360287715019917722911297222)
# print(necklaces(123, 18) == 2306850769218800390268044415272597042)
# print(necklaces(1234567, 6) == 590115108867910855092196771880677924)
# print(necklaces(12345678910, 3) == 627225458787209496560873442940)

# ------------------------------------------------------------------
## Challenge #385: [Intermediate] Necklace Matching
# Link: https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/

# Function prisoner1 takes two inputs: a series S of 64 bits,
# and a number X from 0 to 63 (inclusive). It returns a number Y from 0 to 63.
def prisoner1(series, x):
    # index is the location of the coin
    # s is the state of that coin (heads=1 or tails=0)
    for index, s in enumerate(series):
        x ^= s*index
    return x

def prisoner2(series):
    return prisoner1(series, 0)

def flip(series, pos):
    series[pos] = 1 - series[pos]
    return series

# provided pseudocode
def solve(series, x):
    y = prisoner1(series, x)
    t = flip(series, y)
    return prisoner2(t) == x

import random
def main():
    # create a series of 64 bits and a number from 0 to 63
    series = [random.randint(0, 1) for i in range(64)]
    x = random.randint(0, 63)
    print(solve(series, x))

# main()
