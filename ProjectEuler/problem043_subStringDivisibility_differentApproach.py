# Sub-string divisibility
#
# Problem 43
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in
# some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# ------------------------------------------------------------------------------
# idea:
# * the last triplet should be the most "awkward":
# ** construct all possible triplets from 0to9pandigital number-space: and check if div-able by 17
# ** if yes, then add one letter in front and check the new triplet if this is also divisable by 13
# ** .. same approach for the rest: this shall really rule out a lot of duds
# * question how many take-three-from-ten variants exist? (3 digits can be arranged in 6 different ways) - there should be 12 over 9 variations to pick 3 elements of ten given ones; then rearranging the oder multiply with six
# * but wait: instead of making a fuzz: for the start just count up all multiples of 17 from 0 to 1000: then check if unique digits (nothing double) and then use this as start for the additional checks ..
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# todo: works, but has a problem with numbers with less than three digits (like 0), because the prefix of zeroes would be added -> boom, not fitting anymore!
def hasUniqueDigits(number):
    stringified = str(number)
    everycharUnique = len(set(stringified)) == len(stringified)
    return everycharUnique

# ------------------------------------------------------------------------------
print(hasUniqueDigits(221)) # todo convert to unit-test!
print(hasUniqueDigits(123))
# ------------------------------------------------------------------------------

def generateAlld8d9d10Numbers():
    candidates = []
    startingValue = 0
    while startingValue < 1000:
        if startingValue % 17 == 0:
            if hasUniqueDigits(startingValue):
                print(startingValue)
                candidates.append(startingValue)

        startingValue += 17

    print("candidates:", candidates)
    print("number of items:", len(candidates))

# ------------------------------------------------------------------------------

import time
currentTime = time.time()
generateAlld8d9d10Numbers()
print("generation took", time.time() - currentTime, "s")
