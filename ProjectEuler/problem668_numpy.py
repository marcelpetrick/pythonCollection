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

# ------------------------------------------------------------------------------

def sieveEras(limit):
    isPrimeArray = np.full(limit, True, dtype = bool)
    #print("before:", isPrimeArray)

    # zero and one are by definition no prime
    isPrimeArray[0] = False
    isPrimeArray[1] = False

    steps = 10 # number of expected feedback steps

    # compute primes
    print("### computing primes now ###")
    upperLimit = int(limit ** 0.5) + 1
    for index in range(upperLimit):
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
    print("### mapping bool to numbers now ###")
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
import time
print("###############")
for i in range(5, 7 + 1):
    startTime = time.time()
    print("how many primes in 10 ^", i, "?", len(sieveEras(10 ** i)), "in", time.time() - startTime, "s")
