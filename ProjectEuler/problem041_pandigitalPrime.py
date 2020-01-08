# Pandigital prime
#
# Problem 41
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# ------------------------------------------------------------------------------
# idea:
# * it is clear that a number with 9 digits is the biggest pandigital number,
# * searching from 10**9 -1 downwards inside all primes, check if it is n-pandigital
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def isPandigital(number):
    ''' An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. '''
    stringified = str(number)
    length = len(stringified)

    if length > 9:
        return False

    for i in range(1, length + 1):
        # print(i)
        if str(i) not in stringified:
            return False

    return True

# ------------------------------------------------------------------------------

def checkAllPrimesWith9DigitsForPandigitalityDescending():
    print("---------------")
    # instead of relying again on another self-implementation of prime-generator, just try this library
    import sympy
    import time

    startTime = time.time()
    digits = 9
    #primesWith9Digits = list(sympy.primerange(10 ** digits, 10 ** (digits + 1)))
    #print(time.time() - startTime, "s:", "primesWith9Digits:", len(primesWith9Digits), primesWith9Digits)

    number = 10 ** 10 - 1
    while True:
        if sympy.isprime(number):
            #print(number,"is prime .. check now pandigitality")
            if isPandigital(number):
                print("is also pandigital! :)")
                break
        number -= 2

    print(number," is the wanted one: computation took", time.time() - startTime, "s")

# test call
checkAllPrimesWith9DigitsForPandigitalityDescending()

# ------------------------------------------------------------------------------
import unittest
import logging  # needed for unit-test-logging
import sys  # needed for unit-test-logging

class Testcase(unittest.TestCase):

    def test_isPandigital(self):
        pass
        self.assertEqual(True, isPandigital(1))
        self.assertEqual(True, isPandigital(12))
        self.assertEqual(True, isPandigital(321))
        self.assertEqual(True, isPandigital(2143)) # given example
        self.assertEqual(True, isPandigital(987654321))
        self.assertEqual(False, isPandigital(11))
        self.assertEqual(False, isPandigital(10))
        self.assertEqual(False, isPandigital(9876543210))

# ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#     unittest.main()

# ------------------------------------------------------------------------------
