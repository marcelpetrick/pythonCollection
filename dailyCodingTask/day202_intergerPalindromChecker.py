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

# ------------------------------------------------------------------------------

def isPalindrome(input):
    # todo implement this
    return True

# ------------------------------------------------------------------------------

def driver(input):
    print("input", input, ("is a palindrome" if isPalindrome(input) else "is not a palindrome"))

# ------------------------------------------------------------------------------

driver(12) # wrong, of course
driver(22)
