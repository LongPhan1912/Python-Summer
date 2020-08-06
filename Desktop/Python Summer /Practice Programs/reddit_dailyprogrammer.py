## Challenge #381: Yahtzee Upper Section Scoring
# Link: https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

def yahtzee_upper(sorted_int_list):
    d = dict()
    max_result = 0
    for key in sorted_int_list:
        d[key] = d.get(key, 0) + 1
        value = d[key]
        if max_result < key * value: max_result = key * value
    print(max_result)

# yahtzee_upper([2, 3, 5, 5, 6]) # => 10
# yahtzee_upper([1, 1, 1, 1, 3]) # => 4
# yahtzee_upper([1, 1, 1, 3, 3]) # => 6
# yahtzee_upper([1, 2, 3, 4, 5]) # => 5
# yahtzee_upper([6, 6, 6, 6, 6]) # => 30
#
# yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
#     1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
#     30864, 4868, 30864]) # => 123456

## Challenge #383: Necklace Matching
# Link: https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

## personal answer 1 (too long and complex)
# def same_necklace(str1, str2):
#     if str1 == "" and str2 == "": print(True)
#     else:
#         permutations = list()
#         for i in range(len(str1)):
#             perm = rotate_right(str1, i)
#             if perm not in permutations:
#                 permutations.append(perm)
#         print(str1 in permutations and str2 in permutations)
#
# def rotate_right(str, count):
#     permutations = ''
#     for i in range(len(str)):
#         mod = (i + count) % len(str)
#         if (mod >= len(str)): mod -= len(str)
#         permutations += str[mod]
#     return permutations

## personal answer 2
def same_necklace(str1,str2):
    ans = False
    if str1 == "" and str2 == "": ans = True
    for i in range(len(str1)):
        if str1 == (str2[i:] + str2[:i]): ans = True
    print(ans)


## given answer in comments
# def same_necklace(necklaceA,necklaceB):
#     ans = False
#     if necklaceA == "" and necklaceB == "":
#         ans = True
#     for i in range(len(necklaceB)):
#         if necklaceA == (necklaceB[i:] + necklaceB[:i]):
#             ans = True
#     print(ans)
#     return ans

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
