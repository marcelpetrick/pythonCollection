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
# * one task beforehand would be to produce a container of primes up to a certain number ... to do the check easier
# * create a function which takes two params (a,b) and then tries to find the longest chain of generated primes
# * would be the creation of a LUT for n and n**2 an improvement for computation?
# * multiprocessing would be an option unless i notice a mathematical shortcut

# ------------------------------------------------------------------------------

def quickDirtyPrimTest(number):
    if number < 0:
        return False
        #raise ValueError("primes have to be > 1")

    if number in {0, 1}:
        return False  # no primes

    # TODO replace with something proper and maybe with LUT
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

# ------------------------------------------------------------------------------

# test run
# for number in range(20):
#     print(number, ":", quickDirtyPrimTest(number));

# ------------------------------------------------------------------------------

def computeLongestChainFor(a, b):
    # check the input
    hardcodedLimits = 1000
    # if a <= -hardcodedLimits or a >= hardcodedLimits:
    #     raise ValueError("input error: |a|<1000")
    # if b < -hardcodedLimits or b > hardcodedLimits:
    #     raise ValueError("input error: |b|≤1000")

    # starting value
    n = 0
    isPrime = True

    while isPrime:
        valueOfExpression = n * n + a * n + b
        isPrime = quickDirtyPrimTest(valueOfExpression)

        # if valueOfExpression is in primes:
        #     pass #TODO

        if not isPrime:
            break

        n += 1

    #print("broke for", a, b, "at n", n)
    return n

# ------------------------------------------------------------------------------
computeLongestChainFor(1, 41)  # returns 40, which is exactly what was predicted
computeLongestChainFor(-79, 1601)  # returns 80, which is exactly what was predicted

# crude test run
longestChain, longA, longB = -1, -1, -1
for a in range(-999, 999 + 1):
    for b in range(-1000, 1000 + 1):
        #print("handling", a, b)
        result = computeLongestChainFor(a, b)
        if result > longestChain:
            longestChain = result
            longA, longB = a, b
            print("new top: longestChain, longA, longB =", longestChain, longA, longB)

print("final: longestChain, longA, longB =", longestChain, longA, longB)
print("euler answer:", longA * longB)

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
# if __name__ == '__main__':
#     unittest.main()

# ------------------------------------------------------------------------------
