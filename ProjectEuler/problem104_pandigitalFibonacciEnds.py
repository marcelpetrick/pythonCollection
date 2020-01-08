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

def hasRequestedAttributes(currentFib, fibIndex):
    '''
    Check first the current fibonacci if it is pandigital. If yes, then compute the beginning and determine if the prefix is pandigital.
    :param currentFib:
    :param fibIndex:
    :return:
    '''
    currentFibStr = str(currentFib)

    # check the suffix for being pandigital
    suffix = currentFibStr[-9:]
    if isStringPandigital(suffix):
        #print("fibIndex:", fibIndex, "suffix:", currentFib)
        #print("\t at least suffix is pandigital")
        # check also the begin of the number for being pandigital
        prefix = firstNineDigitsMoivreBinet_asString(fibIndex)
        #print("\t prefix to check:", prefix)
        if isStringPandigital(prefix):
            #print("\t HIT! now also the prefix is fitting")
            return True

    return False

# ------------------------------------------------------------------------------

import decimal # avoid: OverflowError: (34, 'Result too large')
#decimal.getcontext().prec = 100
# even with decimal there is the following crash: decimal.Overflow: [<class 'decimal.Overflow'>]
decimal.getcontext().Emax = 20000000

# precomputed values
invRoot5 = decimal.Decimal(1 / 5 ** 0.5)
firstTerm = decimal.Decimal((1 + 5 ** 0.5) / 2)
#secondTerm = decimal.Decimal((1 - 5 ** 0.5) / 2)

def firstNineDigitsMoivreBinet_asString(n):
    ''' Closed formula for the computation of the n-th fibonacci number:
    https://de.wikipedia.org/wiki/Fibonacci-Folge#Formel_von_Moivre-Binet
    '''

    #fibo = invRoot5 * (firstTerm ** n - secondTerm ** n)
    fibo = invRoot5 * (firstTerm ** n) # simplified
    #print("fibo has exponent:", fibo.log10())
    multiplicator = int(fibo.log10()) - 9 - 1 # for nine proper digits # also added one, else the last digit was sometimes wrong
    #print("final multiplicator:", multiplicator)

    # print("n:", n, "->", fibo)
    # print("remove: ", secondTerm ** n)
    # print("remove: ", (secondTerm ** n) ** n) # almost zero with 100 ... can maybe removed ..
    firstDigits = fibo / (decimal.Decimal(10) ** decimal.Decimal(multiplicator))
    #print("fibo * decimal.Decimal(multiplicator):", firstDigits)
    stringified = "%.0f" % float(firstDigits)  # str(fibo) does give the exponential-form, which is not what is needed
    #print("stringified is:", stringified)
    returnValue = stringified[:9] if len(stringified) > 9 else stringified
    # print("-->", returnValue)
    return returnValue # keep as string, no conversion via int(..)

#limit = 2000
#print(limit, ":", firstNineDigitsMoivreBinet_asString(limit))
# ------------------------------------------------------------------------------

import unittest
import logging  # needed for unit-test-logging
import sys  # needed for unit-test-logging

class Testcase(unittest.TestCase):

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
        #self.assertEqual(firstNineDigitsMoivreBinet_asString(10), "55") # omitted, because wrong, because the result length is too small..
        # expected: 3542248481_79261915075
        startTime = time.time()
        self.assertEqual(firstNineDigitsMoivreBinet_asString(100), "354224848")
        log = logging.getLogger("TestLog")
        log.debug(" computing Moivre-Binet of 100th Fibo took %s s" % (time.time() - startTime))

        self.assertEqual(firstNineDigitsMoivreBinet_asString(300), "222232244")

        # calculated with: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibCalcX.html
        self.assertEqual(firstNineDigitsMoivreBinet_asString(1000), "434665576")

    def test_driver(self):
        ''' The test-call itself!'''

        import time
        startTime = time.time()
        log = logging.getLogger("TestLog")

        # the Fibonacci generator
        fibGen = getFibGen()

        # the driver itself which starts the threads
        while True:
            fibIndex, currentFib = next(fibGen)

            if hasRequestedAttributes(currentFib, fibIndex):
                log.debug(" %s is the index of the first fibonacci number where prefix and suffix are pandigital" % (fibIndex))
                break

        log.debug(" computation took %s s" % (time.time() - startTime))

    # ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()

# ------------------------------------------------------------------------------

# DEBUG:TestLog: 329468 is the index of the first fibonacci number where prefix and suffix are pandigital
# DEBUG:TestLog: computation took 0.47820258140563965 s
# .DEBUG:TestLog: 1000th fibonacci is 849228875, index is 1000
# ...DEBUG:TestLog: computing Moivre-Binet of 100th Fibo took 0.0 s
# .DEBUG:TestLog: getting the first 1000000 fibonaccis took 0.24993586540222168 s
# .
# ----------------------------------------------------------------------
# Ran 6 tests in 0.725s
#
# OK
#
# Process finished with exit code 0

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 104 is correct.
#
# You are the 14762nd person to have solved this problem.
#
# This problem had a difficulty rating of 25%. The highest difficulty rating you had previously solved was 20%.
# This is a new record. Well done!