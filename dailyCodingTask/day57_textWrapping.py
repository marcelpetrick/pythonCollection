# This problem was asked by Amazon.
#
# Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less.
# You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.
#
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
#
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
# ["the quick", "brown fox", "jumps over", "the lazy", "dog"].No string in the list has a length of more than 10.
##########################################################

import unittest

# ------------------------------------------------------------------------------

def wrapText(s, k):
    '''
    :param s - input string
    :param k - length in integer of desired substrings'''
    print("wrapText called with: ", s, " and length ", k)

    # my idea:
    # - split the whole text into substrings
    #- their length should be then used to "try" out all possible permutation-sums with less-equal the given length
    # would be: 3, 5, 5, 3, 5, 4, 3, 4, 3
    #- but when computing the length of concatenated words, then don't forget the space between as +1!
    splitString = s.split(" ")
    print("splitString", splitString)

    returnValue = []

    return returnValue

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    ''' Tests for day56_textWrapping.py '''

    def test0(self):
        s = "the quick brown fox jumps over the lazy dog"
        k = 10
        expectedResult = ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
        output = wrapText(s, k)
        self.assertEqual(output, expectedResult)
        print(" --> input", s, " with length ", k, "yielded result:", output, ":)")

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
