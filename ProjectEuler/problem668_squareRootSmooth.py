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

# improved idea:
# 0. pre-calculate the list of all primes up to sqrt(givenlimit), because we have to check against square root.
#       no full factorization needed - just check if already bigger then sqrt for SRS-ness
# 1. for given number do loop until one condition is met:
#       a. either in list with "biggest factors"
#       b. else start to factor by calling getBiggestFactor(number): and factorize with help of the prime List
#           after each step check against the existing biggestFactorList
# do this for all numbers in the range ..

# ------------------------------------------------------------------------------

import unittest

import math # for square root - TODO replace with ** 0.5 an cast to int ..

import time

# import from the current directory
#from . import PrimeClass - would not work, because is not naming a project
from ProjectEuler import PrimeClass # import from "our" project "ProjectEuler"

# ------------------------------------------------------------------------------

def getNumberOfSRSBelow_NEW(number):

    # 0. determine the root limit
    rootLimit = int(number ** 0.5) + 1
    #print("root limit:", rootLimit)

    # 1. prepare the primes list
    primeContainer = PrimeClass.PrimeClass(rootLimit) # don't use directly PrimeClass(rootLimit)! because this is seen as call
    startTimePrime = time.time()
    primeContainer.runInitialization()
    print(f"\t computation time primes: {time.time() - startTimePrime} s")

    # 2. prepare a maxFactor-dictionary
    maxFactorDict = {}

    # is the later result
    amountOfSRS = 0
    #resultList = [] # todo remove this

    startTimeSRS = time.time()
    # todo do something like: loop in 1% ranges, so that there can be some printout of each "1% turn"
    for currentN in range(2, number + 1):
        # determine the sqrt
        squareRoot = math.sqrt(currentN)
        #print(f"handle {currentN} with root {squareRoot}")

        # get the biggest prime factor
        tempNumber = currentN
        currentMaxPrime = 1
        isPrimeItself = False

        currentPrimeList = primeContainer.primeList.copy()
        #print("currentPrimeList:", currentPrimeList)
        tempDividend = currentPrimeList.pop(0) # pop the first element

        # start the finding of the biggest prime factor
        while tempNumber > 1: # no other check for the size of the primeFactorList needed
            #print("\t inner: handling now:", tempNumber, "dictionary is:", maxFactorDict)
            # check if the current number exists already precomputed
            if tempNumber in maxFactorDict:
                fromDict = maxFactorDict[tempNumber]
                currentMaxPrime = max(fromDict, currentMaxPrime)
                #print("\t\t found in dict - break")
                break
            else: # do the traditional factoring
                if currentN % tempDividend == 0:
                    currentMaxPrime = tempDividend # increase not needed, because monotonous: max(tempDividend, currentMaxPrime)
                    tempNumber = tempNumber // tempDividend
                else:
                    # if we ran out of new primes for factoriziation, then this won't be an SRS anyway!
                    if not currentPrimeList:
                        isPrimeItself = True
                        maxFactorDict[currentN] = tempNumber # insert itself to dict for caching
                        #print("\t\t must be prime - break")
                        break
                    else:
                        tempDividend = currentPrimeList.pop(0)  # pop the next element

        if not isPrimeItself:
            # insert the current finding into the dictionary: means also "overwrite" in lots of cases; possible optimization
            maxFactorDict[currentN] = currentMaxPrime

            # do now the check if SRS
            #print("\tcurrentN:", currentN, "currentMaxPrime:", currentMaxPrime, "squareRoot:", squareRoot)
            isSquareRootSmooth = currentMaxPrime < squareRoot
            if isSquareRootSmooth:
                amountOfSRS += 1
               # resultList.append(currentN)

#    print("resultList: ", resultList)
    print(f"\t computation time SRS: {time.time() - startTimeSRS} s")
    return amountOfSRS + 1 # TODO maybe do the +1 trick

# ------------------------------------------------------------------------------

def getNumberOfSRSBelow(number):
    amount = 0
    resultList = []
    for currentN in range(1, number + 1):
        isSRS = isSquareRootSmooth(currentN)
        #print(f"number {currentN} is", ("" if isSRS else "not"), "square root smooth")
        if(isSRS):
            amount += 1
            resultList.append(currentN)

    print("------------------------------------")
    print(f"below {number} are {amount} numbers square-root-smooth")
    print("result list: ", resultList)

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

# Should replace the "full" prime-factorization, which is wasting the cpu-cycles
biggestPrimeFactorCache = {}
def getChonkiestPrimeFactor(number):

    if number < 1:
        raise Exception("negative numbers have in my world no prime factors")

    # check if in cache
    if number in biggestPrimeFactorCache:
        #print("cache hit! :)")
        return biggestPrimeFactorCache[number]

    # else divide by first fitting prime and call with quotient recursively
    # TODO

    return "not implemented yet!"

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):

    # def test_getChonkiestPrimeFactor(self):
    #     self.assertEqual(2, getChonkiestPrimeFactor(2))
    #     self.assertEqual(5, getChonkiestPrimeFactor(5))
    #     self.assertEqual(5, getChonkiestPrimeFactor(40))
    #     self.assertEqual(7, getChonkiestPrimeFactor(210))
    #
    #     # for loop for the first thousand numbers
    #     self.assertEqual(max(getPrimeFactors(1234567890)), getChonkiestPrimeFactor(1234567890))

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

# # benchmark for different ranges the computation a bit. Rises quite fast: first 0s, 0s, 0s, 1s, 122s .. without optimization
# for digits in range(1, 4):
#     startTime = time.time()
#     #print("digits:",digits)
#     number = 10 ** digits
#     #print("number:", number)
#
#     print("for range up to ", number, "the amount of SRS is:", getNumberOfSRSBelow(number))
#     print(f"\t computation time: {time.time() - startTime} s" )

# new approach
#limit = 100 # leads to 29 - just like the old impl
#limit = 10000000000 # init with primes: 0.14s
#print(getNumberOfSRSBelow_NEW(limit))

# old impl for comparison
getNumberOfSRSBelow(100)

# ascending test:
for power in range(1, 1 + 1):
    print("------------")
    limit = 10 ** power
    print("limit:", limit, " -> ", getNumberOfSRSBelow_NEW(limit), "square root smooth numbers")

# ------------
# 	 computation time primes: 0.0 s
# 	 computation time SRS: 0.0 s
# limit: 10  ->  2 square root smooth numbers
# ------------
# 	 computation time primes: 0.0 s
# 	 computation time SRS: 0.0009951591491699219 s
# limit: 100  ->  29 square root smooth numbers
# ------------
# 	 computation time primes: 0.0 s
# 	 computation time SRS: 0.0019948482513427734 s
# limit: 1000  ->  274 square root smooth numbers
# ------------
# 	 computation time primes: 0.0 s
# 	 computation time SRS: 0.02293848991394043 s
# limit: 10000  ->  2656 square root smooth numbers
# ------------
# 	 computation time primes: 0.0 s
# 	 computation time SRS: 0.37200188636779785 s
# limit: 100000  ->  26613 square root smooth numbers
# ------------
# 	 computation time primes: 0.0009970664978027344 s
# 	 computation time SRS: 6.19291353225708 s
# limit: 1000000  ->  268172 square root smooth numbers
# ------------
# 	 computation time primes: 0.0019948482513427734 s
# 	 computation time SRS: 126.43314504623413 s
# limit: 10000000  ->  2719288 square root smooth numbers
# ------------
# 	 computation time primes: 0.004986763000488281 s
# .. MemoryError :/

import sys
print("max container size:", sys.maxsize)
