# This problem was asked by Amazon.
#
# An sorted array of integers was rotated an unknown number of times.
#
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
#
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
#
# You can assume all the integers in the array are unique.

############################# help needed from https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/ #############################
# 1) Find middle point mid = (l + h)/2
# 2) If key is present at middle point, return mid.
# 3) Else If arr[l..mid] is sorted
#     a) If key to be searched lies in range from arr[l]
#      to arr[mid], recur for arr[l..mid].
#     b) Else recur for arr[mid+1..r]
# 4) Else (arr[mid+1..r] must be sorted)
#     a) If key to be searched lies in range from arr[mid+1]
#        to arr[r], recur for arr[mid+1..r].
#     b) Else recur for arr[l..mid]
##########################################################

import unittest

# ------------------------------------------------------------------------------

def findInRotatedArray(inputList, element):
    print("findInRotatedArray called with: ", inputList, " and element ", element)
    returnValue = 0 # this will be the found index; zero by default and if not found (weird: shall be different than index == 0!)

    return returnValue


def findPivotElement(inputList):
    ''' Used to find the pivot element in the given list'''
    returnValue = 0
    if inputList.__len__() > 0:
        # returnValue = inputList[0]

        first = inputList[0]
        last = inputList[inputList.__len__() - 1]
        middle = inputList[inputList.__len__() / 2]

    return returnValue

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    ''' Tests for day58_findInRotatedArray.py '''

    def test0(self):
        inputList = [13, 18, 25, 2, 8, 10]
        element = 8
        expectedResult = 4
        output = findInRotatedArray(inputList, element)
        self.assertEqual(output, expectedResult)
        print(" --> input", inputList, " with element ", element, "yielded result:", output, ":)")

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


print("ATTENTION: not fully implemented version!!!")