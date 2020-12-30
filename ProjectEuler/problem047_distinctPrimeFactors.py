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
# * todo
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def determineDistinctPrimeFactors(number):
    resultList = []
    resultList.append(2)
    return resultList

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

findFourConsecutiveIntegers()
