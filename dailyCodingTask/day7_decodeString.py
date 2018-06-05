# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

# todo write unit-tests for the first five(?)-char-strings

import unittest

# given word : interpretable in how many ways?
# 1 : 1 (1)
# 11 : 2 (11 and 2)
# 111 : 3 (111, 21, 12)
# 1111 :  5 (1111, 211, 121, 112, 22)
# 11111 : (11111, 2111, 1211, 1121, 1112,
def countDecodePossibilities(inputString):
    ''' Count all possibilites to decode a given string. '''
    amountOfFoundPossibilities = 0 # has to be fixed, of course ..

    # todo: dictionary for the already computed values
    if inputString.__len__() == 1:
        amountOfFoundPossibilities = 1
    elif inputString.__len__() == 2:
        amountOfFoundPossibilities = 1
        if isValidPair(inputString):
            amountOfFoundPossibilities += 1 # add one
    else: # we have a longer string
        # plan:
        # cut of one item; also for the two-letter-case; recursively process the input
        pass

    output = "countDecodePossibilities(" + inputString + ") = " + str(amountOfFoundPossibilities)
    print(output)
    return amountOfFoundPossibilities

#---------------------------------------------
def isValidPair(inputString):
    '''
    In case the given string of size two is <= 26, then return true. Else false.
    Check also the length: if different from two, then throw an exception.
    '''
    return (int(inputString) <= 26) # converts string to int

#---------------------------------------------


class ProductListTestCase(unittest.TestCase):
    ''' Tests for day7_decodeString.py '''

    def test0(self):
        inputString = "1"
        expectedOutput = 1
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")

    def test1(self):
        inputString = "11"
        expectedOutput = 2 # namely: as "1,1" and "11"
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")

    def test1a(self):
        inputString = "27"
        expectedOutput = 1 # namely: 2,7
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")

    def test2(self):
        inputString = "111"
        expectedOutput = 3 # 111 : 3 (111, 21, 12)
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")

    def test2a(self):
        inputString = "232"
        expectedOutput = 2 # 3 : 2,3,2; 23,2; 32,2 is invalid
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")

    # def test3(self):
    #     inputString = "1111"
    #     expectedOutput = 3 # 1111 : 3 (111, 21, 12)
    #     self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
