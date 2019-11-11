# Amicable numbers
#
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

# idea:
# * do for all numbers in the range: find all divisors (list) and compute sum
# * then sort them into buckets where the sum is the key
# * if one bucket has more than one entry, then that
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

#import time
import unittest

# ------------------------------------------------------------------------------

def sumOfProperDivisors(number):
    return sum(computeProperDivisors(number))

# ------------------------------------------------------------------------------

def computeProperDivisors(number):
    if number <= 0:
        raise ValueError("Only positive integers bigger than zero are allowed.")

    properDivisors = set()
    for divisor in range(1, number):
        dividend, modulo = divmod(number, divisor)

        if modulo == 0:
            properDivisors.add(divisor)
            properDivisors.add(dividend) # save one call

        # since the task requires that the number itself is not part of the returned values, remove it
        if number in properDivisors:
            properDivisors.remove(number)

    return properDivisors

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExampleOfProperDivisors0(self):
        n = 220
        expectedOutput = {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}
        computedOutput = computeProperDivisors(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExampleOfProperDivisors1(self):
        n = 284
        expectedOutput = {1, 2, 4, 71, 142}
        computedOutput = computeProperDivisors(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_sumOfProperDivisors0(self):
        n = 220
        expectedOutput = 284
        computedOutput = sumOfProperDivisors(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_sumOfProperDivisors1(self):
        n = 284
        expectedOutput = 220
        computedOutput = sumOfProperDivisors(n)
        self.assertEqual(expectedOutput, computedOutput)

# ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     unittest.main()

# --- test call ---
# def driver(number):
#     print(number, "-->", computeProperDivisors(number), "-->", sumOfProperDivisors(number))
#
# driver(220)
# driver(284)

print("###############################")

def computeAmicableNumbersBelowN(limit):
    amis = set()
    for numberToTest in range(2, limit):

        # prevent double checks
        if numberToTest in amis:
            continue

        ami = sumOfProperDivisors(numberToTest)
        #print(numberToTest, "-->", ami)

        if sumOfProperDivisors(ami) == numberToTest and ami != numberToTest:
            amis.add(numberToTest)
            amis.add(ami)
            print("found:", numberToTest, "-->", ami, "(ami)")

    return amis

# amis = computeAmicableNumbersBelowN(100)
# print("amis:", amis)

amis = computeAmicableNumbersBelowN(10000)
print("amis:", amis, "sum of amis:", sum(amis))

# ------------------------------------------------------------------------------
# found: 220 --> 284 (ami)
# found: 1184 --> 1210 (ami)
# found: 2620 --> 2924 (ami)
# found: 5020 --> 5564 (ami)
# found: 6232 --> 6368 (ami)
# amis: {1184, 6368, 5564, 5020, 2924, 284, 6232, 1210, 220, 2620} sum of amis: 31626
#
# Process finished with exit code 0
# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 21 is correct.
#
# You are the 135617th person to have solved this problem.
#
# You have earned 1 new award:
#
#     Easy Prey: Solve twenty-five of the fifty easiest problems
