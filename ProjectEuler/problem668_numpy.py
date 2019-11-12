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
#   // according https://github.com/ScytheMax -- the idea is (unedited quote):
#   // let p be a prim number. then follows p is not srs.
#   // because pp bigger p.
#   // the it follows for every natural number m with m lesser or equal p:
#   // pm is not a srs. because p is the highest prim factor in pm. so it follows pp bigger or equal pm.

#   // with this knowledge.
#   // 1. calc all primes until limit.
#   // 2. filter out all non srs by: take every prim p until limit. and filter out all numbers pm for m lesser equal p.
#
# ------------------------------------------------------------------------------

import unittest
import time
import numpy as np

# ------------------------------------------------------------------------------

def sieveEras(limit, returnPrimeListBoolInsteadOfNumbers = True):
    # print("################################")
    # print("compute primes up to", limit)
    # print("### creating prime-array now ###")
    isPrimeArray = np.full(limit, True, dtype=bool)
    #print("before:", isPrimeArray)

    # zero and one are by definition no prime
    isPrimeArray[0] = False
    isPrimeArray[1] = False

    # compute primes
    # print("### computing primes now ###")
    upperLimit = int(limit ** 0.5) + 1
    # steps = 10 # number of expected feedback steps
    # stepSize = upperLimit // steps
    # nextStep = 1
    for index in range(upperLimit):
        # # print some percentage
        # if index >= nextStep * stepSize:
        #     print(nextStep * 100 // steps, "%")
        #     nextStep += 1

        #print("handling:", index)
        if isPrimeArray[index] == False:
            continue
        else:
            multiple = 2
            while index * multiple < limit:
                isPrimeArray[index * multiple] = False
                multiple += 1

        #print("\tnow:", isPrimeArray)

    if returnPrimeListBoolInsteadOfNumbers:
        return isPrimeArray

    # map to numbers
    # print("### mapping bool to numbers now ###")
    resultList = []
    for i in range(limit):
        if isPrimeArray[i] == True:
            resultList.append(i)

    return resultList

# ------------------------------------------------------------------------------

def getNumberOfSqureRootSmoothNumbersBelow(inputLimit):
    limit = inputLimit + 1
    print("### start computation of number of SRS up to", limit, "now ###")
    primeArray = sieveEras(limit)
    print("* determined", sum(primeArray), "primes")

    # new array for the SRS
    srsArray = np.full(limit, True, dtype=bool)
    # zero and one are by definition no prime
    srsArray[0] = False
    srsArray[1] = False

    #   // 2. filter out all non srs by: take every prim p until limit. and filter out all numbers pm for m lesser equal p.
    for indexPrime in range(1, limit):
        # find the next prime by skipping over non-primes
        if primeArray[indexPrime] == False:
            continue

        #print("current prime to handle is:", indexPrime)
        # now remove all multiples m < p
        for multiple in range(1, indexPrime + 1): # prime included
            index = multiple * indexPrime
            #print("\ttackling multiple:", index)
            if index >= limit:
                break
            srsArray[index] = False

    # # SRS below 100: [8, 12, 16, 18, 24, 27, 30, 32, 36, 40, 45, 48, 50, 54, 56, 60, 63, 64, 70, 72, 75, 80, 81, 84, 90, 96, 98, 100]
    # # map to numbers
    # resultList = []
    # for i in range(limit):
    #     if primeArray[i] == True:
    #         resultList.append(i)
    # print("primes", resultList)
    # resultList = []
    # for i in range(limit):
    #     if srsArray[i] == True:
    #         resultList.append(i)
    # print("srs:", resultList)

    resultAmountSum = sum(srsArray) + 1 # with the famous +1
    print("\tsum gives result of", resultAmountSum, "SRS")
    # sum up manually, because of the overflow
    resultAmount = 1
    for elem in srsArray:
        if elem == True:
            resultAmount += 1
    print("\tcounting manually gives result of", resultAmount, "SRS")

    numpySum = srsArray.sum(dtype=np.int64, initial=1) # important, else it looks like int32 is taken: https://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    print("\tnumpy.sum gives result: ", numpySum, "SRS")

    print("* determined", resultAmount, "square-root-smooth numbers")
    return resultAmount

