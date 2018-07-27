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

def lazybuttWrapText(s, k):
    '''
    :param s - input string
    :param k - length in integer of desired substrings'''
    print("lazybuttWrapText called with: ", s, " and length ", k)
    returnValue = []

    splitString = s.split(" ")

    # lazybutt-wrap: check if each element is a fitting substring and then just return this!
    allElementsOfValidLength = True
    for elem in splitString:
        if elem.__len__() > k:
            allElementsOfValidLength = False
            break
        print("check now:", elem) # todo remove: to see if break works

    if allElementsOfValidLength:
        print("yes, fits!")
        returnValue = splitString
    # end of lazybutt-version

    return returnValue

# ------------------------------------------------------------------------------

def wrapText(s, k):
    '''
    :param s - input string
    :param k - length in integer of desired substrings'''
    print("wrapText called with: ", s, " and length ", k)
    returnValue = []

    # my idea:
    # - split the whole text into substrings
    #- their length should be then used to "try" out all possible permutation-sums with a length less-equal the given length
    # would be: 3, 5, 5, 3, 5, 4, 3, 4, 3
    #- but when computing the length of concatenated words, then don't forget the space between as +1!
    splitString = s.split(" ")
    print("splitString", splitString)

    # lazybutt-wrap: check if each element is a fitting substring and then just return this!
    allElementsOfValidLength = True
    for elem in splitString:
        if elem.__len__() > k:
            allElementsOfValidLength = False
            break
        print("check now:", elem) # todo remove: to see if break works

    if allElementsOfValidLength:
        print("yes, fits!")
        returnValue = splitString
    # end of lazybutt-version

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

print("############################################################")
print("should not work:", lazybuttWrapText("klaushaus", 2))
print("should work:", lazybuttWrapText("klaushaus", 20))
