# description:
# Problem 668
#
# A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
# ah
#
# How many square root smooth numbers are there not exceeding 10000000000?

# ------------------------------------------------------------------------------

# examples: https://oeis.org/A048098 - not sure if this is the same sequence, because of the "strictly less" here in
# task and "<=" in the page

# ------------------------------------------------------------------------------

# idea: simplest version: loop for the whole range, check for each if SRS. if yes, then add up

# ------------------------------------------------------------------------------

import unittest

import math # for square root

import time

# ------------------------------------------------------------------------------

def getNumberOfSRSBelow(number):
    amount = 0
    #resultList = []
    for currentN in range(1, number + 1):
        isSRS = isSquareRootSmooth(currentN)
        #print(f"number {currentN} is", ("" if isSRS else "not"), "square root smooth")
        if(isSRS):
            amount += 1
            #resultList.append(currentN)

    #print("------------------------------------")
    #print(f"below {number} are {amount} numbers square-root-smooth")
    #print("result list: ", resultList)

    return amount + 1 # plus one for the number "1" itself, because the task-description is including it

# ------------------------------------------------------------------------------

def isSquareRootSmooth(number):
    ''' check if getBiggestPrimeFactor is smaller than the square root '''

    squareRoot = math.sqrt(number)
    biggestPrime = getBiggestPrimeFactor(number) # add some dictionary LUT for performance

    result = biggestPrime < squareRoot

    #print(f"{number} has primes {getPrimeFactors(number)} and the biggest is {biggestPrime} and the square-root "
          # f"is {squareRoot} which is",
          # "" if result else "NOT",
          # "square root smooth"
          # )

#    if result:
#        print(number)

    return result

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

    # just for the sake of the algorithm ..
    if(number == 1):
        return [1]

    primeFactors = []
    divisor = 2
    while(number > 1):
        if(number % divisor == 0):
            number = number / divisor
            primeFactors.append(divisor)
        else:
            divisor += 1

    return primeFactors

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):

    def test_getPrimeFactors(self):
        self.assertEqual([], getPrimeFactors(-1))
        self.assertEqual([1], getPrimeFactors(1))
        self.assertEqual([2], getPrimeFactors(2))
        self.assertEqual([2, 2], getPrimeFactors(4))
        self.assertEqual([2, 2, 2, 2, 2, 2, 2], getPrimeFactors(128))
        self.assertEqual([2, 3, 5, 7], getPrimeFactors(210))
        self.assertEqual([2, 2, 2, 5], getPrimeFactors(40))

    def test_getBiggestPrimeFactor(self):
        self.assertEqual(2, getBiggestPrimeFactor(2))
        self.assertEqual(5, getBiggestPrimeFactor(5))
        self.assertEqual(5, getBiggestPrimeFactor(40))
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

    def test_getNumberOfSRSBelow(self):
        '''
        Although I am not fully convinced this is the real, because of the diverting comparators
        1, 4, 8, 9, 12, 16, 18, 24, 25, 27, 30, 32, 36, 40, 45, 48, 49, 50, 54, 56,
        60, 63, 64, 70, 72, 75, 80, 81, 84, 90,
        96, 98, 100, 105, 108, 112, 120, 121, 125, 126, 128, 132, 135, 140, 144, 147, 150,
        154, 160, 162, 165, 168, 169, 175, 176, 180, 182, 189, 192, 195
        '''

        amount = getNumberOfSRSBelow(100)
        #print("below 100:", amount)
        self.assertEqual(29, amount) # TODO should be 29!

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# real task
# answer = getNumberOfSRSBelow(10000000000)
# print("below 10000000000:", answer)


#print(f"is SRS? 10.000.000.000 - {isSquareRootSmooth(10000000000)}")

# benchmark for different ranges the computation a bit. Rises quite fast: first 0s, 0s, 0s, 1s, 122s .. without optimization
for digits in range(1, 4):
    startTime = time.time()
    #print("digits:",digits)
    number = 10 ** digits
    #print("number:", number)

    print("for range up to ", number, "the amount of SRS is:", getNumberOfSRSBelow(number))
    print(f"\t computation time: {time.time() - startTime} s" )
