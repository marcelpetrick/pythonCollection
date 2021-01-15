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

import sys
sys.setrecursionlimit(10**6) # todo: still needed?

dictOfDistinctPrimeFactors = dict()
def determineDistinctPrimeFactors(number, divisor):
    # first try the good old lookup
    if number in dictOfDistinctPrimeFactors:
        return dictOfDistinctPrimeFactors[number]

    # else compute
    current = number
    #print("compute for number divisor:", number, divisor)

    if current == 1:
        primeFactors = set()
    elif current % divisor == 0:
        primeFactors = determineDistinctPrimeFactors(current // divisor, divisor)
        primeFactors.add(divisor)
    else:
        primeFactors = determineDistinctPrimeFactors(current, divisor + 1)

    return primeFactors

# todo make this a unittest with the given values
print(sorted(list(determineDistinctPrimeFactors(646, 2)))) # sorted just for readability
# ------------------------------------------------------------------------------
def benchmarkTest(limit):
    import time
    startTime = time.time()

    for number in range(2, limit):
        pf = determineDistinctPrimeFactors(number, 2)
        #print(number, "->", pf)

    print("benchmarkTest took", time.time() - startTime, "s")


benchmarkTest(2 ** 12)
# old implementation:  2 ** 13: 4.2 s

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
