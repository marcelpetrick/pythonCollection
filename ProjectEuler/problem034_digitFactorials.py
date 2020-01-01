# Digit factorials
#
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# ------------------------------------------------------------------------------
# idea:
# * a function to compute the factorial (maybe with dictionary for caching) - not really needed, because just 0 to 9
# * if one of the facs is bigger than the wanted sum, then it can be skipped immediately, or?
# * what is the boundary? how to know to stop?
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
