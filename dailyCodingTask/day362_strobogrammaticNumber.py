# This problem was asked by Twitter.
#
# A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees.
# For example, 16891 is strobogrammatic.
#
# Create a program that finds all strobogrammatic numbers with N digits.

# ------------------------------------------------------------------------------

# idea: if string is of length 0 or 1: is strobo; else: compare the first and last character for rotation-awareness;
# then apply the function to the inner string
#
# 1 is rotatable (is this a word?) to 1
# 2 to 5? (i would say yes, but this depends on the type of glyphs which are used; is a detail ..)
# 6 to 9
# 8 to itself
# 3, 4, 7 are fitting to nothing ... so if first/last is one of those, then discard

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

# added also the switched case to this list
fittingPairs = [(1, 1),
                (2, 5),
                (5, 2), # remove if 5 =/= 2
                (6, 9),
                (8, 8), # remove if 5 =/= 2
                (9, 6),
                ]

def isStroboGrammmatic(number):
    # todo description of the method
    # number should be an integer

    strNumber = str(number)

    if len(strNumber)  < 2:
        # strings of length 0 or 1 are always strobo
        return True

    # get the head and tail and convert them back to int
    first = int(strNumber[:1])
    last = int(strNumber[-1:])
    #print(first, last) # todo remove
    middle = strNumber[1:-1]
    #print("middle:", middle) # todo remove

    headAndTailAreStrobo = False
    for a,b in fittingPairs:
        if a == first and b == last:
            headAndTailAreStrobo = True


    return headAndTailAreStrobo

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        number = 16891
        expectedOutput = True
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample1(self):
        number = 123
        expectedOutput = False
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample2(self):
        number = 4
        expectedOutput = True
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

    def test_expectFail(self):
        self.assertFalse(1 < 0, "hell has frozen over")


# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
