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

hardCodedPrimeList = getPrimesUntilLimit(10 ** 5) # is 100k really enough? with all four-digit number? doubt it
# ------------------------------------------------------------------------------

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

# # todo make this a unittest with the given values
# print(sorted(list(determineDistinctPrimeFactors(646, 2)))) # sorted just for readability
# ------------------------------------------------------------------------------

def findFourConsecutiveIntegers():

    number = 1
    while True:
        pf0 = determineDistinctPrimeFactors(number + 0)

        if len(pf0) == 4:
            pf1 = determineDistinctPrimeFactors(number + 1)

            if len(pf1) == 4:
                pf2 = determineDistinctPrimeFactors(number + 2)

                if len(pf2) == 4:
                    pf3 = determineDistinctPrimeFactors(number + 3)

                    if len(pf3) == 4:
                        print("found one:")
                        print("  ", number + 0, "->", pf0)
                        print("  ", number + 1, "->", pf1)
                        print("  ", number + 2, "->", pf2)
                        print("  ", number + 3, "->", pf3)

                        # todo continue here ..

        number-=-1

# ------------------------------------------------------------------------------

#findFourConsecutiveIntegers()

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
