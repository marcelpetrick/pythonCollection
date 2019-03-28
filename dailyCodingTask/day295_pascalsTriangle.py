# description:
# This problem was asked by Stitch Fix.
#
# Pascal's triangle is a triangular array of integers constructed with the following formula:
#
#     The first row consists of the number 1.
#     For each subsequent row, each element is the sum of the numbers directly above it, on either side.
#
# For example, here are the first few rows:
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#
# Given an input k, return the kth row of Pascal's triangle.
#
# Bonus: Can you do this using only O(k) space?

# ------------------------------------------------------------------------------

# idea: after thinking about this during a nice walk with my daughter I determined a quite nice algorithm
# - create an array[n] filled with 0, except the last entry (array[n-1] = 0)
# - while( array[0] != 0) do:
#       loop over the whole array (except very last item): // because last item of the row is always 1
#          array[n] = array[n] = array[n+1]
#
# .. done .. :)

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def getPascalsTriangleRow(n):
    # Return the n-th row of the Pascal's Triangle

    if n <= 0:
        raise ValueError("Pascal's Triangle only defined for integer values bigger 0")

    # create the array
    pascalsRow = [0] * n

    # fill last item with 1
    pascalsRow[n - 1] = 1
    #print("current state:")
    #print(pascalsRow)

    while pascalsRow[0] == 0:
        #print("current state - in loop:")
        #print(pascalsRow)
        for index in range(0, n - 1): # exclusive last!
            #print("index:" + str(index))
            pascalsRow[index] = pascalsRow[index] + pascalsRow[index + 1]

    return pascalsRow

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample1(self):
        n = 1
        expectedOutput = [1]
        computedOutput = getPascalsTriangleRow(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample2(self):
        n = 2
        expectedOutput = [1, 1]
        computedOutput = getPascalsTriangleRow(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample5(self):
        n = 5
        expectedOutput = [1, 4, 6, 4, 1]
        computedOutput = getPascalsTriangleRow(n)
        self.assertEqual(expectedOutput, computedOutput)

    # TODO add a test which checks for the thrown exception
    def test_exceptionThrowing(self):
        self.assertRaises(ValueError, getPascalsTriangleRow, -1337)

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
# direct call:
print("pascal's row " + str(20) + ": " + str(getPascalsTriangleRow(20)))
