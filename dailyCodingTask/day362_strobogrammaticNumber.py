# This problem was asked by Twitter.
#
# A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees.
# For example, 16891 is strobogrammatic.
#
# Create a program that finds all strobogrammatic numbers with N digits.

# ------------------------------------------------------------------------------

# idea: TODO
# 1 is rotat-able (is this a word?) to 1
# 2 to 5?
# 6 to 9
# 8 to itself

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def isStroboGrammmatic(number):
    # todo description of the method

    if(number == 1 or number == 8 or number == 69):
        return True

    return False

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        number = 16891
        expectedOutput = True
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

    def test_expectFail(self):
        self.assertFalse(1 < 0, "hell has frozen over")

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
