import unittest
import random
import math
import operator

# ------------------------------------------------------------------
##  Challenge #361 [Easy] Tally Program
# Link: https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/
def tally_ho(str):
    tally_dict = dict()
    for char in str:
        if char.islower():
            tally_dict[char] = tally_dict.get(char, 0) + 1
        if char.isupper():
            dec = char.lower()
            tally_dict[dec] = tally_dict.get(dec, 0) - 1

    return {k: v for k, v in sorted(tally_dict.items(), key=lambda item: item[1], reverse=True)}

# print(tally_ho('dbbaCEDbdAacCEAadcB'))
# print(tally_ho('EbAAdbBEaBaaBBdAccbeebaec'))

# ------------------------------------------------------------------
##  Challenge #367 [Easy] Subfactorials - Another Twist on Factorials
# Link: https://www.reddit.com/r/dailyprogrammer/comments/9cvo0f/20180904_challenge_367_easy_subfactorials_another/
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)

def subfactorials(n): # this follows the formula given by Wolfram: https://mathworld.wolfram.com/Subfactorial.html
    sum = 0
    for k in range(n+1):
        diff = n - k
        sum += (factorial(n) * (-1)**diff) / factorial(diff)
    return int(sum)

def derangement(n): # this follows the recursive formula from: https://en.wikipedia.org/wiki/Derangement
    if n == 0: return 1
    if n == 1: return 0
    return (n - 1) * (derangement(n - 2) + derangement(n - 1))

# ------------------------------------------------------------------
##  Challenge #367 [Hard] The Mondrian Puzzle
# Link: https://www.reddit.com/r/dailyprogrammer/comments/9dv08q/20180907_challenge_367_hard_the_mondrian_puzzle/
def all_rectangles(n):
    rectangles = list()
    for i in range(1, n):
        for j in range(1, n+1):
            if j >= i: rectangles.append((i, j, i*j))
    return rectangles

def make_canvas(n):
    # base case
    if n <= 2: return None

    rectangle_set = all_rectangles(n)
    combos = []
    diff = 0
    total_area = 0
    target_area = n**2

    while total_area != target_area:
        random_area = random.choice(rectangle_set)
        if random_area not in combos:
            combos.append(random_area)
            total_area += random_area[2]

        areas = [c[2] for c in combos]
        diff = max(areas) - min(areas)

        if total_area > target_area:
            combos.clear()
            perimeter = 0
            total_area = 0
            diff = 0
            continue

    return diff, combos


def solve_mondrian(n):
    diff, combos = make_canvas(n)
    min = n**2
    all_diff = list()
    all_combos = list()
    idx = 0
    access = 0

    while combos not in all_combos:
        all_diff.append(diff)
        all_combos.append(combos)
        if min > diff:
            min = diff
            access = idx
        diff, combos = make_canvas(n)
        idx += 1

    return all_combos[access], min

def solve_mondrian_M_times(dim, M):
    abs_min = dim**2
    abs_combo = list()
    for m in range(M):
        combo, diff = solve_mondrian(dim)
        print(diff)
        if diff < abs_min:
            abs_min = diff
            abs_combo = combo

    print(f'solved {dim}x{dim} puzzle {M} times:')
    print(abs_combo, abs_min)

solve_mondrian_M_times(15, 10)
# the more cycles you run, the more accurate the result;
# the best answer for 4x4 is 4, 11x11 is 9, 15x15 is 6, 32x32 is 16

# ------------------------------------------------------------------
##  Challenge #368 [Intermediate] Single-symbol squares
# Link: https://www.reddit.com/r/dailyprogrammer/comments/9z3mjk/20181121_challenge_368_intermediate_singlesymbol/

def random_grid(size):
    grid = []
    for y in range(size):
        grid.append([])
        for x in range(size):
            grid[y].append(random.choice(['X', 'O']))
    return grid

