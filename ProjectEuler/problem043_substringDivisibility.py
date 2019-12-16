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

def tripleDivideableBy(numList, firstIndex, dividend):
    subList = numList[firstIndex:firstIndex+3]
    print("original:", numList, "firstIndex:", firstIndex, "subList:", subList)

    return int(str(subList)) // dividend == 0

print("check:", tripleDivideableBy([char for char in str(144)], 0, 12))

def satisfiesRequiredDivisibilityAttributes(number):
    numList = [char for char in str(number)]
    # to make indexing easier, I add a dummy in the beginning
    numList = ["dummy"] + numList
    print("numlist now:", numList)



satisfiesRequiredDivisibilityAttributes(123)
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
