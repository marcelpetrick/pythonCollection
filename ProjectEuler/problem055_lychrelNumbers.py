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
# implementation
# ------------------------------------------------------------------------------

def doLychrelIteration(number):
    # create mirrored version
    mirrorNumber = int(str(number)[::-1])
    returnValue = number + mirrorNumber
    return returnValue

# ------------------------------------------------------------------------------

# big problem with that function is that palindromic lychrels as starting point are returned as being non-lychrel!
def computeNumberOfLychrelStepsNeeded(number, limitOfIterations, firstIteration = False):
    ''' Returns a tuple of (failed?, number of iterations). '''

    if limitOfIterations == 0:
        # abort mission!
        return True, 666

    # check if given number is palindromic
    numberString = str(number)
    mirrorNumberStr = numberString[::-1]
    if numberString == mirrorNumberStr and not firstIteration:
        return False, 0 # is already palindromic, so zero iterations needed
    else:
        # do lychrel iteration and therefore the "+1" for the number of iterations
        # reduce the limit
        result, iterations = computeNumberOfLychrelStepsNeeded(doLychrelIteration(number), limitOfIterations - 1)
        return result, iterations+1

# ------------------------------------------------------------------------------

def computeLychrelsWithLimit50IterationsBelowLimit(limit):
    lychrelIterationsLimit = 50
    lychrels = []

    for number in range(1, limit + 1):
        if number == 4994:
            print("debug now")
        failed, neededIterations = computeNumberOfLychrelStepsNeeded(number, lychrelIterationsLimit, True)

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
        self.assertEqual([196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986],
                         computeLychrelsWithLimit50IterationsBelowLimit(1000))
        self.assertEqual([196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986,
                          1495, 1497, 1585, 1587, 1675, 1677, 1765, 1767, 1855, 1857, 1945, 1947, 1997],
                         computeLychrelsWithLimit50IterationsBelowLimit(2000))

    def test_againstWikipedia(self):
        # see: https://de.wikipedia.org/wiki/Lychrel-Zahl
        expectedResultListBelow10k = [196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986,
1495, 1497, 1585, 1587, 1675, 1677, 1765, 1767, 1855, 1857, 1945, 1947, 1997,
2494, 2496, 2584, 2586, 2674, 2676, 2764, 2766, 2854, 2856, 2944, 2946, 2996,
3493, 3495, 3583, 3585, 3673, 3675, 3763, 3765, 3853, 3855, 3943, 3945, 3995,
4079, 4169, 4259, 4349, 4439, 4492, 4494, 4529, 4582, 4584, 4619, 4672, 4674, 4709, 4762, 4764, 4799, 4852, 4854, 4889, 4942, 4944, 4979, 4994,
5078, 5168, 5258, 5348, 5438, 5491, 5493, 5528, 5581, 5583, 5618, 5671, 5673, 5708, 5761, 5763, 5798, 5851, 5853, 5888, 5941, 5943, 5978, 5993,
6077, 6167, 6257, 6347, 6437, 6490, 6492, 6527, 6580, 6582, 6617, 6670, 6672, 6707, 6760, 6762, 6797, 6850, 6852, 6887, 6940, 6942, 6977, 6992,
7059, 7076, 7149, 7166, 7239, 7256, 7329, 7346, 7419, 7436, 7491, 7509, 7526, 7581, 7599, 7616, 7671, 7689, 7706, 7761, 7779, 7796, 7851, 7869, 7886, 7941, 7959, 7976, 7991,
8058, 8075, 8079, 8089, 8148, 8165, 8169, 8179, 8238, 8255, 8259, 8269, 8328, 8345, 8349, 8359, 8418, 8435, 8439, 8449, 8490, 8508, 8525, 8529, 8539, 8580, 8598, 8615, 8619, 8629, 8670, 8688, 8705, 8709, 8719, 8760, 8778, 8795, 8799, 8809, 8850, 8868, 8885, 8889, 8899, 8940, 8958, 8975, 8979, 8989, 8990,
9057, 9074, 9078, 9088, 9147, 9164, 9168, 9178, 9237, 9254, 9258, 9268, 9327, 9344, 9348, 9358, 9417, 9434, 9438, 9448, 9507, 9524, 9528, 9538, 9597, 9614, 9618, 9628, 9687, 9704, 9708, 9718, 9777, 9794, 9798, 9808, 9867, 9884, 9888, 9898, 9957, 9974, 9978, 9988, 9999]
        computedLychrel = computeLychrelsWithLimit50IterationsBelowLimit(10000)

        # compare
        for elem in expectedResultListBelow10k:
            if elem not in computedLychrel:
                print("missing:", elem)

        # expected: see three numbers ... and those will be tested
        # missing: 4994
        # missing: 8778
        # missing: 9999
        # that are the three palindromic lychrels ... why do they miss from the computed list?!?

print(4994, computeNumberOfLychrelStepsNeeded(4994, 100, True))
print(8778, computeNumberOfLychrelStepsNeeded(8778, 100, True))
print(9999, computeNumberOfLychrelStepsNeeded(9999, 100, True))

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
# ------------------------------------------------------------------------------

import time
startTime = time.time()
print(f"amount of potential Lychrel numbers below 10k: {len(computeLychrelsWithLimit50IterationsBelowLimit(10000))}")
print(f"computation too {time.time() - startTime} seconds")

# ------------------------------------------------------------------------------

# amount of potential Lychrel numbers below 10k: 249
# computation too 0.03774762153625488 seconds

# ------------------------------------------------------------------------------
