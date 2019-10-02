# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# ------------------------------------------------------------------------------

# idea:
# how to generate them efficiently?
# a) memoization and then checking each iterated one?
# b) Sieve up to 2 mio, then sum ..
#
# what would be more or less the range to check (sieve) for primes by calculation?
# https://primes.utm.edu/howmany.html
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------------------------

#################################
# bad style, but I have to get things done ;)
# function "sieveEras" copied from problem668_numpy.py ..
#################################

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

primes = sieveEras(2000000, False)
print("sum:", sum(primes))

# output:
# sum: 142913828922
