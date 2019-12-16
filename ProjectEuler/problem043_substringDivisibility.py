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
    numList = [char for char in str(number)]
    # to make indexing easier, I add a dummy in the beginning
    numString = "X" + str(number)

    # the tests for the required attribute
    # TODO make this less "DRY" by using a list of index and dividend
    if not tripleDivideableBy(numString, 2, 2):
        print("2")
        return False # break early, save the rest of the evaluation

    if not tripleDivideableBy(numString, 3, 3):
        print("3")
        return False

    if not tripleDivideableBy(numString, 4, 5):
        print("5")
        return False

    if not tripleDivideableBy(numString, 5, 7):
        print("7")
        return False

    if not tripleDivideableBy(numString, 6, 11):
        print("11")
        return False

    if not tripleDivideableBy(numString, 7, 13):
        print("13")
        return False

    if not tripleDivideableBy(numString, 8, 17):
        print("17")
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
        isValid = satisfiesRequiredDivisibilityAttributes(elem)
        if isValid:
            print("candidate:", elem)
            resultSum += elem

    print("resultSum:", resultSum)

# ------------------------------------------------------------------------------

driver()

# ------------------------------------------------------------------------------
# unit test
# ------------------------------------------------------------------------------
import unittest
class Testcase(unittest.TestCase):

    def test_whatever(self):
        #self.assertEqual(36, computeAmountOfDivisors(3658732))
        pass

# --- test call
#getFirstTriangleNumberWithMoreThanXDivisors(500)
