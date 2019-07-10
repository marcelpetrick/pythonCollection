# description:
# Problem 668
#
# A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
# Including the number 1, there are 29 square root smooth numbers not exceeding 100.
#
# How many square root smooth numbers are there not exceeding 10000000000?

# ------------------------------------------------------------------------------

# idea:
# * improved version with new algorithm, since the computational complexity for the previous version for
#   numbers > 10**7 was too high

# new algorithm (based on recommendations from https://github.com/ScytheMax ):
#   * pre-compute primes up to limit
#   * for each prime p: remove all multiples of p (up to p) from the list of possible numbers
#   * summarize the remaining amount of SRS
#
#   // according https://github.com/ScytheMax -- the idea is:
#   // let p be a prim number. then follows p is not srs.
#   // because pp bigger p.
#   // the it follows for every natural number m with m lesser or equal p:
#   // pm is not a srs. because p is the highest prim factor in pm. so it follows pp bigger or equal pm.

#   // with this knowledge.
#   // 1. calc all primes until limit.
#   // 2. filter out all non srs. take every prim p until limit. and filter out all numbers pm for m lesser equal p.
#
# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def getNumberOfSRSBelow(number):
    amount = 0
    resultList = []

    # TODO implement this

    print("------------------------------------")
    print(f"below {number} are {amount} numbers square-root-smooth")
    print("result list: ", resultList)

    return amount + 1 # plus one for the number "1" itself, because the task-description is including it

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):

    def test_getNumberOfSRSBelow(self):
        '''
        Although I am not fully convinced this is the real, because of the diverting comparators
        1, 4, 8, 9, 12, 16, 18, 24, 25, 27, 30, 32, 36, 40, 45, 48, 49, 50, 54, 56,
        60, 63, 64, 70, 72, 75, 80, 81, 84, 90,
        96, 98, 100, 105, 108, 112, 120, 121, 125, 126, 128, 132, 135, 140, 144, 147, 150,
        154, 160, 162, 165, 168, 169, 175, 176, 180, 182, 189, 192, 195
        '''

        amount = getNumberOfSRSBelow(100)
        self.assertEqual(29, amount) # TODO should be 29! 28 SRS and +1 (because we don't know ..)

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# ascending test:
for power in range(1, 1 + 1): # change the second to 10
    print("------------")
    limit = 10 ** power
    print("limit:", limit, " -> ", getNumberOfSRSBelow(limit), "square root smooth numbers")

# just to check if there is a 64 bit Python running
import sys
print("max container size:", sys.maxsize)
