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
# idea2: start with smallest number, check if divides. If true, then divide also the input and check again.
# This way a lot of "dead" numbers inbetween the prime-factors are left out.
def findLargestPrimeFactor2(input):
    manipulatedNumber = input
    lastFoundPrimeFactor = -1

    print("manipulatedNumber:", manipulatedNumber)
    while manipulatedNumber > 1:
        foundDivisor = False
        iterator = 2
        while not foundDivisor:
            if manipulatedNumber % iterator == 0:
                print(iterator, "divides", input, "without remainder: test now for prime")
                if isPrime(iterator): # todo really necessary?
                    print("is prime and divides:", iterator)
                    manipulatedNumber /= iterator
                    lastFoundPrimeFactor = iterator # save for output later :)
                    break
            iterator += 1
        print("manipulatedNumber:", manipulatedNumber)

    return lastFoundPrimeFactor

# ------------------------------------------------------------------------------

def isPrime(input):
    upperLimit = input // 2 + 1
    #print(list(range(2, upperLimit)))
    for x in range(2, upperLimit): # is -1
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
        self.assertEqual(True, isPrime(29))
        self.assertEqual(False, isPrime(87))
        self.assertEqual(True, isPrime(89))

    def test_findLargetPrimeFactor(self):
        input = 13195
        expectedResult = 29
        output = findLargestPrimeFactor(input)
        self.assertEqual(output, expectedResult)
        print(" --> input", input, "yielded result:", output)

# ------------------------------------------------------------------------------
# just my own testing
print(2, findLargestPrimeFactor(2))
print(6, findLargestPrimeFactor(6))
print(25, findLargestPrimeFactor(25))
print(87, findLargestPrimeFactor(87))

# ------------------------------------------------------------------------------

print(600851475143, findLargestPrimeFactor2(600851475143))
# result is: 6857


# project Euler-question:
#print(600851475143, findLargestPrimeFactor(600851475143))
# not really efficient!

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 3 is correct.
#
# You are the 444603rd person to have solved this problem.
#
# You have earned 1 new award:
#
# Baby Steps: Solve three problems
#
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.
