# Lexicographic permutations
#
# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# ----------------

# idea: brute force; just count upwards, check if the number would be a valid permutation ..

# --------------

# init
comparisonList = []
for i in range(0,10):
    comparisonList.append(str(i))

def isValidPermutation(number):
    asListOfChars = [x for x in str(number)]
    asListOfChars.sort()
    print("as char:", asListOfChars)
    return asListOfChars == comparisonList

print(comparisonList)
print("1234567890:", isValidPermutation(1234567890))
