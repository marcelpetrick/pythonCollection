# Goldbach's other conjecture
#
# Problem 46
#
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime
# and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
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
    # task: since the list of primes is later needed anyway for the Goldbach-check, pass it as argument?
    primes = getPrimesUntilLimit(limit)
    # range 3: because 1 is not considered to be a composite number; also take stepping 2 for just "the odd ones"
    returnValue = [x for x in range(3, limit+1, 2) if x not in primes]

    return returnValue

# ------------------------------------------------------------------------------

# upperLimit = 100
# primesTillLimit = getPrimesUntilLimit(upperLimit)
# print("primesTillLimit:", primesTillLimit)
# potentialOddComposites = getPotentialOddComposites(upperLimit)
# print("potentialOddComposites:", potentialOddComposites)

# ------------------------------------------------------------------------------

# so far just with some arbitrary upper limit ... if this has to be incremented, then improve later
limitForTest = 2 ** 13 # first run had 2 ** 16, but ... can be chosen smaller ;)
def findAGoldbachConjectureViolation(limit):
    primes = getPrimesUntilLimit(limit)
    candidates = getPotentialOddComposites(limit)

    for elem in candidates:
        print("testing elem:", elem)
        for prime in primes:
            # abort if all primes until the number were tested
            if prime > elem:
                print("abort mission, because all primes up to the given number where tested:", prime, ">", elem)
                return elem # abort mission

            difference = elem - prime
            if difference % 2 == 1:
                #print("  remaining double-square is not even: difference = ", difference)
                continue

            remainingSquare = difference // 2

            if (int(remainingSquare ** 0.5) ** 2) != remainingSquare:
                #print("   not a square:", remainingSquare)
                continue

            print("  has fitting formula:", elem, " = ", prime, " + 2 * ", int(remainingSquare ** 0.5), " ^ 2")
            break # no more testing of the given candidate needed

    return -1337 # fail

# ------------------------------------------------------------------------------

import time
startTime = time.time()
violator = findAGoldbachConjectureViolation(limitForTest)
print("computation ran for", time.time() - startTime, "s")
print("result is:", violator)

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

# ..
#   has fitting formula: 5773  =  571  + 2 *  51  ^ 2
# testing elem: 5775
#   has fitting formula: 5775  =  157  + 2 *  53  ^ 2
# testing elem: 5777
# abort mission, because all primes up to the given number where tested: 5779 > 5777
# computation ran for 0.602898359298706 s
# result is: 5777
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 46 is correct.
#
# You are the 60972nd person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 25%.
