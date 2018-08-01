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

    # todo prevent nonsense for wrong input, like negative numbers

    # positions get enumerated with 1..n - not starting with 0
    returnValue = computeWaysToMoveWithPosition(m, n, 1, 1) # start at top-left

    return returnValue

def computeWaysToMoveWithPosition(m, n, x, y):
    ''' helper with current position '''
    returnValue = None

    # compute the amount of possible solutions for both possible ways (horizontal and vertical) recursively; sum them up
    if x < m:
        horizontalSolutions = 1 + computeWaysToMoveWithPosition(m, n, x+1, y)
    else:
        horizontalSolutions = 0

    if y < n:
        verticalSolutions = 1 + computeWaysToMoveWithPosition(m, n, x, y+1)
    else:
        verticalSolutions = 0

    returnValue = horizontalSolutions + verticalSolutions

    print("computeWaysToMoveWithPosition called with: ", m, n, x, y, "and will return:", returnValue)
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
