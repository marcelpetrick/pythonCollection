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
# * to say it bluntly: this idea ould work, but due to the handling of numbers with a lot of digits, this consumes more time to call functions than to do something
#
# inspiration taken from this suggestion to omit the inner digits: https://euler.stephan-brumme.com/104/
# also used a closed formula to determine the first digits (Moivre-Binet)
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

    # check the suffix for being pandigital
    suffix = currentFibStr[-9:]
    if isStringPandigital(suffix):
        print("Fib", fibIndex, ":", currentFib)
        print("\tat least suffix is pandigital")
        # check also the beginof the number for being pandigital
        prefix = firstNineDigitsMoivreBinet_asString(fibIndex)
        print("prefix:", prefix)
        if isStringPandigital(prefix):
            print("HIT! now also the prefix is fitting")
            return True

    return False

# ------------------------------------------------------------------------------

# precomputed values
invRoot5 = 1 / 5 ** 0.5
firstTerm = (1 + 5 ** 0.5) / 2
secondTerm = (1 - 5 ** 0.5) / 2

def firstNineDigitsMoivreBinet_asString(n):
    ''' Closed formula for the computation of the n-th fibonacci number:
    https://de.wikipedia.org/wiki/Fibonacci-Folge#Formel_von_Moivre-Binet
    '''

    fibo = invRoot5 * (firstTerm ** n - secondTerm ** n)
    # print("n:", n, "->", fibo)
    # print("remove: ", secondTerm ** n)
    # print("remove: ", (secondTerm ** n) ** n) # almost zero with 100 ... can maybe removed ..

    stringified = "%.0f" % fibo  # str(fibo) does give the exponential-form, which is not what is needed
    # print("stringified is:", stringified)
    returnValue = stringified[:9+1] if len(stringified) > 9 else stringified
    # print("-->", returnValue)
    return returnValue # keep as string, no conversion via int(..)

# ------------------------------------------------------------------------------

def driver():
    # now with threads ..
    #from threading import Thread

    # the Fibonacci generator
    fibGen = getFibGen()

    # the driver itself which starts the threads
    while True:
        fibIndex, currentFib = next(fibGen)

        # TODO do this in a threaded way until we have a result
        if hasRequestedAttributes(currentFib, fibIndex):
            print("we have a hit!", fibIndex, ":", currentFib)
        #thread = Thread(target=hasRequestedAttributes, args=(currentFib, fibIndex), daemon=True)
        #thread.start() # omitting .join for the threads ..

# ------------------------------------------------------------------------------

# test call
driver()

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
        log.debug(" 1000th fibonacci is %s, index is %s" % (fib, index))

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
        log.debug(" getting the first %s fibonaccis took %s s" % (limit, time.time() - startTime))

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

    def test_moivreBinet(self):
        import time
        # expected: 55
        self.assertEqual(firstNineDigitsMoivreBinet_asString(10), "55")
        # expected: 3542248481_79261915075
        startTime = time.time()
        self.assertEqual(firstNineDigitsMoivreBinet_asString(100), "3542248481")
        log = logging.getLogger("TestLog")
        log.debug(" computing Moivre-Binet of 100th Fibo took %s s" % (time.time() - startTime))

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()

# ------------------------------------------------------------------------------
