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

# ------------------------------------------------------------------------------

def driver():
    fibGen = getFibGen()

    index = 1
    currentFib = -1
    while currentFib < 100:
        currentFib = next(fibGen)
        print("index", index, ":", currentFib)
        index += 1

# ------------------------------------------------------------------------------

# test call
driver()
