# This problem was asked by Google.
#
# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
# For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
#
#   1
#  2 3
# 1 5 1
#
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
# eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is
# the sum of the entries.
#
# Write a program that returns the weight of the maximum weight path.

# ------------------------------------------------------------------------------
# idea:
# * looks like the trick is to imagine this pyramid not as "centered" version, but as one aligned to the left
# 0
# 0 1
# 0 1 2
# 0 1 2 3 ..
# Then it is immediately clear by the indices which are the "followers". 0 goes to 00, 01. 01 has 011 and 012.
# Given the fact that the levels are fully filled, the follower of n is n and n+1.
#
# First we need a "path-generator": which yields all possible paths through the pyramid (array of arrays).
# Then a "sum the path".
# Then a driver iterating over all paths, getting their sums and then finding the biggest one. Printing that path.
#
# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def findMaximumWeightedSum(inputArray):
    pass

# ------------------------------------------------------------------------------

def generatePaths(inputArray):
    # todo find the depth of the pyramid
    depth = len(inputArray)
    print("generatePaths: depth:", depth)

    returnValue = []

    if depth == 0:
        pass # nothing to do
    else:
        firstElem = [inputArray[0]] # as list
        returnValue.append(firstElem)
        # todo continue here

    print("will return returnValue: ", returnValue)

    # todo generate all paths
    # return a list of lists (the paths)
    return returnValue

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_findMaximumWeightedSum(self):
        #self.assertEqual(True, [] == rotateByOne([]))
        pass

    def test_generatePaths(self):
        # no paths for an empty array
        self.assertEqual(True, [] == generatePaths([]))
        # just one path for an one-element array
        self.assertEqual(True, [[0]] == generatePaths([0]))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
