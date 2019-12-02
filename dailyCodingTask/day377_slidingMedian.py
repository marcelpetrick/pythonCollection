# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given an array of numbers arr and a window of size k, print out the median of each window of size k starting from the left and moving right by one position each time.
#
# For example, given the following array and k = 3:
#
# [-1, 5, 13, 8, 2, 3, 3, 1]
# Your function should print out the following:
#
# 5 <- median of [-1, 5, 13]
# 8 <- median of [5, 13, 8]
# 8 <- median of [13, 8, 2]
# 3 <- median of [8, 2, 3]
# 3 <- median of [2, 3, 3]
# 3 <- median of [3, 3, 1]
# Recall that the median of an even-sized list is the average of the two middle numbers.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def slidingMedian(inputList, k):
    ''' will return a list of strings '''

    return []

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_givenExample(self):
        givenInput = [-1, 5, 13, 8, 2, 3, 3, 1]
        givenK = 3
        expectedOutput = ["5 <- median of [-1, 5, 13]",
"8 <- median of [5, 13, 8]",
"8 <- median of [13, 8, 2]",
"3 <- median of [8, 2, 3]",
"3 <- median of [2, 3, 3]",
"3 <- median of [3, 3, 1]"
                          ]
        self.assertEqual(expectedOutput, slidingMedian(givenInput, givenK))

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
