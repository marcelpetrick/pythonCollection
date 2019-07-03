# description:
# Problem 668
#
# A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
# Including the number 1, there are 29 square root smooth numbers not exceeding 100.
#
# How many square root smooth numbers are there not exceeding 10000000000?

# ------------------------------------------------------------------------------

# idea: TODO

# ------------------------------------------------------------------------------

import unittest

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

def isSquareRootSmooth(n):
    # todo description of the method

    if(n == 1):
        return True

    pass

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        n = 1
        expectedOutput = True
        computedOutput = isSquareRootSmooth(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_getPrimeFactors(self):
        self.assertEqual([], getPrimeFactors(-1))
        self.assertEqual([], getPrimeFactors(1))
        self.assertEqual([2], getPrimeFactors(2))
        self.assertEqual([2, 2], getPrimeFactors(4))
        self.assertEqual([2, 2, 2, 2, 2, 2, 2], getPrimeFactors(128))
        self.assertEqual([2, 3, 5, 7], getPrimeFactors(210))

# todo add more tests

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# print("result of 2:", getPrimeFactors(2))
# print("result of 20:", getPrimeFactors(20))
# print("result of 1337:", getPrimeFactors(1337))
# print("result of 32:", getPrimeFactors(32))