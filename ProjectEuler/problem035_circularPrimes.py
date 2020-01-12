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
            return False

    return True

# ------------------------------------------------------------------------------

def createListOfCircularPrimesBelowLimit(limit):
    # generate the primes
    primes = getPrimesUntilLimit(limit)

    # filter the prime list by the circular-function
    circularPrimeList = [elem for elem in primes[:] if isGivenPrimeACircularPrime(elem, primes)]

    return circularPrimeList

# ------------------------------------------------------------------------------

# expected: 100 -> 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
print(createListOfCircularPrimesBelowLimit(10 ** 6))
