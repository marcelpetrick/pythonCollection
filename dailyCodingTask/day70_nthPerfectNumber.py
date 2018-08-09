# This problem was asked by Microsoft.
#
# A number is considered perfect if its digits sum up to exactly 10.
#
# Given a positive integer n, return the n-th perfect number.
#
# For example, given 1, you should return 19. Given 2, you should return 28.

import unittest

# ------------------------------------------------------------------------------

def nthPerfectNumber(input):
	pass

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test0(self):
        input = 1
        expectedResult = 19
        output = nthPerfectNumber(input)
        self.assertEqual(output, expectedResult)
        print(" --> input", input, "yielded result:", output)

    def test1(self):
        input = 2
        expectedResult = 28
        output = nthPerfectNumber(input)
        self.assertEqual(output, expectedResult)
        print(" --> input", input, "yielded result:", output)

# # ------------------------------------------------------------------------------
#
# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

