# Pandigital Fibonacci ends
#
# Problem 104
#
# The Fibonacci sequence is defined by the recurrence relation:
#
#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits
# are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains
# 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
#
# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9
# pandigital, find k.

# ------------------------------------------------------------------------------
# idea:
# * iterate numbers until one fitting with the given attributes is found ... print this.
# ------------------------------------------------------------------------------

def getFibGen():
    ''' Returns a generator for the Fibonacci numbers as well as the "index".
    @attention Fib is truncated to the last nine digits!'''

    a = 1
    b = 1
    counter = 1
    while True:
        yield counter, a
        a, b = b, (a + b) % 1000000000 # returns just as truncated form the last nine digits correctly :) big perfomance improvement: 10**6 with 0.5s versus 14s (for real implementation)
        counter += 1

# ------------------------------------------------------------------------------

def isStringPandigital(input):
    ''' Contains all digits from 1 to 9? '''

    if len(input) != 9:
        return False

    for elem in range(1,10):
        if str(elem) not in input:
            return False

    return True

# ------------------------------------------------------------------------------

# TODO have a look at this suggestion to omit the inner digits: https://euler.stephan-brumme.com/104/
def hasRequestedAttributes(currentFib, fibIndex):
    currentFibStr = str(currentFib)

    # check the begin for being pandigital
    prefix = currentFibStr[:9]  # first nine digits
    # print("prefix:", prefix)
    if isStringPandigital(prefix):
        print("Fib", fibIndex, ":", currentFib)
        print("\tat least prefix is pandigital")
        # check also the end for being pandigital
        suffix = currentFibStr[-9:]  # last nine digits
        # print("suffix:", suffix)
        if isStringPandigital(suffix):
            print("HIT! now also the suffix")
            return True

    return False

# ------------------------------------------------------------------------------

def driver():
    # now with threads ..
    from threading import Thread

    # the Fibonacci generator
    fibGen = getFibGen()

    # the driver itself which starts the threads
    fibIndex = 0
    while True:
        currentFib = next(fibGen)
        fibIndex += 1

        # TODO do this in a threaded way until we have a result
        hasRequestedAttributes(currentFib, fibIndex)
        thread = Thread(target=hasRequestedAttributes, args=(currentFib, fibIndex), daemon=True)
        thread.start() # omitting .join for the threads ..

# ------------------------------------------------------------------------------

# test call
#driver()

# ------------------------------------------------------------------------------

import unittest
import logging  # needed for unit-test-logging
import sys  # needed for unit-test-logging

class Testcase(unittest.TestCase):
    def test_fibGen_1000th_fib_has_proper_prefix_and_suffix(self):
        self.assertEqual(True, True)

    def test_fibGen(self):
        fibGen = getFibGen()

        # first is one?
        index, fib = fibGen.__next__()
        self.assertEqual(1, index)
        self.assertEqual(1, fib)

        # second is one?
        index, fib = fibGen.__next__()
        self.assertEqual(2, index)
        self.assertEqual(1, fib)

        # third is two?
        index, fib = fibGen.__next__()
        self.assertEqual(3, index)
        self.assertEqual(2, fib)

        # check the 1000th
        while index < 1000:
            index, fib = fibGen.__next__()

        # minor test: just check if the 1000th is correct: sample taken from: http://www.fullbooks.com/The-first-1001-Fibonacci-Numbers.html
        expectedResult = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
        self.assertEqual(1000, index)
        self.assertEqual(expectedResult % 1000000000, fib)
        log = logging.getLogger("TestLog")
        log.debug(" 1000th fibonacci is %s, index is %s" % (fib, index)) # todo fix this

    def test_performanceTestFibonaccis(self):
        '''  Quick test for the speed of the current fib-generator '''
        import time
        fibGen = getFibGen()
        limit = 10 ** 6
        startTime = time.time()
        index = -1
        while index < limit:
            index, fib = fibGen.__next__()

        log = logging.getLogger("TestLog")
        log.debug(" getting the first %s fibonaccis took %s s" % (limit, time.time() - startTime)) # todo fix this

    def test_isStringPandigital(self):
        self.assertEqual(False, isStringPandigital(""))
        self.assertEqual(False, isStringPandigital("1"))
        self.assertEqual(False, isStringPandigital("123"))
        self.assertEqual(False, isStringPandigital("12345678"))
        self.assertEqual(True, isStringPandigital("123456789"))
        self.assertEqual(False, isStringPandigital("1234567890"))
        self.assertEqual(True, isStringPandigital("987654321"))
        self.assertEqual(True, isStringPandigital("198765432"))
        self.assertEqual(False, isStringPandigital("1987654321"))
        self.assertEqual(False, isStringPandigital("aaa"))

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()

# ------------------------------------------------------------------------------
