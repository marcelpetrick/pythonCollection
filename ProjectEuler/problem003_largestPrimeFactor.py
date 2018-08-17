# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# ------------------------------------------------------------------------------
import unittest

# idea:
# (of course, not the most efficient way to fix it) decrease the number of the input to find a fitting divisor
# (% == 0), then check if this is prime
def findLargestPrimeFactor(input):
    for decreasingValue in range(input, 1, -1):
        if input % decreasingValue == 0:
            #print(decreasingValue, "divides", input, "without remainder: test now for prime")
            if isPrime(decreasingValue):
                #print("is prime - nice :) return this")
                return decreasingValue

    return -1 # error

# ------------------------------------------------------------------------------

def isPrime(input):
    for x in range(2, input): # is -1
        #print("input:", input, "test:", x)
        if input % x == 0:
            #print("is dividing!")
            return False
    # else we have a prime if we reached this
    return True

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(True, isPrime(2))
        self.assertEqual(True, isPrime(3))
        self.assertEqual(False, isPrime(6))
        self.assertEqual(True, isPrime(7))
        self.assertEqual(False, isPrime(16))
        self.assertEqual(False, isPrime(25))
        self.assertEqual(True, isPrime(29)) # true?
        self.assertEqual(False, isPrime(87))  # true?
        self.assertEqual(True, isPrime(89))  # true?

    def test_findLargetPrimeFactor(self):
        input = 13195
        expectedResult = 29
        output = findLargestPrimeFactor(input)
        self.assertEqual(output, expectedResult)
        print(" --> input", input, "yielded result:", output)


print(2, findLargestPrimeFactor(2))
print(6, findLargestPrimeFactor(6))
print(25, findLargestPrimeFactor(25))
print(87, findLargestPrimeFactor(87))
