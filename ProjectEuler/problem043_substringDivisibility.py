# Sub-string divisibility
#
# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
# order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
#
# ------------------------------------------------------------------------------
# idea:
# * a function to check if the required attributes are satisfied
# * a function to create all permutations of 0..9: question is a leading zero a valid number?
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def tripleDivideableBy(numString, firstIndex, dividend):
    subString = numString[firstIndex:firstIndex+3]
    #print("original:", numString, "firstIndex:", firstIndex, "subString:", subString)

    query = int(subString) % dividend == 0
    return query

# ------------------------------------------------------------------------------

def satisfiesRequiredDivisibilityAttributes(number):
    # to make indexing easier, I add a dummy in the beginning
    numString = "X" + str(number)

    # the tests for the required attribute
    # TODO make this less "DRY" by using a list of index and dividend
    if not tripleDivideableBy(numString, 2, 2):
        #print("2")
        return False # break early, save the rest of the evaluation

    if not tripleDivideableBy(numString, 3, 3):
        #print("3")
        return False

    if not tripleDivideableBy(numString, 4, 5):
        #print("5")
        return False

    if not tripleDivideableBy(numString, 5, 7):
        #print("7")
        return False

    if not tripleDivideableBy(numString, 6, 11):
        #print("11")
        return False

    if not tripleDivideableBy(numString, 7, 13):
        #print("13")
        return False

    if not tripleDivideableBy(numString, 8, 17):
        #print("17")
        return False

    # if the control flow came here, then we satisfy everything
    return True

print("test:", satisfiesRequiredDivisibilityAttributes(1406357289))
# TODO put this into a unit-test!

# ------------------------------------------------------------------------------

def driver():
    import itertools
    elementSet = "01234567890"
    # create the permutations
    permuts = itertools.permutations(elementSet)

    # test them
    resultSum = 0
    for elem in permuts:
        if elem[0] == "0":
            #print("wrong candidate, leading zero")
            continue

        #print("handle now:", elem)
        candidate = int(''.join(elem)) # convert the tuple to string; and this to int
        isValid = satisfiesRequiredDivisibilityAttributes(candidate)
        if isValid:
            print("candidate:", candidate)
            resultSum += candidate

    print("resultSum:", resultSum)

# ------------------------------------------------------------------------------
# unit test
# ------------------------------------------------------------------------------
# import unittest
# class Testcase(unittest.TestCase):
#
#     def test_whatever(self):
#         #self.assertEqual(36, computeAmountOfDivisors(3658732))
#         pass

# --- test call

import time
startTime = time.time()
print("starting computation now:", startTime)
driver()
print("computation took:", time.time() - startTime, "s")

# ------------------------------------------------------------------------------
# starting computation now: 1577046626.7263896
# candidate: 10309528674
# candidate: 10603572894
# candidate: 10063572894
# candidate: 13009528674
# candidate: 13009528674
# candidate: 14063572890
# candidate: 14003572896
# candidate: 14009528673
# candidate: 14309528670
# candidate: 14309528670
# candidate: 14603572890
# candidate: 14603572890
# candidate: 14003572896
# candidate: 14009528673
# candidate: 14063572890
# candidate: 16003572894
# candidate: 16003572894
# candidate: 10063572894
# candidate: 10309528674
# candidate: 10603572894
# candidate: 31009528674
# candidate: 31009528674
# candidate: 34009528671
# candidate: 34009528671
# candidate: 40309528671
# candidate: 40603572891
# candidate: 40063572891
# candidate: 41063572890
# candidate: 41003572896
# candidate: 41009528673
# candidate: 41309528670
# candidate: 41309528670
# candidate: 41603572890
# candidate: 41603572890
# candidate: 41003572896
# candidate: 41009528673
# candidate: 41063572890
# candidate: 43009528671
# candidate: 43009528671
# candidate: 46003572891
# candidate: 46003572891
# candidate: 40063572891
# candidate: 40309528671
# candidate: 40603572891
# candidate: 61003572894
# candidate: 61003572894
# candidate: 64003572891
# candidate: 64003572891
# resultSum: 1473970614426
# computation took: 100.16895651817322 s
#
# Process finished with exit code 0

# ------------------------------------------------------------------------------
# lol ..
# Sorry, but the answer you gave appears to be incorrect.
#
# Go back to Problem 43.
