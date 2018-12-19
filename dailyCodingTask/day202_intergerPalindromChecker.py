# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome,
# as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
#
# ------------------------------------------------------------------------------
# idea:
#
# ------------------------------------------------------------------------------

import unittest
import math

# ------------------------------------------------------------------------------

def isPalindrome(input):
    # if the number is negative, then never a palindrome
    if input < 0:
        return False

    power = math.log(input, 10)
    # if the number has just one digit, it is palindrome
    if power < 1:
        return True

    # now check for those bigger (10 and upwards)

    # todo implement this

    # find first the power of 10
    power = math.log(input, 10)
    print(power)

    return False

# ------------------------------------------------------------------------------

def driver(input):
    print("input", input, ("is a palindrome" if isPalindrome(input) else "is not a palindrome"))

# ------------------------------------------------------------------------------

driver(-1)
driver(2)
driver(10) # wrong, of course
driver(100)
driver(101)