def check_grid(grid, size):
    for y in range(size):
        for x in range(size):
            dist = min(size - x, size - y)
            for i in range(1, dist):
                nw = grid[y][x]
                ne = grid[y][x + i]
                se = grid[y + i][x + i]
                sw = grid[y + i][x]
                if nw == ne and ne == se and se == sw:
                    return False
    return True

def make_grid(size): # O(n^4) solution
    count = 0
    grid = random_grid(size)
    while True:
        count += 1
        if check_grid(grid, size): break
        else: grid = random_grid(size)

    for s in range(size):
        print(' '.join(grid[s]))

    print('total iterations: %s' % count)

# make_grid(3) # can go up to 7 with 0.48s; stops at 8 (no response)

# ------------------------------------------------------------------
##  Challenge #369 [Easy] Hex colors
# Link: https://www.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/
dex_hex = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def dec_to_hex(dec):
    hex_list=[]
    while len(hex_list) < 2:
        rem = dec % 16
        to_add = str(rem)
        if rem >= 10: to_add = dex_hex[rem]
        hex_list.append(to_add)
        dec //= 16

    return ''.join(reversed(hex_list))

def hexcolour(red, green, blue):
    return '#'+dec_to_hex(red)+dec_to_hex(green)+dec_to_hex(blue)

class HexTest(unittest.TestCase):
    def test_hexcolours(self):
        self.assertEqual(hexcolour(255, 99, 71), "#FF6347")
        self.assertEqual(hexcolour(184, 134, 11), "#B8860B")
        self.assertEqual(hexcolour(189, 183, 107), "#BDB76B")
        self.assertEqual(hexcolour(0, 0, 205), "#0000CD")

# if __name__ == "__main__":
#     unittest.main(HexTest())

# ------------------------------------------------------------------
##  Challenge #370 [Easy] UPC check digits
# Link: https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/
def upc_check_digit(code_str):
    sum_even = 0
    sum_odd = 0
    for i, d in enumerate(code_str):
        digit = int(d)
        if i % 2 == 0:
            sum_even += digit
        else: sum_odd += digit
    remainder = (sum_even*3 + sum_odd) % 10
    return 10 - remainder

class UPCTest(unittest.TestCase):
    def test_upc(self):
        self.assertTrue(upc_check_digit('03600029145'), 2)
        self.assertTrue(upc_check_digit('4210000526'), 4)
        self.assertTrue(upc_check_digit('3600029145'), 2)
        self.assertTrue(upc_check_digit('12345678910'), 4)
        self.assertTrue(upc_check_digit('1234567'), 0)

# if __name__ == "__main__":
#     unittest.main(UPCTest())

# ------------------------------------------------------------------
##  Challenge #371 [Easy] N queens validator
# Link: https://www.reddit.com/r/dailyprogrammer/comments/ab9mn7/20181231_challenge_371_easy_n_queens_validator/
def q_check(s_list):
    for idx1, val1 in enumerate(s_list):
        for idx2, val2 in enumerate(s_list):
            if idx1 == idx2: continue
            if val1 == val2:
                # print(val1, val2)
                return False
            if abs(val1 - val2) == abs(idx1 - idx2):
                # print(val1, val2, idx1, idx2)
                return False
    return True

def q_fix(old_list):
    for i in range(len(old_list)):
        for j in range(len(old_list)):
            if i == j: continue
            new_list = old_list[:]
            # swap the first element with any other element in the list until the queen check is satisfied
            # if first element does not work, then move to second element and so on
            new_list[i], new_list[j] = new_list[j], new_list[i]
            if q_check(new_list): return new_list
    return False

