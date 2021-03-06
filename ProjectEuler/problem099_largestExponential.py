# Largest exponential
#
# Problem 99
# Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that
# 211 = 2048 < 37 = 2187.
#
# However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over
# three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
# base/exponent pair on each line, determine which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example given above.

# ------------------------------------------------------------------------------
# idea:
# Maybe using the logarithm is helpful: comparing by the length of the digits of the result:
# length = base * log(exponent) ?
# hint: https://www.quora.com/How-do-we-compare-numbers-with-big-exponents-and-different-bases-for-example-how-do-we-compare-3-210-and-17-140
#
# or: https://math.stackexchange.com/questions/2178989/finding-digits-of-large-exponent

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------


# todo add the implementation
