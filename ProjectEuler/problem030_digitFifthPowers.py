# Digit fifth powers
#
# Problem 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# ------------------------------------------------------------------------------

# idea:
# * implement a generalized function
# * is it a lucky hit that all aforementioned numbers are four-digit numbers? what about bigger numbers?
#       else generating and checking just the range of 10**n to 10**(n+1) woulds be enough
# * for digit in digits: compute the n-th power; add and check if the sum is the digit
# * maybe pre-calc a rainbow-table of all digit-powers and just make a look up
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
import time