# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decode-able. For example, '001' is not allowed.

import time
import unittest


# todo decorator with dictionary
# todo time-measurement

# ---------------------------------------------

def stopwatchDecorator(func):
    def decoratedFunc(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("call needed:", end - start)
        return result

    return decoratedFunc


# ---------------------------------------------

def memoisationDecorator(funk):
    ''' decorator for memoisation - works quite well :)'''
    d = {} # emptxy dictionary
    def decorated_func(n):
        if n in d: # if found, then return the already computed thing
            return d[n]
        d[n] = funk(n) # else: decorate
        return d[n]

    return decorated_func # return the new (the decorated) function

# ---------------------------------------------

# given word : interpretable in how many ways?
# 1 : 1 (1)
# 11 : 2 (11 and 2)
# 111 : 3 (111, 21, 12)
# 1111 :  5 (1111, 211, 121, 112, 22)
# 11111 : (11111, 2111, 1211, 1121, 1112,..)
# @stopwatchDecorator
@memoisationDecorator
def countDecodePossibilities(inputString):
    ''' Count all possibilites to decode a given string. '''
    amountOfFoundPossibilities = 0  # has to be fixed, of course ..

    # todo: dictionary for the already computed values
    if inputString.__len__() == 1:
        amountOfFoundPossibilities = 1
    elif inputString.__len__() == 2:
        amountOfFoundPossibilities = 1
        if isValidPair(inputString):
            amountOfFoundPossibilities += 1  # add one
    else:  # we have a longer string
        # plan:
        # cut of one item; also for the two-letter-case; recursively process the input
        prefixOne = inputString[:1]
        remainderOne = inputString[1:]
        prefixTwo = inputString[:2]  # check here if this is at all a valid double-digit item
        remainderTwo = inputString[2:]
        # print(prefixOne, remainderOne)
        # print(prefixTwo, remainderTwo)

        amountOfFoundPossibilities = countDecodePossibilities(remainderOne)
        if (isValidPair(prefixTwo)):
            amountOfFoundPossibilities += countDecodePossibilities(remainderTwo)

    # output = "countDecodePossibilities(" + inputString + ") = " + str(amountOfFoundPossibilities)
    # print(output)
    return amountOfFoundPossibilities


# ---------------------------------------------

def isValidPair(inputString):
    '''
    In case the given string of size two is <= 26, then return true. Else false.
    Check also the length: if different from two, then throw an exception.
    '''
    return (int(inputString) <= 26)  # converts string to int


# ---------------------------------------------

class ProductListTestCase(unittest.TestCase):
    ''' Tests for day7_decodeString.py '''

    def test0(self):
        inputString = "1"
        expectedOutput = 1
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def test1(self):
        inputString = "11"
        expectedOutput = 2  # namely: as "1,1" and "11"
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def test1a(self):
        inputString = "27"
        expectedOutput = 1  # namely: 2,7
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def test2(self):
        inputString = "111"
        expectedOutput = 3  # 111 : 3 (111, 21, 12)
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def test2a(self):
        inputString = "232"
        expectedOutput = 2  # 3 : 2,3,2; 23,2; 32,2 is invalid
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def test2b(self):
        inputString = "123"
        expectedOutput = 3  # 3 : 1,2,3; 12,3; 1,23
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def test3(self):
        inputString = "1111"
        expectedOutput = 5  # 1,1,1,1; 2,1,1; 1,2,1; 1,1,2; 2,2
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def test3a(self):
        inputString = "88888"
        expectedOutput = 1  # 1,1,1,1; 2,1,1; 1,2,1; 1,1,2; 2,2
        self.assertEqual(expectedOutput, countDecodePossibilities(inputString), "expected result does not match")
        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))


# ---- here comes the execution of the unit-tests ----
#if __name__ == '__main__':
#    unittest.main()

# ---- just some random-run for testing ----
import string
import random


# #@stopwatchDecorator
# def testRun(amountOfRuns):
#     inputString = ''.join(random.choices(string.ascii_uppercase + string.digits, 10))
#     print(inputString, amountOfRuns)

# stack overflow ..
def id_generator(size = 6, chars = string.digits):
    return ''.join(random.choice(chars) for _ in range(size)).replace("0", "")


foo = id_generator(500)
#foo = "9883627168399891958164272916396843616135412715394522814986713184577291221548244546742314444947666848275782528199"
start = time.time()
print(foo, "->", countDecodePossibilities(foo))
print("call took ", time.time() - start, "seconds")

#without decorator for memoisation:
#9883627168399891958164272916396843616135412715394522814986713184577291221548244546742314444947666848275782528199 -> 1048576
#call took  7.7468485832214355 seconds

#with:
#9883627168399891958164272916396843616135412715394522814986713184577291221548244546742314444947666848275782528199 -> 1048576
#call took  0.0 seconds

# even with leng5h 500 just 0.0 seconds! :)