class QueenTest(unittest.TestCase):
    # The simplest TestCase subclass will simply implement a test method (i.e. a method whose name starts with test)
    def test_queen(self):
        self.assertTrue(q_check([4, 2, 7, 3, 6, 8, 5, 1]))
        self.assertTrue(q_check([2, 5, 7, 4, 1, 8, 6, 3]))
        self.assertFalse(q_check([5, 3, 1, 4, 2, 8, 6, 3]))
        self.assertFalse(q_check([5, 8, 2, 4, 7, 1, 3, 6]))
        self.assertFalse(q_check([4, 3, 1, 8, 1, 3, 5, 2]))

    def test_queen_fix(self):
        self.assertEqual(q_fix([8, 6, 4, 2, 7, 1, 3, 5]), [4, 6, 8, 2, 7, 1, 3, 5])
        self.assertEqual(q_fix([8, 5, 1, 3, 6, 2, 7, 4]), [8, 4, 1, 3, 6, 2, 7, 5])
        self.assertEqual(q_fix([4, 6, 8, 3, 1, 2, 5, 7]), [4, 6, 8, 3, 1, 7, 5, 2])
        self.assertEqual(q_fix([7, 1, 3, 6, 8, 5, 2, 4]), [7, 3, 1, 6, 8, 5, 2, 4])

# if __name__ == "__main__":
#     unittest.main(QueenTest())

# ------------------------------------------------------------------
##  Challenge #372 [Easy] Perfectly balanced
# Link: https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/
def balanced(str):
    return str.count('x') == str.count('y')

def balanced_bonus(str):
    char_dict = dict()
    for char in str:
        char_dict[char] = char_dict.get(char, 0) + 1

    compare = 0
    for char in char_dict:
        if compare == 0:
            compare = char_dict[char]
            continue
        if char_dict[char] != compare:
            return False
    return True

