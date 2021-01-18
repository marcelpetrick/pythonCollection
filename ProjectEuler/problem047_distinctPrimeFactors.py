# Distinct primes factors
#
# Problem 47
#
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

# ------------------------------------------------------------------------------
# idea:
# * todo [..] yeah, this is what happens when you implement on the fly and then it does NOT work!
# * it looks like primefactors of higher power are counted as "different": see the given example for 3: 644 and 646 both
# share the prime factor 2, but first has power of two, the other of one -> this attribute  could be the reason the current
# program returns a non-accepted value (I don't want to call it: wrong)
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# reuse code from previous solution: will require the existing numpy!
# TODO maybe consider to use a prime-generator, which is proven and tested; see problem041
def getPrimesUntilLimit(limit):
    from ProjectEuler.problem668_numpy import sieveEras  # works, but just after commenting lots of code inside that file
    primes = sieveEras(limit, False) # this is also a mistake in the second parameter
    #print(len(primes), ":", primes)  # 78,498 for 10 ** 6 - which is correct
    return primes

hardCodedPrimeList = getPrimesUntilLimit(666666) # is 100k really enough? with all four-digit number? doubt it
# ------------------------------------------------------------------------------

# kept the pure function - should be put into a nice, nice library later
def computePrimeFactors(number):
    #primeFactorLimit = int(number ** 0.5) + 1
    #print("number", number, "primeFactorLimit:", primeFactorLimit)

    #primeList = getPrimesUntilLimit(primeFactorLimit)

    primeFactors = []

    rest = number
    for elem in hardCodedPrimeList:
        while rest % elem == 0:
            primeFactors.append(elem)
            rest = rest // elem
        if rest == 1:
            break

    # add the rest if it was not one, because then this is a prime as well!
    if rest != 1:
        primeFactors.append(rest)

    #print("number", number, "primeFactors:", primeFactors)
    return primeFactors

# ------------------------------------------------------------------------------

def computePrimeFactorsCombined(number):
    ''' idea: instead of 12 = 2*3*3 return: 4*3,
        means: combine all identical prime factors into one number
    '''

    primeFactors = []

    rest = number
    for elem in hardCodedPrimeList:
        power = 0
        while rest % elem == 0:
            power = power + 1
            rest = rest // elem
        if power > 0:
            primeFactors.append(elem ** power)
        if rest == 1:
            break

    return primeFactors

# ------------------------------------------------------------------------------

# # todo make this a unittest with the given values
# print(sorted(list(determineDistinctPrimeFactors(646, 2)))) # sorted just for readability
# ------------------------------------------------------------------------------

def findFourConsecutiveIntegers():

    number = 1
    increaseUntilInfinity = True
    while increaseUntilInfinity:
        pf0 = computePrimeFactorsCombined(number + 0)

        if len(pf0) == 4:
            pf1 = computePrimeFactorsCombined(number + 1)

            if len(pf1) == 4:
                pf2 = computePrimeFactorsCombined(number + 2)

                if len(pf2) == 4:
                    pf3 = computePrimeFactorsCombined(number + 3)

                    if len(pf3) == 4:
                        print("found one:")
                        print("  ", number + 0, "->", pf0)
                        print("  ", number + 1, "->", pf1)
                        print("  ", number + 2, "->", pf2)
                        print("  ", number + 3, "->", pf3)

                        # todo continue here .. compare if they are distinct
                        combinedSet = set()
                        combinedSet.update(pf0)
                        combinedSet.update(pf1)
                        combinedSet.update(pf2)
                        combinedSet.update(pf3)
                        print("combinedSet:", combinedSet)
                        print("has length:", len(combinedSet))

                        if len(combinedSet) == 16:
                            print("we have matched the conditions")
                            increaseUntilInfinity = False

        number-=-1

    print("the wanted number is:", number)

# ------------------------------------------------------------------------------

findFourConsecutiveIntegers()

# ------------------------------------------------------------------------------

# found one:
#    23373 -> {53, 3, 21, 7}
#    23374 -> {2, 29, 13, 31}
#    23375 -> {17, 11, 5, 25}
#    23376 -> {2, 3, 4, 487}
#
# Process finished with exit code -1

# ------------------------------------------------------------------------------

# last run:
# [2, 17, 19]
#
# Process finished with exit code -1073741571 (0xC00000FD)
# stack overflow says: "Simple as that, you are getting a stack overflow.", xD

# ------------------------------------------------------------------------------

import unittest
class Testcase(unittest.TestCase):
    def test_computePrimeFactors(self):
        self.assertEqual([7,191], computePrimeFactors(1337))
        self.assertEqual([2,2,2,2], computePrimeFactors(16))
        self.assertEqual([2,2,7,23], computePrimeFactors(644))
        self.assertEqual([3,5,43], computePrimeFactors(645))
        self.assertEqual([2,17,19], computePrimeFactors(646))

        # from the task itself:
        # 644 = 2² × 7 × 23
        # 645 = 3 × 5 × 43
        # 646 = 2 × 17 × 19.

    def test_computePrimeFactorsCombined(self):
        self.assertEqual([7, 191], computePrimeFactorsCombined(1337))
        self.assertEqual([16], computePrimeFactorsCombined(16))
        self.assertEqual([4, 7, 23], computePrimeFactorsCombined(644))
        self.assertEqual([3, 5, 43], computePrimeFactorsCombined(645))
        self.assertEqual([2, 17, 19], computePrimeFactorsCombined(646))

    def test_benchmark(self):
        import time
        startTime = time.time()
#
        limit = 2 ** 14
        for number in range(2, limit):
            # pf = determineDistinctPrimeFactors(number, 2)
            pf = computePrimeFactors(number)
            # print(number, "->", pf)

        print("benchmarkTest took", time.time() - startTime, "s")

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
# ------------------------------------------------------------------------------

# C:\Users\MarcelP\Desktop\MarcelsFolder\coding\pythonCollection\venv\Scripts\python.exe C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/ProjectEuler/problem047_distinctPrimeFactors.py
# found one:
#    134043 -> [3, 7, 13, 491]
#    134044 -> [4, 23, 31, 47]
#    134045 -> [5, 17, 19, 83]
#    134046 -> [2, 9, 11, 677]
# combinedSet: {2, 3, 4, 5, 677, 7, 9, 491, 11, 13, 47, 17, 19, 83, 23, 31}
# has length: 16
# we have matched the conditions
# the wanted number is: 134044
# benchmarkTest took 0.17865967750549316 s
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.179s
#
# OK
#
# Process finished with exit code 0

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 47 is correct.
#
# You are the 57440th person to have solved this problem.
#
# You have earned 1 new award:
#
#     Flawless Fifty: Solve fifty consecutive problems
#
#
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 25%.