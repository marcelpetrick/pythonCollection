# This problem was asked by Airbnb.
#
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

import unittest


def maxSumInList(inputList):
    print("maxsumlist called with: ", inputList)
    returnValue = 0

    # idea: since they shall be non-adjacent, adding always the first and calling
    # the function on the rest of the list (without head and head+1) recursively. Of course, this has lookup of O(n^2)

    if inputList.__len__() == 0:
        pass  # do nothing
    elif inputList.__len__() == 1:
        returnValue += inputList[0]  # add the value of first element and return
    else: # length at least two
        additionalOffset = 1
        # idea: check if first or second element is bigger: pick the bigger one
        first = inputList[0]
        second = inputList[1]
        if first >= second:
            index = 0
            returnValue += first
            print("take first", first)
        else:
            index = 1
            returnValue += second
            print("take second", second)

        if inputList.__len__() >= (index + 2): # prevent index Error while accessing
            remainingList = inputList[(index + 2):] # with gap of one
            print(".. even enough for another call with:", remainingList)
            returnValue += maxSumInList(remainingList)


        # # now check if the next element for gap is negative or zero: if that is the case, then this is ALWAYS the proper gap
        # additionalOffset = 1
        # if inputList[index + additionalOffset] <= 0 or inputList.__len__() == 2:
        #     print("negative or zero value found:", inputList[index + additionalOffset])
        #     remainderWithGap = inputList[(index + additionalOffset):]
        #     # check now for that part for the maxSum
        #     returnValue += maxSumInList(remainderWithGap)
        # else:
        #     # do a regular gap - or do a two-gap and call again
        #     # compare both results and use the bigger one
        #     remainderOneGap = inputList[(index + 1):]
        #     remainderTwoGap = inputList[(index + 2):] # will this crash?
        #     # todo maybe add some history of the worthy path?
        #     resultOneGap = maxSumInList(remainderOneGap)
        #     resultTwoGap = maxSumInList(remainderTwoGap)
        #     if resultOneGap >= resultTwoGap:
        #         print("oneGap won")
        #         returnValue += resultOneGap
        #     else:
        #         print("twoGap won")
        #         returnValue += resultTwoGap

    return returnValue

# ------------------------------------------------------------------------------

class UnivalTestcase(unittest.TestCase):
    ''' Tests for day8_countUnivalSubtrees.py '''

    def test0(self):
        input = [2, 4, 6, 2, 5]
        expectedResult = 13
        self.assertEqual(maxSumInList(input), expectedResult)
        print("input", input, "yielded result", maxSumInList(input), ":)")

    def test1(self):
        input = [5, 1, 1, 5]
        expectedResult = 10
        self.assertEqual(maxSumInList(input), expectedResult)


# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


# https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/