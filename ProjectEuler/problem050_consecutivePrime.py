# Consecutive prime sum
#
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# ------------------------------------------------------------------------------

# idea:
# TODO

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------

# proper unit-test

import unittest
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        n = 1
        expectedOutput = 1
        computedOutput = lookAndSay(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_expectFail(self):
        self.assertFalse(1 < 0, "hell has frozen over")

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
