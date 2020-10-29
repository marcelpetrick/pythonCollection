# Sub-string divisibility
#
# Problem 43
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in
# some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# ------------------------------------------------------------------------------
# idea:
# * the last triplet should be the most "awkward":
# ** construct all possible triplets from 0to9pandigital number-space: and check if div-able by 17
# ** if yes, then add one letter in front and check the new triplet if this is also divisable by 13
# ** .. same approach for the rest: this shall really rule out a lot of duds
# * question how many take-three-from-ten variants exist? (3 digits can be arranged in 6 different ways) - there should be 12 over 9 variations to pick 3 elements of ten given ones; then rearranging the oder multiply with six
# * but wait: instead of making a fuzz: for the start just count up all multiples of 17 from 0 to 1000: then check if unique digits (nothing double) and then use this as start for the additional checks ..
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def hasUniqueDigits(number):
    stringified = str(number)

    # this check fixes the problem with numbers with less than three digits (like 0), because the prefix
    # of zeroes would be added -> boom, not fitting anymore!
    if len(stringified) < 3:
        stringified = stringified.rjust(3, '0')
        #print("pad pad:", stringified)

    everycharUnique = len(set(stringified)) == len(stringified)
    return everycharUnique

# ------------------------------------------------------------------------------
# print(hasUniqueDigits(221)) # todo convert to unit-test!
# print(hasUniqueDigits(123))
# ------------------------------------------------------------------------------

def generateAlld8d9d10Numbers():
    candidates = []
    startingValue = 0
    while startingValue < 1000:
        if startingValue % 17 == 0:
            if hasUniqueDigits(startingValue):
                #print(startingValue)
                candidates.append(str(startingValue).rjust(3, '0'))

        startingValue += 17

    print("candidates:", candidates)
    print("number of items:", len(candidates))
    return candidates

# ------------------------------------------------------------------------------

# import time
# currentTime = time.time()
# generateAlld8d9d10Numbers()
# print("generation took", time.time() - currentTime, "s")

# ------------------------------------------------------------------------------

def findRemainingDigits(inputString):
    # gimme all the list comprehensions! maybe the double str(elem) can be eliminated somehow?
    resultSet = set(str(elem) for elem in range(10) if str(elem) not in inputString)
    #print(resultSet) # todo remove
    return resultSet

# ------------------------------------------------------------------------------
# just a test-call for the function
# print(findRemainingDigits("123"))
# print(findRemainingDigits("085"))
# ------------------------------------------------------------------------------

def createAllCandidatesWhichFulfilld7d8d9Attribute(inputListOfStringifiedSuffixes):
    # 0. create all possible combinations of one element of the  remaining digits prefixed to
    # the given element from inputListOfStringifiedSuffixes
    # 1. then check if this is dividable by 13 (should eliminate a lot of elements)

    for d8d9d10 in inputListOfStringifiedSuffixes:
        # 0. remaining digits
        remainingDigits = findRemainingDigits(d8d9d10)
        for d7 in remainingDigits:
            d7d8d9d10 = d7 + d8d9d10
            if int(d7d8d9d10[:3]) % 13 == 0:
                print("-->", d7d8d9d10)

                # todo continue with that one
                print("continue implementation here: that block should be refactored out: because it is applied iteratively for all other requirements")

    pass

# ------------------------------------------------------------------------------

createAllCandidatesWhichFulfilld7d8d9Attribute(generateAlld8d9d10Numbers()) # todo make this a better approach; the function shall create the input itself

# ------------------------------------------------------------------------------

# new, optimized function

def createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(
        inputListOfStringifiedSuffixes, divisorToObey):

    resultList = []

    for givenSuffixString in inputListOfStringifiedSuffixes:
        remainingDigits = findRemainingDigits(givenSuffixString)
        for prefix in remainingDigits:
            newNumberString = prefix + givenSuffixString
            if int(newNumberString[:3]) % divisorToObey == 0:
                #print("-->", newNumberString) # todo remove
                resultList.append(newNumberString)

    return resultList

# ------------------------------------------------------------------------------

result13 = createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(generateAlld8d9d10Numbers(), 13)
print("result13:", result13)
result11 = createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(result13, 11)
print("result11:", result11)
result7 = createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(result11, 7)
print(f"{result7=}") # abused the f-string-functionality for printing the vaiables name in front of the value
result5 = createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(result7, 5)
print(f"{result5=}")
result3 = createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(result5, 3)
print(f"{result3=}")
result2 = createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(result3, 2)
print(f"{result2=}")
# a filler for the first digit is needed: and this can be whatevery, so just make it divisiable by one!
result1 = createListOfStringifiedNumbersByPrependingOneOfTheRemainingDigitsWhileFulfillingDivisibility(result2, 1)
print(f"{result1=}")

finalSum = sum([int(elem) for elem in result1])
print("send to PE:", finalSum)
# ------------------------------------------------------------------------------

# result13: ['2085', '9102', '0136', '7153', '5204', '9238', '7289', '1306', '2340', '6374', '0391', '8459', '2476', '3510', '0527', '4680', '1697', '8714', '2731', '0782', '4816', '2867', '3901', '0918', '7935', '1952', '5986']
# result11: ['89102', '67153', '35204', '79238', '57289', '91306', '80391', '92476', '93510', '60527', '94680', '62731', '40782', '74816', '52867', '53901', '20918', '31952', '75986']
# result7=['735204', '679238', '357289', '791306', '280391', '392476', '693510', '294680', '462731', '140782', '574816', '952867', '420918', '175986']
# result5=['6357289', '0357289', '4357289', '1357289', '4952867', '0952867', '3952867', '1952867']
# result3=['06357289', '60357289', '30952867', '03952867']
# result2=['406357289', '106357289', '460357289', '160357289', '430952867', '130952867']
# result1=['1406357289', '4106357289', '1460357289', '4160357289', '1430952867', '4130952867']
# send to PE: 16695334890
