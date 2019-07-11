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

        return

        #limit = 100 # 10000000000
        #amount = getNumberOfSRSBelow(limit)
        ##self.assertEqual(29, amount) # TODO should be 29! 28 SRS and +1

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# # ascending test:
for power in range(1, 10 + 1): # change the second limit to 10
    print("--------------------------------")
    limit = 10 ** power
    print("limit:", limit, " -> ", getNumberOfSRSBelow(limit), "square root smooth numbers")
#
# # just to check if there is a 64 bit Python running
# import sys
# print("max container size:", sys.maxsize)
#
#
# # test multiprocessing
# # from: https://www.machinelearningplus.com/python/parallel-processing-python/
# # also check this: https://medium.com/@mjschillawski/quick-and-easy-parallelization-in-python-32cb9027e490
# # or this: http://www.nickstricks.net/wp/2016/03/01/quick-parallelism-in-python/
# import multiprocessing as mp
# print("cpu count:", mp.cpu_count())

# for verification: -> 5761455
# https://www.wolframalpha.com/input/?i=number+of+primes+below+100000000&wal=header
#number of primes below 100000000  =>  5761455
#	 computation time primes: 50.28856682777405 s

# scaling
#100.000.000 50s
#1.000.000.000 500 -> 8 min 20 seconds
#10.000.000.000 5000s -> 1h 23 min 20 seconds

# memory: 10 * 10**9 * 24 byte for [Boolean] -> 30 GiByte -> not fitting,
# will run into MemoryError on the current system with 32 GiByte RAM

# unchanged runtimes:
# number of primes below 10  =>  4
# 	 computation time primes: 0.0 s
# number of primes below 100  =>  25
# 	 computation time primes: 0.0 s
# number of primes below 1000  =>  168
# 	 computation time primes: 0.0 s
# number of primes below 10000  =>  1229
# 	 computation time primes: 0.0 s
# number of primes below 100000  =>  9592
# 	 computation time primes: 0.031247615814208984 s
# number of primes below 1000000  =>  78498
# 	 computation time primes: 0.3917055130004883 s
# number of primes below 10000000  =>  664579
# 	 computation time primes: 4.938384294509888 s
# number of primes below 100000000  =>  5761455
# 	 computation time primes: 50.28856682777405 s
#just as expected it grows with factor 10
#number of primes below 1000000000  =>  50847534
#	 computation time primes: 594.089750289917 s
# then: MemoryError
