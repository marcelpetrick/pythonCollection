# Truncatable primes
#
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# ------------------------------------------------------------------------------

# idea:
# * implement function to compute all primes up to a certain limit
# * for each elem (prime) inside that list, check if a possible, consecutive sublist can be added up to that prime ->
# return the longest chain for each prime; sometimes maybe empty list
# check which prime has the longest list

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# reuse code from previous solution
def getPrimesUntilLimit(limit):
    from ProjectEuler.problem668_numpy import sieveEras  # works, but just after commenting lots of code inside that file
    primes = sieveEras(limit, False) # this is also a mistake in the second parameter
    #print(len(primes), ":", primes)  # 78,498 for 10 ** 6 - which is correct

    return primes

# ------------------------------------------------------------------------------

primes = getPrimesUntilLimit(10 ** 4)
def testPrimeTruncation(number):
    numberAsString = str(number)

    return testStringTrunc(numberAsString)

# ------------------------------------------------------------------------------

def testStringTrunc(input):
    fromLeft = test(input, True)
    fromRight = test(input, False)

    return fromLeft and fromRight

# ------------------------------------------------------------------------------

def test(inputString, fromLeft):
    print("test:", inputString, fromLeft)
    length = len(inputString)

    if length == 1:
        isPrime = int(inputString) in primes
        return isPrime

    if length > 1:
        if fromLeft:
            inputString = inputString[1:length]
        else:
            inputString = inputString[0:length-1]

    return test(inputString, fromLeft)

# ------------------------------------------------------------------------------

listOfTruncatablePrimes = []
for number in primes:
    if testPrimeTruncation(number):
        listOfTruncatablePrimes.append(number)

print("truncatable primes:", listOfTruncatablePrimes)

print(".........")
test("277", True)
print("........")
test("277", False)
