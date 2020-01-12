# Circular primes
#
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
# are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

# ------------------------------------------------------------------------------
# idea:
# * compute all primes up to the limit, take the function from problem 50
# * create function which returns if a given prime is a circular prime (permutation..)
# * return len(resultList) .. profit!

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# reuse code from previous solution
# TODO maybe consider to use a prime-generator, which is proven and tested; see problem041
def getPrimesUntilLimit(limit):
    from ProjectEuler.problem668_numpy import sieveEras  # works, but just after commenting lots of code inside that file
    primes = sieveEras(limit, False) # this is also a mistake in the second parameter
    #print(len(primes), ":", primes)  # 78,498 for 10 ** 6 - which is correct

    return primes

# ------------------------------------------------------------------------------

import itertools
def isGivenPrimeACircularPrime(prime, primeList):
    # checks if prime is really a prime or if primeList is not empty are omitted for performance reasons!
    primeString = str(prime)
    for permutationTuple in itertools.permutations(primeString):
        permutAsNumber = int(''.join(permutationTuple))
        #print("current permut:", permutAsNumber)
        if permutAsNumber not in primeList:
            if prime == 1193:
                print("1193 will skip because of:", permutAsNumber)
            return False

    return True

# ------------------------------------------------------------------------------

def createListOfCircularPrimesBelowLimit(limit):
    # generate the primes
    primesUpToLimit = getPrimesUntilLimit(limit)
    print("made primesUpToLimit")
    primesForValidation = getPrimesUntilLimit(limit * 10) # have to be one magnitude bigger, else permutations of a number like 1193 could check against 9311, which is not in the first prime-list
    print("made primesForValidation")

    #print("found:", primes)

    # filter the prime list by the circular-function # note: somehow this only works until 1000?!?
    circularPrimeList = [elem for elem in primesUpToLimit[:] if isGivenPrimeACircularPrime(elem, primesForValidation)]

    # # reimplementation
    # circularPrimeList = []
    # for prime in primes:
    #     if isGivenPrimeACircularPrime(prime, primes):
    #         print("is circular:", prime)
    #         circularPrimeList.append(prime)

    return circularPrimeList

# ------------------------------------------------------------------------------

# expected: 100 -> 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#print(createListOfCircularPrimesBelowLimit(10 ** 6))

# for i in range(1, 7):
#     import time
#     startTime = time.time()
#     print("#### run for 10 **", i, "####")
#     result = createListOfCircularPrimesBelowLimit(10 ** i)
#     print(time.time() - startTime, "s; exp = ", i, "result = ", result)
#     print("len:", len(result), "first prime is:", result[0], "sum is:", sum(result))

# ------------------------------------------------------------------------------

result = createListOfCircularPrimesBelowLimit(10 ** 4)
print("result 10.000:", result)
