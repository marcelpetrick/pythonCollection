# This problem was asked by Amazon.
#
# An sorted array of integers was rotated an unknown number of times.
#
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
#
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
#
# You can assume all the integers in the array are unique.




###################


import unittest


def findInRotatedArray(inputList, element):
    print("findInRotatedArray called with: ", inputList, " and element ", element)
    returnValue = -1 # is the found index

    return returnValue

# ------------------------------------------------------------------------------

class UnivalTestcase(unittest.TestCase):
    ''' Tests for day8_countUnivalSubtrees.py '''

    def test0(self):
        inputList = [13, 18, 25, 2, 8, 10]
        element = 8
        expectedResult = 4
        output = findInRotatedArray(inputList, element)
        self.assertEqual(output , expectedResult)
        print(" --> input", inputList, " with element ", element, "yielded result:", output, ":)")

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
