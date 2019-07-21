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
    isPrimeArray = np.full(limit, True, dtype = bool)
    #print("before:", isPrimeArray)

    # zero and one are by definition no prime
    isPrimeArray[0] = False
    isPrimeArray[1] = False

    index = 0
    #print("going up to:", range(int(limit ** 0.5)))
    for index in range(int(limit ** 0.5) + 1):
        #print("handling:", index)
        if isPrimeArray[index] == False:
            continue
        else:
            multiple = 2
            while index * multiple < limit:
                isPrimeArray[index * multiple] = False
                multiple += 1

        #print("\tnow:", isPrimeArray)

    # map to numbers
    resultList = []
    for i in range(limit):
        if isPrimeArray[i] == True:
            resultList.append(i)

    return resultList

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):

    def test_sieveEras10(self):
        limit = 10
        result = sieveEras(limit)
        #print("computed primes until", limit, " --> ", result)

        expectedPrimes = [2,3,5,7]
        self.assertEqual(expectedPrimes, result)

    def test_sieveEras100(self):
        limit = 100
        result = sieveEras(limit)
        #print("computed primes until", limit, " --> ", result)

        expectedPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(expectedPrimes, result)

    def test_sieveEras1000(self):
        limit = 1000
        result = sieveEras(limit)
        #print("computed primes until", limit, " --> ", result)

        expectedPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        self.assertEqual(expectedPrimes, result)

# ---- here comes the execution of the unit-tests ----

if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
# import time
# print("###############")
# for i in range(2, 6 + 1):
#     startTime = time.time()
#     print("how many primes in 10 ^", i, "?", len(sieveEras(10 ** i)), "in", time.time() - startTime, "s")