# ------------------------------------------------------------------------------

# proper unit-test
class Testcase(unittest.TestCase):

    def test_sieveEras10(self):
        limit = 10
        result = sieveEras(limit, False)
        #print("computed primes until", limit, " --> ", result)

        expectedPrimes = [2,3,5,7]
        self.assertEqual(expectedPrimes, result)

    def test_sieveEras100(self):
        limit = 100
        result = sieveEras(limit, False)
        #print("computed primes until", limit, " --> ", result)

        expectedPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(expectedPrimes, result)

    def test_sieveEras1000(self):
        limit = 1000
        result = sieveEras(limit, False)
        #print("computed primes until", limit, " --> ", result)

        expectedPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        self.assertEqual(expectedPrimes, result)

    def test_getSRS(self):
        result = getNumberOfSqureRootSmoothNumbersBelow(100) # 100000 --> 9592 primes
        self.assertEqual(29, result)

# ---- here comes the execution of the unit-tests ----

#if __name__ == '__main__':
#    unittest.main()

# ------------------------------------------------------------------------------
# commented to make it usable in other functions
# print("###############")
# for i in range(1, 10 + 1):
#     startTime = time.time()
#     print("--> amount of square-root-smooth numbers in 10 ^", i, "?", getNumberOfSqureRootSmoothNumbersBelow(10 ** i), "; computed in in", time.time() - startTime, "s")

# ###############
# ### start computation of number of SRS up to 11 now ###
# * determined 4 primes
# * determined 2 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 1 ? 2 ; computed in in 0.0 s
# ### start computation of number of SRS up to 101 now ###
# * determined 25 primes
# * determined 29 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 2 ? 29 ; computed in in 0.0 s
# ### start computation of number of SRS up to 1001 now ###
# * determined 168 primes
# * determined 274 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 3 ? 274 ; computed in in 0.015622138977050781 s
# ### start computation of number of SRS up to 10001 now ###
# * determined 1229 primes
# * determined 2656 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 4 ? 2656 ; computed in in 0.04686141014099121 s
# ### start computation of number of SRS up to 100001 now ###
# * determined 9592 primes
# * determined 26613 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 5 ? 26613 ; computed in in 0.4998812675476074 s
# ### start computation of number of SRS up to 1000001 now ###
# * determined 78498 primes
# * determined 268172 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 6 ? 268172 ; computed in in 5.098489284515381 s
# ### start computation of number of SRS up to 10000001 now ###
# * determined 664579 primes
# * determined 2719288 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 7 ? 2719288 ; computed in in 50.67194867134094 s
# ### start computation of number of SRS up to 100000001 now ###
# * determined 5761455 primes
# * determined 27531694 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 8 ? 27531694 ; computed in in 472.49259877204895 s
# ### start computation of number of SRS up to 1000000001 now ###
# * determined 50847534 primes
# * determined 278418003 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 9 ? 278418003 ; computed in in 4675.5832278728485 s
# ### start computation of number of SRS up to 10000000001 now ###
# * determined 455052511 primes
# * determined -1483889523 square-root-smooth numbers
# --> amount of square-root-smooth numbers in 10 ^ 10 ? -1483889523 ; computed in in 48464.38842749596 s

# ugh .. what is this? -1483889523 -> -1.483.889.523
#(1 << 31) -1 = 2.147.483.649

#np.int32	int32_t	Integer (-2147483648 to 2147483647)
#np.int64	int64_t	Integer (-9223372036854775808 to 9223372036854775807)

# -1483889523
#  2147483647 max
# -2147483648 max+1
#
# difference -1483889523 and -2147483648? is 663594125
#
#2147483647 + 1 + 663594125
#Out[10]: 2811077773


# Congratulations, the answer you gave to problem 668 is correct.
#
# You are the 438th person to have solved this problem.