class BalancedTest(unittest.TestCase):
    def test_balanced(self):
        self.assertTrue(balanced("xxxyyy"))
        self.assertFalse(balanced("xxxyyyy"))
        self.assertTrue(balanced(""))
        self.assertFalse(balanced("x"))
        self.assertTrue(balanced("yyxyxxyxxyyyyxxxyxyx"))
        self.assertFalse(balanced("xyxxxxyyyxyxxyxxyy"))

    def test_balanced_bonus(self):
        self.assertTrue(balanced_bonus("xxxyyyzzz"))
        self.assertTrue(balanced_bonus("abccbaabccba"))
        self.assertTrue(balanced_bonus("xxxyyy"))
        self.assertTrue(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(balanced_bonus("pqq"))
        self.assertFalse(balanced_bonus("fdedfdeffeddefeeeefddf"))
        self.assertTrue(balanced_bonus("x"))
        self.assertTrue(balanced_bonus(""))

# if __name__ == "__main__":
#     unittest.main(BalancedTest())

# ------------------------------------------------------------------
##  Challenge #374 [Easy] Additive Persistence
# Link: https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

def add_every_digit(num):
    sum = 0
    while num > 0:
        sum += num % 10 # help get last digit
        num //= 10 # eliminate last digit
    return sum

def additive_persistence(num):
    iter = 0
    while num >= 10:
        num = add_every_digit(num)
        iter += 1
    return iter

class AdditivePersistenceTest(unittest.TestCase):
    def test_ap(self):
        self.assertEqual(additive_persistence(13), 1)
        self.assertEqual(additive_persistence(199), 3)
        self.assertEqual(additive_persistence(1234), 2)
        self.assertEqual(additive_persistence(9876), 2)

# if __name__ == "__main__":
#     unittest.main(AdditivePersistenceTest())

# ------------------------------------------------------------------
##  Challenge #374 [Hard] Nonogram Solver
# Link: https://www.reddit.com/r/dailyprogrammer/comments/am1x6o/20190201_challenge_374_hard_nonogram_solver/

# most of this is hard-coded, so only works for the first image.
# def draw_board(columns, rows):
#     grid = []
#     for row in range(rows):
#         grid.append([])
#         for column in range(columns):
#             grid[row].append(' ')
#     return grid
#
# def draw_rows(input, row, grid):
#     max_col = 0
#     for row_idx, elem in enumerate(input):
#         elems = elem.split(',')
#         if int(elems[0]) > max_col: max_col = int(elems[0])
#         for col_idx in range(int(elems[0])):
#             grid[row_idx][col_idx] = '*'
#         if len(elems) > 1:
#             for i in range(1, len(elems)):
#                 start_pos = int(elems[i])
#                 # print(start_pos, row_idx, col_idx)
#                 for col_idx in range(max_col - start_pos, max_col):
#                     # print(start_pos, row_idx, col_idx)
#                     grid[row_idx][col_idx] = '*'
#
#     for i in range(row): print(''.join(grid[i]))
#     return grid
#
# def draw_columns(input, grid):
#     max_row = 0
#     for col_idx, elem in enumerate(input): # 0,1,2,3,4
#         # print(col_idx)
#         elems = elem.split(',')
#         if int(elems[0]) > max_row: max_row = int(elems[0])
#         for row_idx in range(int(elems[0])):
#             # print(elems[0], row_idx, col_idx)
#             grid[row_idx][col_idx] = '*'
#         if len(elems) > 1:
#             for i in range(1, len(elems)):
#                 start_pos = int(elems[i])
#                 for row_idx in range(max_row - start_pos, max_row):
#                     grid[row_idx][col_idx] = '*'
#
#     for i in range(max_row): print(''.join(grid[i]))
#     return grid
#
# def draw_nonogram(num_col, num_rows, col_input, row_input):
#     grid = draw_board(num_col, num_rows)
#     # draw_columns(col_input, grid)
#     # print('\n'+'------------------------'+'\n')
#     draw_rows(row_input, num_rows, grid)
#     return grid


# draw_nonogram(5, 5, ["5","2,2","1,1","2,2","5"], ["5","2,2","1,1","2,2","5"])
# draw_nonogram(8, 11, ["0","9","9","2,2","2,2","4","4","0"], ["0","4","6","2,2","2,2","6","4","2","2","2","0"])
# draw_nonogram(30, 20,
# ["1","1","2","4","7","9","2,8","1,8","8","1,9","2,7","3,4","6,4","8,5","1,11",
# "1,7","8","1,4,8","6,8","4,7","2,4","1,4","5","1,4","1,5","7","5","3","1","1"],
# ["8,7,5,7","5,4,3,3","3,3,2,3","4,3,2,2","3,3,2,2","3,4,2,2","4,5,2","3,5,1",
# "4,3,2","3,4,2","4,4,2","3,6,2","3,2,3,1","4,3,4,2","3,2,3,2","6,5","4,5","3,3","3,3","1,1"])

# ------------------------------------------------------------------
##  Challenge #375 [Easy] Print a new number by adding one to each of its digit
# Link: https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/

def plus_one_to_digit(num):
    remains = num
    result = 0
    extra = 0
    for i in range(len(str(num))):
        digit = remains % 10 # 1st loop: 8, 2nd loop: 9, 3rd loop: 9
        result += (digit + 1) * (10**(i+extra)) # 1st loop: 9, 2nd loop: 100, 3rd loop: 10000
        if digit >= 9: extra = 1
        else: extra = 0
        remains = (remains - digit) // 10 # 1st loop: 99, 2nd loop: 9
    return result

# Run the program (should return True):
# print(plus_one_to_digit(998) == 10109)

# ------------------------------------------------------------------
##  Challenge #375 [Intermediate] A Card Flipping Game
# https://www.reddit.com/r/dailyprogrammer/comments/aq6gfy/20190213_challenge_375_intermediate_a_card/
def flip(char):
    if char == '.': return char
    else:
        return '0' if char == '1' else '1'

def remove_card(str, i):
    seq = [char for char in str]
    seq[i] = '.'
    if i - 1 >= 0:
        seq[i - 1] = flip(seq[i - 1])
    if i + 1 < len(seq):
        seq[i + 1] = flip(seq[i + 1])
    return seq

def card_flip(str, steps):
    if len(steps) < len(str):
        for i, char in enumerate(str):
            if char == '1':
                steps.append(i)
                return card_flip(remove_card(str, i), steps)
    # return the steps if all cards are flipped
    return steps if str.count('.') == len(str) else 'no solution'

# Run the program (should all be true):
# print(card_flip('0100110', []) == [1, 0, 2, 3, 5, 4, 6])
# print(card_flip('01001100111', []) == 'no solution')
# print(card_flip('100001100101000', []) == [0, 1, 2, 3, 4, 6, 5, 7, 8, 11, 10, 9, 12, 13, 14])
# Bonus input:
# print(card_flip('010111111111100100101000100110111000101111001001011011000011000', []))

# ------------------------------------------------------------------
##  Challenge #376 [Intermediate] The Revised Julian Calendar
# Link: https://www.reddit.com/r/dailyprogrammer/comments/b0nuoh/20190313_challenge_376_intermediate_the_revised/

def is_leap(year): # naive approach
    if year % 4 != 0: return False
    if year % 100 == 0 and not (year % 900 == 200 or year % 900 == 600): return False
    return True

def count_leaps(year):
    # a year is a leap year if:
    # it is a multiple of 4 and not a multiple of 100
    # except when the remainder when divided by 900 is either 200 or 600
    return year // 4 - year // 100 + (year - 600) // 900 + (year - 200) // 900

def leaps(year1, year2):
    if year2 < year1: return None
    elif year1 == year2: return 0
    else:
        year1 -= 1
        # for year in range(year1, year2): # O(n) implementation
        #     if is_leap(year): leaps += 1
        return count_leaps(year2) - count_leaps(year1) # O(1) implementation

class LeapYear(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leaps(2016, 2017), 1)
        self.assertEqual(leaps(2019, 2017), None)
        self.assertEqual(leaps(1900, 1901), 0)
        self.assertEqual(leaps(2000, 2001), 1)
        self.assertEqual(leaps(123456, 123456), 0)
        self.assertEqual(leaps(1234, 5678), 1077)
        self.assertEqual(leaps(123456789101112, 1314151617181920), 288412747246241)

# if __name__ == "__main__":
#     unittest.main(LeapYear())

# ------------------------------------------------------------------
##  Challenge #377 [Easy] Axis-aligned crate packing
# Link: https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

def fit1(X, Y, x, y):
    return int(X / x) * int(Y / y)

def fit2(X, Y, x, y):
    return max(fit1(X, Y, x, y), fit1(X, Y, y, x))

from itertools import permutations
def fit3(X, Y, Z, x, y, z):
    b_dim = [x, y, z]
    results = []
    for box in list(permutations(b_dim)):
        perm = fit2(X, Y, box[0], box[1]) * (int(Z / box[2]))
        results.append(perm)
    return max(results)
# since fitN works, you can just use fixN here if you'd like

def fitN(crate_dim, box_dim):
    result = 0
    for box in list(permutations(box_dim)):
        fit = 1
        for index, dim in enumerate(box):
            # match correct crate_dim to the respective box_dim (ensure same orientation)
            fit *= crate_dim[index] // dim
        result = max(fit, result) # update result for each permutation (find greatest value)
    return result

class FitTest(unittest.TestCase):
    def test_fit1(self):
        self.assertEqual(fit1(25, 18, 6, 5), 12)
        self.assertEqual(fit1(10, 10, 1, 1), 100)
        self.assertEqual(fit1(12, 34, 5, 6), 10)
        self.assertEqual(fit1(12345, 678910, 1112, 1314), 5676)
        self.assertEqual(fit1(5, 100, 6, 1), 0)
    def test_fit2(self):
        self.assertEqual(fit2(25, 18, 6, 5), 15)
        self.assertEqual(fit2(12, 34, 5, 6), 12)
        self.assertEqual(fit2(5, 5, 3, 2), 2)
        self.assertEqual(fit2(5, 100, 6, 1), 80)
        self.assertEqual(fit2(5, 5, 6, 1), 0)
    def test_fit3(self):
        self.assertEqual(fit3(10, 10, 10, 1, 1, 1), 1000)
        self.assertEqual(fit3(12, 34, 56, 7, 8, 9), 32)
        self.assertEqual(fit3(123, 456, 789, 10, 11, 12), 32604)
        self.assertEqual(fit3(1234567, 89101112, 13141516, 171819, 202122, 232425), 174648)
    def test_fitN(self):
        self.assertEqual(fitN([12, 34, 56], [7, 8, 9]), 32)
        self.assertEqual(fitN([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21]), 1883443968)

# if __name__ == "__main__":
#     unittest.main(FitTest())

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

class HavelHakimiTest(unittest.TestCase):
    def test_hh(self):
        self.assertFalse(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
        self.assertFalse(hh([4, 2, 0, 1, 5, 0]))
        self.assertTrue(hh([3, 1, 2, 3, 1, 0]))
        self.assertTrue(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
        self.assertTrue(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))
        self.assertFalse(hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))
        self.assertFalse(hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))
        self.assertFalse(hh([2, 2, 0]))
        self.assertFalse(hh([3, 2, 1]))
        self.assertFalse(hh([1]))
        self.assertTrue(hh([]))
        self.assertTrue(hh([1, 1]))

