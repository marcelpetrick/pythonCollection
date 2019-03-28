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
    # todo return the nth term of the sequence

    if(n == 1):
        return [1]

    pass

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        n = 1
        expectedOutput = [1]
        computedOutput = getPascalsTriangleRow(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample0(self):
        n = 2
        expectedOutput = [1, 1]
        computedOutput = getPascalsTriangleRow(n)
        self.assertEqual(expectedOutput, computedOutput)
