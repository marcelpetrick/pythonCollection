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

def driver():
    fibGen = getFibGen()

    index = 0
    currentFib = -1
    while True: # currentFib < 10 ** 10:
        currentFib = next(fibGen)
        #print("Fib", index, ":", currentFib)
        index += 1

        currentFibStr = str(currentFib)

        # check the begin for being pandigital
        prefix = currentFibStr[:9] # first nine digits
        #print("prefix:", prefix)
        if isStringPandigital(prefix):
            print("Fib", index, ":", currentFib)
            print("\tat least prefix is pandigital")
            # check also the end for being pandigital
            suffix = currentFibStr[-9:]  # last nine digits
            #print("suffix:", suffix)
            if isStringPandigital(suffix):
                print("HIT! now also the suffix")
                break

# ------------------------------------------------------------------------------

# test call
driver()
