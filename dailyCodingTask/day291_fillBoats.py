# description:
# This problem was asked by Glassdoor.
#
# An imminent hurricane threatens the coastal town of Codeville.
# If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k,
# determine how many boats will be needed to save everyone.
#
# For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest
# number of boats required will be three.
# ------------------------------------------------------------------------------

# idea: TODO

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def fillBoats(givenList, maxAllowedWeight):
    # todo description of the method

    pass

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        list = {1, 1, 2}
        maxWeight = 2
        expectedOutput = 2
        computedOutput = fillBoats(list, maxWeight)
        self.assertEqual(expectedOutput, computedOutput)

    def test_expectFail(self):
        self.assertFalse(1 < 0, "hell has frozen over")

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
