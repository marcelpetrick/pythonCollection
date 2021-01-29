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
    ''' Returns a tuple of (failed?, number of iterations). '''

    if limitOfIterations == 0:
        # abort mission!
        return True, 666

    # check if given number is palindromic
    numberString = str(number)
    mirrorNumberStr = numberString[::-1]
    if numberString == mirrorNumberStr:
        return False, 0 # is already palindromic, so zero iterations needed
    else:
        # do lychrel iteration and therefore the "+1" for the number of iterations
        # reduce the limit
        result, iterations = computeNumberOfLychrelStepsNeeded(doLychrelIteration(number), limitOfIterations - 1)
        return result, iterations+1

# TODO write unit-test
# print("quick test 349:", computeNumberOfLychrelStepsNeeded(349, 50)) # should be 3
# print("quick test 10677:", computeNumberOfLychrelStepsNeeded(10677, 60)) # should be 53 iterations? yes

# ------------------------------------------------------------------------------

# # todo remove this
# def eulerDriver():
#     lychrelIterationsLimit = 50
#     numberLimit = 10000
#     lychrels = []
#     for number in range(1, numberLimit + 1):
#         failed, neededIterations = computeNumberOfLychrelStepsNeeded(number, lychrelIterationsLimit)
#
#         if failed == True: # means: after 50 iterations no result was found
#             print("lychrel number:", number, ":", neededIterations)
#             lychrels.append(number)
#
#     print(len(lychrels), "Lychrel numbers below", numberLimit)
#     print("lychrels:", lychrels)
#
#     expectedLychrelsBelow2k = [196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986, 1495, 1497, 1585, 1587, 1675, 1677, 1765, 1767, 1855, 1857, 1945, 1947, 1997]
#     print("expected:", expectedLychrelsBelow2k)
#
#     print("diff:", [elem for elem in expectedLychrelsBelow2k if elem not in lychrels])
#     # sadly this proves below 2k they are identical ... whut?!?
# # ------------------------------------------------------------------------------
#
# eulerDriver()

# lychrel number: 9957
# lychrel number: 9974
# lychrel number: 9978
# lychrel number: 9988
# 246 Lychrel numbers below 10000
# .. this is off by 3!


# ------------------------------------------------------------------------------

def computeLychrelsWithLimit50IterationsBelowLimit(limit):
    lychrelIterationsLimit = 50
    lychrels = []

    for number in range(1, limit + 1):
        failed, neededIterations = computeNumberOfLychrelStepsNeeded(number, lychrelIterationsLimit)

        if failed == True: # means: after 50 iterations no result was found
            #print("lychrel number:", number, ":", neededIterations) # will print 716, because 666+50+1 ... lol
            lychrels.append(number)

    return lychrels

# ------------------------------------------------------------------------------

import unittest
class Testcase(unittest.TestCase):
    def test_computeNumberOfLychrelStepsNeeded(self):
        self.assertEqual((False, 3), computeNumberOfLychrelStepsNeeded(349, 50))
        self.assertEqual((False, 53), computeNumberOfLychrelStepsNeeded(10677, 60))

    def test_computeLychrelsWithLimit50IterationsBelowLimit(self):
        self.assertEqual([196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986], computeLychrelsWithLimit50IterationsBelowLimit(1000))

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
# ------------------------------------------------------------------------------