# if __name__ == "__main__":
#     unittest.main(HavelHakimiTest())

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

def get_income(tax_rate):
    tax_rate = round(tax_rate, 4)
    hi = 100000000 - 1
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

class TaxationTest(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(tax(12000), 200)
        self.assertEqual(tax(56789), 8697)
        self.assertEqual(tax(1234567), 473326)
    def test_income(self):
        self.assertAlmostEqual(get_income(0.06), 25000, delta=100)
        self.assertAlmostEqual(get_income(0.09), 34375, delta=100)
        self.assertAlmostEqual(get_income(0.32), 256250, delta=100)

# if __name__ == "__main__":
#     unittest.main(TaxationTest())

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
    return max_result

class YahtzeeTest(unittest.TestCase):
    def test_yahtzee(self):
        self.assertEqual(yahtzee_upper([2, 3, 5, 5, 6]), 10)
        self.assertEqual(yahtzee_upper([1, 1, 1, 1, 3]), 4)
        self.assertEqual(yahtzee_upper([1, 1, 1, 3, 3]), 6)
        self.assertEqual(yahtzee_upper([1, 2, 3, 4, 5]), 5)
        self.assertEqual(yahtzee_upper([6, 6, 6, 6, 6]), 30)
        self.assertEqual(yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
        1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
        30864, 4868, 30864]), 123456)

