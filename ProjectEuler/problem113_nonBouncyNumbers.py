# Non-bouncy numbers
#
# Problem 113
# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
# for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below
# one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.
#
# How many numbers below a googol (10100) are not bouncy?

# ------------------------------------------------------------------------------

# idea:
# * dont solve it like problem 112; instead use an iterative approach over the lenght of the string (number string, just 100 digits)
# for each string (starting string) find the fitting follow up numbers (equal or bigger). recursive approach? check how long this would take
#

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def determineFollowupNumbers(currentChar):
    currentNumber = int(currentChar)

    returnList = list(range(currentNumber, 10))  # from the current number, because increasing = "equal or higher"

    return returnList

# ------------------------------------------------------------------------------

def computeAllIncreasingNumbersUpToLimit_recursiveApproach_(limit):
    initialString = "0"
    # todo maybe think about the start ... because empty string would be better

    # determine all follow up numbers (increasing -> just those bigger than last digit)

    # collect the result-strings (list?) and combine with current string?
    pass

# ------------------------------------------------------------------------------
import unittest

class Testcase(unittest.TestCase):

    def test_determineFollowupNumbers(self):

        # given input from Project Euler itself
        self.assertEqual([9], determineFollowupNumbers("9"))
        self.assertEqual([8, 9], determineFollowupNumbers("8"))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], determineFollowupNumbers("0"))

    # def test_determineAmountOfBouncyNumbersBelowLimit(self):
    #     # given input from Project Euler itself
    #     self.assertEqual(525, determineAmountOfBouncyNumbersBelowLimit(1000))
    #
    # def test_percentage(self):
    #     self.assertEqual(538, findNumberWhereBouncyNumbersReachGivenPercentageFirst(50))
    #     self.assertEqual(21780, findNumberWhereBouncyNumbersReachGivenPercentageFirst(90))
    #
    # def test_createSolution(self):
    #     import time
    #     startTime = time.time()
    #     print("solution: 99 percent bouncyness is reached at number:", findNumberWhereBouncyNumbersReachGivenPercentageFirst(99))
    #     print("calculation took", time.time() - startTime, "s")

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------