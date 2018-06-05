# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

# todo write unit-tests for the first five(?)-char-strings

import unittest

def countDecodePossibilities(inputString):
    ''' bla bla '''
    amountOfFoundPossibilities = 0 # has to be fixed, of course ..

    return amountOfFoundPossibilities


#---------------------------------------------


class ProductListTestCase(unittest.TestCase):
    ''' Tests for day7_decodeString.py '''

    def test0(self):
        inputString = "1"
        expectedOutput = 1
       # self.assertTrue(expectedOutput == countDecodePossibilities(inputString))
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")


# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
