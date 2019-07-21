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
import time
import numpy as np
#from ProjectEuler import PrimeClass # import from "our" project "ProjectEuler"

# ------------------------------------------------------------------------------

def getNumberOfSRSBelow(limit):
    amount = 0
    #resultList = []

    # 0. determine the root limit
    #rootLimit = int(limit ** 0.5) + 1
    #print("root limit:", rootLimit)

    # 1. prepare the primes list
    startTimePrime = time.time()
    primesList = [True] * limit # create a list with 10 times True
    primesList[0] = False  # 0 is not a prime!
    primesList[1] = False # 1 is not a prime!
    #print("primesList:", primesList)

    # sieve of Erastothenes
    # TODO build in to do the sieving only if the current pos is True
    for number in range(2, limit): # question: could it be that this has to be run only up to half of the limit?1? because the remaining part is already sieved?
        if primesList[number] == False:
            continue
        #print("handling number:", number)
        multiple = 2
        pos = multiple * number

        while pos < limit:
            #print("\thandling multiple:", pos)
            primesList[pos] = False
            multiple += 1
            pos = multiple * number

        #print("primesList after priming:", primesList, " => ", sum(primesList))

    #print("primesList after priming:", primesList, " => ", sum(primesList))
    print("number of primes below", limit, " => ", sum(primesList))
    # output: number of primes below 10000  =>  1229
    print(f"\t computation time primes: {time.time() - startTimePrime} s")

    # TODO implement this

#    print("------------------------------------")
#    print(f"below {limit} are {amount} (true) numbers square-root-smooth")
#    print("result list: ", resultList)

    return amount + 1 # plus one for the number "1" itself, because the task-description is including it

# ------------------------------------------------------------------------------

def sieveEras(limit):
    bitArray = np.full(limit, True, dtype = bool)
    print("before:", bitArray)

    # zero and one are by definition no prime
    bitArray[0] = False
    bitArray[1] = False
    

    return bitArray

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):

    def test_sieveEras(self):
        limit = 10
        result = sieveEras(limit)
        print("computed primes until", limit, " --> ", result)

        expectedPrimes = [2,3,5,7] #,11,13,17]

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
