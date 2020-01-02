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

# taken from problem 002
def getFibGen():
    a = 1
    b = 1
    while True:
        yield a # yay, my first generator! :)
        a, b = b, a + b

# ------------------------------------------------------------------------------

def isStringPandigital(input):
    ''' Contains all digits from 1 to 9? '''

    if len(input) != 9:
        return False

    for elem in range(1,10):
        if str(elem) not in input:
            return False

    return True

# TODO convert this to unit-tests
print("pand:", isStringPandigital("123"))
print("pand:", isStringPandigital("1234567890"))
print("pand:", isStringPandigital("123456789"))
print("pand:", isStringPandigital("192345678"))
print("pand:", isStringPandigital("19234567811"))

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
driver()

# ------------------------------------------------------------------------------
# from an aborted, endlessly running test-execution ... now with threads

# Fib 240188 : ...
# 	at least prefix is pandigital
#
# Process finished with exit code -1

# ------------------------------------------------------------------------------