# This problem was asked by Airbnb.
#
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

import unittest


def maxSumInList(inputList):
    #print("maxsumlist called with: ", inputList)
    returnValue = 0

    # idea: since they shall be non-adjacent, adding always the first and calling
    # the function on the rest of the list (without head and head+1) recursively. Of course, this has lookup of O(n^2)

    if inputList.__len__() == 0:
        pass  # do nothing
    elif inputList.__len__() == 1:
        returnValue += inputList[0]  # add the value of first element and return
    else: # length at least two
        # idea: check if first or second element is bigger: pick the bigger one
        # additional note: the sume of the taken element and the remainder has to be maximum - this is the critical part

        results = [0,0] # needs to be prefilled - else access error6578
        for index in [0, 1]:
            head = inputList[index]
            remainingList = []
            if inputList.__len__() >= (index + 2):  # prevent index Error while accessing
                remainingList = inputList[(index + 2):]  # with gap of one
            results[index] = head + maxSumInList(remainingList)
            #print("check of", head, "plus", remainingList, "yields", results[index])

        # pick the one with the bigger sum
        if results[0] >= results[1]:
            returnValue += results[0]
        else:
            returnValue += results[1]

    return returnValue

# ------------------------------------------------------------------------------

class UnivalTestcase(unittest.TestCase):
    ''' Tests for day08_countUnivalSubtrees.py '''

    def test0(self):
        input = [2, 4, 6, 2, 5]
        expectedResult = 13
        self.assertEqual(maxSumInList(input), expectedResult)
        print("input", input, "yielded result", maxSumInList(input), ":)")

    def test1(self):
        input = [5, 1, 1, 5]
        expectedResult = 10
        self.assertEqual(maxSumInList(input), expectedResult)
        print("input", input, "yielded result", maxSumInList(input), ":)")

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


# https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/