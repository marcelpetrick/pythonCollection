# Number letter counts
#
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# ------------------------------------------------------------------------------
# idea:

# ------------------------------------------------------------------------------
import unittest


# ------------------------------------------------------------------------------

def letterCount(word):
    return len(word)


# how to make this "static"?
# create a list of tuples, which is then converted to a dictionary
numberDict = dict([
    (0, "zero"),
    (1, "one"),
    (2, "two"),
    (3, "three"),
    (4, "two"),
    (5, "two"),
    (6, "two"),
    (7, "two"),
    (8, "two"),
    (9, "two"),
    (10, "ten"),
    (11, "eleven"),
    (12, "twelve"),
    (13, "thirteen"),
    (14, "fourteen"),
    (15, "fifteen"),
    (16, "fifteen"),
    (17, "seventeen"),
    (18, "eighteen"),
    (19, "nineteen"),
    (20, "twenty"),
    (30, "thirty"),
    (40, "forty"),
    # to be continued
])
print("numberDict:", numberDict)


def convertNumberToString(number):
    if number < 0:
        raise Exception("Wrong input value.")
