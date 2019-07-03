# description:
# Problem 668
#
# A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
# Including the number 1, there are 29 square root smooth numbers not exceeding 100.
#
# How many square root smooth numbers are there not exceeding 10000000000?

# ------------------------------------------------------------------------------

# examples: https://oeis.org/A048098

# ------------------------------------------------------------------------------

# idea: simplest version: loop for the whole range, check for each if SRS. if yes, then add up
#

# ------------------------------------------------------------------------------

import unittest

import math # for square root

# ------------------------------------------------------------------------------

def isSquareRootSmooth(number):
    ''' check if get sadfasdf is smaller than the square root'''

    squareRoot = math.sqrt(number)
    biggestPrime = getBiggestPrimeFactor(number) # add some dictionary LUT for preformance

    return biggestPrime < squareRoot

# ------------------------------------------------------------------------------

def getBiggestPrimeFactor(number):

    # check invalid values
    if(number < 1):
        raise Exception("invalid input")

    return max(getPrimeFactors(number))

# ------------------------------------------------------------------------------

def getPrimeFactors(number):

    # check invalid values
    if(number < 1):
        return []

    primeFactors = []
    divisor = 2
    while(number > 1):
        if(number % divisor == 0):
            number = number / divisor
            primeFactors.append(divisor)
        else:
            divisor += 1

    #print(primeFactors)
    return primeFactors

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):

    def test_getPrimeFactors(self):
        self.assertEqual([], getPrimeFactors(-1))
        self.assertEqual([], getPrimeFactors(1))
        self.assertEqual([2], getPrimeFactors(2))
        self.assertEqual([2, 2], getPrimeFactors(4))
        self.assertEqual([2, 2, 2, 2, 2, 2, 2], getPrimeFactors(128))
        self.assertEqual([2, 3, 5, 7], getPrimeFactors(210))

    def test_getBiggestPrimeFactor(self):
        self.assertEqual(2, getBiggestPrimeFactor(2))
        self.assertEqual(5, getBiggestPrimeFactor(5))
        self.assertEqual(7, getBiggestPrimeFactor(210))

    def test_isSquareRootSmooth(self):
        self.assertEqual(True, isSquareRootSmooth(40));
        self.assertEqual(False, isSquareRootSmooth(41));
        self.assertEqual(True, isSquareRootSmooth(45));
        self.assertEqual(True, isSquareRootSmooth(189));
        self.assertEqual(False, isSquareRootSmooth(190));
        self.assertEqual(False, isSquareRootSmooth(191));
        self.assertEqual(True, isSquareRootSmooth(192));
        self.assertEqual(True, isSquareRootSmooth(195));

# todo add more tests

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# print("result of 2:", getPrimeFactors(2))
# print("result of 20:", getPrimeFactors(20))
# print("result of 1337:", getPrimeFactors(1337))
# print("result of 32:", getPrimeFactors(32))