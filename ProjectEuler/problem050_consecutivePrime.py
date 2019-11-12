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
# * implement function to compute all primes up to a certain limit
#

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def lookAndSay(n):
    return 0

# ------------------------------------------------------------------------------

# reuse code from previous solution
def getPrimesUntilLimit(limit):
    from ProjectEuler.problem668_numpy import sieveEras  # works, but just after commenting lots of code inside that file
    primes = sieveEras(limit, False) # this is also a mistake in the second parameter
    #print(len(primes), ":", primes)  # 78,498 for 10 ** 6 - which is correct

    return primes

# ------------------------------------------------------------------------------

# proper unit-test

import unittest
class Testcase(unittest.TestCase):
    def test_primeGen(self):
        expectedOutput = 78498
        computedOutput = len(getPrimesUntilLimit(10 ** 6))
        self.assertEqual(expectedOutput, computedOutput)

# ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     unittest.main()

# ------------------------------------------------------------------------------
