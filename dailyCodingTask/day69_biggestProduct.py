# This problem was asked by Facebook.
#
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.

# my idea: go once throught the whole list, check each element with container.
# that container saves the two smallest negative numbers and the three biggest.
# afterwards: choose wisely ;)

import unittest

# ------------------------------------------------------------------------------

def biggestProduct(inputList):
    print("biggestProduct called with: ", inputList)
    returnValue = None

    return returnValue

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test0(self):
        inputList = [-10, -10, 5, 2]
        expectedResult = 500
        output = biggestProduct(inputList)
        self.assertEqual(output, expectedResult)
        print(" --> input", inputList, "yielded result:", output)


# # ------------------------------------------------------------------------------
#
# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
