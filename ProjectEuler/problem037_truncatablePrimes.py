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

primes = getPrimesUntilLimit(10 ** 6)
def testPrimeTruncation(number):
    numberAsString = str(number)

    result = testStringTrunc(numberAsString)
    print(number, ":", "OK" if result else "ne")
    return result

# ------------------------------------------------------------------------------

def testStringTrunc(input):
    fromLeft = test(input, True)

    if fromLeft:
        fromRight = test(input, False)
        return fromRight
    else:
        return False

# ------------------------------------------------------------------------------

leftDict = dict()
rightDict = dict()

def test(inputString, fromLeft):
    #print("test:", inputString, fromLeft)

    # do dictionary lookup
    if fromLeft:
        if inputString in leftDict:
            return leftDict[inputString]
    else:
        if inputString in rightDict:
            return rightDict[inputString]

    # check the number itself
    numberItselfIsPrime = int(inputString) in primes
    # if fromLeft:
    #     leftDict[inputString] = numberItselfIsPrime
    # else:
    #     rightDict[inputString] = numberItselfIsPrime

    if not numberItselfIsPrime:

        if fromLeft:
            leftDict[inputString] = False
        else:
            rightDict[inputString] = False

        return False

    # check if single digit and therefore no recursion is needed
    length = len(inputString)

    #returnValue = False
    if length == 1:
        returnValue = True
    else:
        # de recursive check
        if fromLeft:
            inputString = inputString[1:length]
        else:
            inputString = inputString[0:length-1]

        returnValue = test(inputString, fromLeft)

    if fromLeft:
        leftDict[inputString] = returnValue
    else:
        rightDict[inputString] = returnValue

    return returnValue

# ------------------------------------------------------------------------------
import time
startTime = time.time()
listOfTruncatablePrimes = []
for number in primes:
    if testPrimeTruncation(number):
        listOfTruncatablePrimes.append(number)
print("computation took", time.time() - startTime, "s")
# before 10**5: 2.4s
# with memo 10**5:

print("truncatable primes:", listOfTruncatablePrimes)

noSingleDigit = [elem for elem in listOfTruncatablePrimes if elem > 9]
print("len:", len(noSingleDigit),":", noSingleDigit)

# print(".........")
# print("result:", test("277", True))
# print("........")
# print("result:", test("277", False))

#------------------------------------------------
# computation took 64.97186279296875 s
# truncatable primes: [2, 3, 5, 7, 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# len: 11 : [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]

# with python console:
# sum([23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397])
# Out[2]: 748317

# ----------------
# Congratulations, the answer you gave to problem 37 is correct.
#
# You are the 67897th person to have solved this problem.
