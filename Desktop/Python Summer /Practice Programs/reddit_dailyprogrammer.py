# ------------------------------------------------------------------
##  Challenge #378 [Easy] The Havel-Hakimi algorithm for graph realization
# Link: https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

def hh(seq):
    # Remove all 0's from the sequence (i.e. warmup1).
    # If the sequence is now empty (no elements left), stop and return true.
    # Sort the sequence in descending order (i.e. warmup2).
    # Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and call it N.
    # The sequence is now 1 shorter than it was after the previous step.
    # If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
    # Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).
    # Continue from step 1 using the sequence from the previous step.
    # Eventually you'll either return true in step 2, or false in step 5.
    while seq:
        # print("begin: %s" % seq)
        seq = [n for n in seq if n != 0]
        if len(seq) == 0:
            return True
        # print("no zeroes: %s" % seq)
        seq.sort(reverse=True)
        N = seq.pop(0)
        # print(N, "popped: %s" % seq)
        if N > len(seq):
            return False
        else:
            for i in range(N): seq[i] -= 1
            # print("dec by 1: %s" % seq)
    return True

print(not hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
print(not hh([4, 2, 0, 1, 5, 0]))
print(hh([3, 1, 2, 3, 1, 0]))
print(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
print(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))
print(not hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))
print(not hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))
print(not hh([2, 2, 0]))
print(not hh([3, 2, 1]))
print(hh([1, 1]))
print(not hh([1]))
print(hh([]))

# ------------------------------------------------------------------
## Challenge #379: [Easy] Progressive taxation
# Link: https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

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

# Run the program
# print(tax(12000) == 200)
# print(tax(56789) == 8697)
# print(tax(1234567) == 473326)

def get_income(tax_rate):
    tax_rate = round(tax_rate, 4)
    hi = 1000000000 - 1
    lo = 0
    result = 0
    # use binary search: O(log(n))
    while (lo <= hi):
        mid = (hi + lo) / 2
        to_compare = round(tax(mid) / mid, 4) # tax = income * tax_rate
        if to_compare > tax_rate:
            hi = mid - 1
        elif to_compare < tax_rate:
            lo = mid + 1
        else:
            result = round(mid)
            break
    return result

# answer should be close to the provided comments
# print(get_income(0.06)) # => 25000
# print(get_income(0.09)) # => 34375
# print(get_income(0.32)) # => 256250

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
