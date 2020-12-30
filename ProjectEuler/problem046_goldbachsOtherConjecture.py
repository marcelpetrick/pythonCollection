# Goldbach's other conjecture
#
# Problem 46
#
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime
# and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# ------------------------------------------------------------------------------
# idea: (naive)
# * composite numbers are the "non-prime" numbers
# * in this case even just the odd ones ..
# * generate a list (or generator) of those by pre-computing the primes until a certain limit, then taking the
#   "inverse", then filtering by oddness?
#
# * goldbach-check: create the difference of "number to test" and "loop up to the prime below number to check":
# ** then divide the difference by two: and the resulting number shall be a square.
# ** at least once this shall be true then -> then the conjecture would be true
#
# * go upwards to find the first number, which does not fulfill it
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

# ------------------------------------------------------------------------------

def getPotentialOddComposites(limit):
    primes = getPrimesUntilLimit(limit)
    # range 3: because 1 is not considered to be a composite number
    returnValue = [x for x in range(3, limit+1, 2) if x not in primes]

    return returnValue

# ------------------------------------------------------------------------------

upperLimit = 100
primesTillLimit = getPrimesUntilLimit(upperLimit)
print("primesTillLimit:", primesTillLimit)
potentialOddComposites = getPotentialOddComposites(upperLimit)
print("potentialOddComposites:", potentialOddComposites)

# ------------------------------------------------------------------------------

import unittest

class Testcase(unittest.TestCase):
    def test_getPotentialOddComposites(self):
        OEIS_list_to150 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36,
                           38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66,
                           68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95,
                           96, 98, 99, 100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120,
                           121, 122, 123, 124, 125, 126, 128, 129, 130, 132, 133, 134, 135, 136, 138, 140, 141, 142,
                           143, 144, 145, 146, 147, 148, 150] # see: https://en.wikipedia.org/wiki/Composite_number
        oddlyFilteredOEIS = [x for x in OEIS_list_to150 if x % 2 == 1]
        #print("oddlyFilteredOEIS:", oddlyFilteredOEIS)
        self.assertEqual(oddlyFilteredOEIS, getPotentialOddComposites(150))

    def test_givenPotentialOdds(self):
        givenList = [9, 15, 21, 25, 27, 33]
        self.assertEqual(givenList, getPotentialOddComposites(34))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
   unittest.main()

# ------------------------------------------------------------------------------