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

#import itertools
def isGivenPrimeACircularPrime(prime, primeList):
    # checks if prime is really a prime or if primeList is not empty are omitted for performance reasons!
    primeString = str(prime)
    # create all rotations of the string
    rotations = {primeString[x:]+primeString[:x] for x in range(len(primeString))}
    for permutationTuple in rotations:
        permutAsNumber = int(''.join(permutationTuple))
        #print("current permut:", permutAsNumber)
        if permutAsNumber not in primeList:
            # if prime == 1193:
            #     print("1193 will skip because of:", permutAsNumber)
            return False

    return True

# ------------------------------------------------------------------------------

def createListOfCircularPrimesBelowLimit(limit):
    # generate the primes
    primesUpToLimit = getPrimesUntilLimit(limit)
    print("made primesUpToLimit")
    # primesForValidation = getPrimesUntilLimit(limit * 10) # have to be one magnitude bigger, else permutations of a number like 1193 could check against 9311, which is not in the first prime-list
    # print("made primesForValidation")

    #print("found:", primes)

    # filter the prime list by the circular-function # note: somehow this only works until 1000?!?
    circularPrimeList = [elem for elem in primesUpToLimit[:] if isGivenPrimeACircularPrime(elem, primesUpToLimit)]

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

for i in range(1, 7):
    import time
    startTime = time.time()
    print("#### run for 10 **", i, "####")
    result = createListOfCircularPrimesBelowLimit(10 ** i)
    print(time.time() - startTime, "s; exp = ", i, "result = ", result)
    print("len:", len(result), "first prime is:", result[0], "sum is:", sum(result))

# ------------------------------------------------------------------------------

# result = createListOfCircularPrimesBelowLimit(10 ** 4)
# print("result 10.000:", result)

# ------------------------------------------------------------------------------

# #### run for 10 ** 1 ####
# made primesUpToLimit
# 0.20301008224487305 s; exp =  1 result =  [2, 3, 5, 7]
# len: 4 first prime is: 2 sum is: 17
# #### run for 10 ** 2 ####
# made primesUpToLimit
# 0.0 s; exp =  2 result =  [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
# len: 13 first prime is: 2 sum is: 446
# #### run for 10 ** 3 ####
# made primesUpToLimit
# 0.0029976367950439453 s; exp =  3 result =  [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991]
# len: 25 first prime is: 2 sum is: 6440
# #### run for 10 ** 4 ####
# made primesUpToLimit
# 0.038007259368896484 s; exp =  4 result =  [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377]
# len: 33 first prime is: 2 sum is: 50880
# #### run for 10 ** 5 ####
# made primesUpToLimit
# 1.2425141334533691 s; exp =  5 result =  [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371]
# len: 43 first prime is: 2 sum is: 628652
# #### run for 10 ** 6 ####
# made primesUpToLimit
# 92.9756772518158 s; exp =  6 result =  [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]
# len: 55 first prime is: 2 sum is: 8184200
#
# Process finished with exit code 0

# ------------------------------------------------------------------------------
# Congratulations, the answer you gave to problem 35 is correct.
#
# You are the 79351st person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 25%.
