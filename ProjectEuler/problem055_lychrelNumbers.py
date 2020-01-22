# Lychrel numbers
#
# Problem 55
#
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the
# theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel
# until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become
# a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so
# far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before
# producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

# ------------------------------------------------------------------------------
# idea:
# TODO

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def doLychrelIteration(number):
    # create mirrored version
    mirrorNumber = int(str(number)[::-1])
    returnValue = number + mirrorNumber
    return returnValue

# TODO write a unit-test with the given numbers
#print(doLychrelIteration(349))
# ------------------------------------------------------------------------------

def computeNumberOfLychrelStepsNeeded(number, limitOfIterations):
    if limitOfIterations == 0:
        # abort mission!
        return True, 666

    # check if given number is palindromic
    numberString = str(number)
    mirrorNumberStr = numberString[::-1]
    if numberString == mirrorNumberStr:
        return False, 0 # is already palindromic, so zero iterations needed
    else:
        # do lychrel iteration and therefore the "+1" for the iterations
        # reduce the limit
        result, iterations = computeNumberOfLychrelStepsNeeded(doLychrelIteration(number), limitOfIterations - 1)
        return result, iterations+1

# TODO write unit-test
# print("quick test 349:", computeNumberOfLychrelStepsNeeded(349, 50)) # should be 3
# print("quick test 10677:", computeNumberOfLychrelStepsNeeded(10677, 60)) # should be 53 iterations? yes

# ------------------------------------------------------------------------------

def eulerDriver():
    amount = 0
    lychrelIterationsLimit = 49
    numberLimit = 10000
    lychrels = []
    for number in range(1, numberLimit + 1):
        result, neededIterations = computeNumberOfLychrelStepsNeeded(number, lychrelIterationsLimit)

        if result == True:
            #print("lychrel number:", number)
            amount += 1
            lychrels.append(number)

    print(amount, "Lychrel numbers below", numberLimit)
    print("lychrels:", lychrels)

# ------------------------------------------------------------------------------

eulerDriver()
# lychrel number: 9957
# lychrel number: 9974
# lychrel number: 9978
# lychrel number: 9988
# 246 Lychrel numbers below 10000
# ------------------------------------------------------------------------------

# Project Euler says: wrong ..

# ------------------------------------------------------------------------------

# 10833 needs 54 iterations
# 10911 needs 55 iterations
# 147996 needs 58 iterations
# 150296 needs 64 iterations
l
