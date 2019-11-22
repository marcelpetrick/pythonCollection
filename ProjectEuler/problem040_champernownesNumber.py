# Champernowne's constant
#
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# ------------------------------------------------------------------------------

# see also: https://oeis.org/A033307

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def createChampernowneNumberOfXDigits(digits):
    if digits < 1:
        raise ValueError("Bad luck for you today, only for digits bigger 0 defined.")

    returnValue = ""
    firstItem = 1
    while len(returnValue) < digits:
        returnValue += str(firstItem)
        firstItem -=- 1

    return returnValue

print(createChampernowneNumberOfXDigits(1000000))
