# This problem was asked by Facebook.
#
# Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed
# using elements from L.
#
# For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.

# ------------------------------------------------------------------------------

def longestConsecutiveSequence(inputList):
    if len(inputList) == 0:
        raise ValueError("wrong input, just a list please")

    return 1 # todo

# ------------------------------------------------------------------------------
# proper unit-test
import unittest
class Testcase(unittest.TestCase):
    def test_givenExample(self):
        giveInput = [5, 2, 99, 3, 4, 1, 100]
        expectedOutput = 5
        computedOutput = longestConsecutiveSequence(giveInput)
        self.assertEqual(expectedOutput, computedOutput)

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
