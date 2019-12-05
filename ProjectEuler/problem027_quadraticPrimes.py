# Quadratic primes
#
# Problem 27
#
# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
# . However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
#
# is clearly divisible by 41.
#
# The incredible formula n2−79n+1601
# was discovered, which produces 80 primes for the consecutive values 0≤n≤79
#
# . The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
#     n2+an+b
#
# , where |a|<1000 and |b|≤1000
#
# where |n|
# is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
#
# Find the product of the coefficients, a
# and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n,
# starting with n=0.

# ------------------------------------------------------------------------------

# idea:
# TODO

# ------------------------------------------------------------------------------
import unittest
class Testcase(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(True, True)

    # def test_computeDiagonalsSum1(self):
    #     sideLength = 1
    #     expectedResult = 1
    #     output = computeDiagonalsSum(sideLength)
    #     self.assertEqual(output, expectedResult)
    #     print("sideLength", sideLength, " --> yielded result:", output)

    # def test_computeDiagonalsSum1001(self):
    #
    #     # this is the final run!
    #     sideLength = 1001
    #     import time
    #     startTime = time.time()
    #     output = computeDiagonalsSum(sideLength)
    #     print("sideLength", sideLength, " --> yielded result:", output)
    #     print("computation took:", time.time() - startTime, "s")

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
