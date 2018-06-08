# This problem was asked by Airbnb.
#
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

import unittest

def maxSumInList(inputList):
    returnValue = 0


    return returnValue




#------------------------------------------------------------------------------

class UnivalTestcase(unittest.TestCase):
    ''' Tests for day8_countUnivalSubtrees.py '''

    def test0(self):
        input = [2, 4, 6, 2, 5]
        expectedResult = 13
        self.assertEqual(maxSumInList(input), expectedResult)

    def test1(self):
        input = [5, 1, 1, 5]
        expectedResult = 10
        self.assertEqual(maxSumInList(input), expectedResult)


#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