# if __name__ == "__main__":
#     unittest.main(YahtzeeTest())

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

def product(iter):
    p = 1
    for i in iter: p *= i
    return p

def phi(num): # compute the phi value of a number
    primes = []
    all = [i for i in range(2, num + 1)]
    for a in all:
        if prime(a) and (num % a == 0): primes.append(a)
    return num * (product([i - 1 for i in primes])) // (product(primes))

# Phi value of 2, 11, 12, 13, 15 should be 1, 10, 4, 12, and 8 respectively

def factors(num):
    factor_list = []
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i * j == num and (i not in factor_list):
                factor_list.append(i)
    return factor_list

def necklaces(k, n):
    result = 0
    for f in factors(n):
        result += phi(f) * k**(n // f)
    return result // n

class NecklaceMatchingTest(unittest.TestCase):
    def test_necklace(self):
        self.assertEqual(necklaces(2, 12), 352)
        self.assertEqual(necklaces(3, 7), 315)
        self.assertEqual(necklaces(9, 4), 1665)
        self.assertEqual(necklaces(21, 3), 3101)
        self.assertEqual(necklaces(99, 2), 4950)
        self.assertEqual(necklaces(3, 90), 96977372978752360287715019917722911297222)
        self.assertEqual(necklaces(123, 18), 2306850769218800390268044415272597042)
        self.assertEqual(necklaces(1234567, 6), 590115108867910855092196771880677924)
        self.assertEqual(necklaces(12345678910, 3), 627225458787209496560873442940)

# if __name__ == "__main__":
#     unittest.main(NecklaceMatchingTest())

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

def main():
    # create a series of 64 bits and a number from 0 to 63
    series = [random.randint(0, 1) for i in range(64)]
    x = random.randint(0, 63)
    print(solve(series, x))

# main()
