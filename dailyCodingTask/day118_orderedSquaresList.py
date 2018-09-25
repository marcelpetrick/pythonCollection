# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a sorted list of integers, square the elements and give the output in sorted order.
#
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def squareAndOrderList(inputList):
    intermediate = [element ** 2 for element in inputList]
    intermediate.sort()
    return intermediate

# ------------------------------------------------------------------------------

# add a short call
inputList = [-9, -2, 0, 2, 3]
result = squareAndOrderList(inputList)

print("result:", result)
