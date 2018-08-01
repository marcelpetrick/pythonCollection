# This problem was asked by Facebook.
#
# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting
# at the top-left corner and getting to the bottom-right corner. You can only move right or down.
#
# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
#
# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

import unittest

# ------------------------------------------------------------------------------

def computeWaysToMove(m, n):
    '''
    :param m - one side of the matrix
    :param m - other side of the matrix
    '''
    print("computeWaysToMove called with: ", m, n)
    returnValue = None

    # TODO

    return returnValue

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test0(self):
        m, n = 2,2
        expectedResult = 2
        output = computeWaysToMove(m, n)
        self.assertEqual(output, expectedResult)
        print(" --> input", m, "x", n, "yielded result:", output)

# # ------------------------------------------------------------------------------
#
# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
