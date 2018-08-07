# This problem was asked by Facebook.
#
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.

# my idea: go once through the whole list, check each element with container.
# that container saves the two smallest negative numbers and the three biggest.
# afterwards: choose wisely ;)
# if the product of the two negative numbers (can either be 0 or 2 negative numbers, because with one or three negative
# ones the product becomes negative -> fail.

import unittest

# ------------------------------------------------------------------------------

class ContainerForBiggestAbs: #
    ''' idea is to push all incoming data to the corresponding list (neg or pos). Then do a cutoff after sorting. '''
    negativeList = []
    positiveList = []
    negativeAmount = 2 # constant
    positiveAmount = 3 # constant

    def __init__(self):
        # nothing to do here
        print("Lexer::__init__")

    def check(self, value):
        ''' Check the given value and sort it into fitting lists.
        The one for negative numbers inverts them automatically, because it will be only two elemnts long.
        '''
        if value == 0:
            return # we don't need ya!

        # quite copy&paste-d code. Could be improved.
        # todo unit tests!
        if value < 0:
            self.negativeList.append(-value) # negate!
            self.negativeList.sort()
            self.negativeList.reverse() # or sort reverted ....
            while self.negativeList.__len__() > self.negativeAmount:
                self.negativeList.pop()
            #print("neg: after pop", self.negativeList)
        else: # must be 0 or positive
            self.positiveList.append(value) # negate!
            self.positiveList.sort()
            self.positiveList.reverse() # or sort reverted ....
            while self.positiveList.__len__() > self.positiveAmount:
                self.positiveList.pop()
            #print("pos: after pop", self.positiveList)

    def getNegativeList(self):
        ''' Check as well if we have an even number of negative values. '''
        amount = len(self.negativeList)
        if amount == 0 or amount == 2:
            return self.negativeList
        else:
            return []

    def getPositiveList(self):
        return self.positiveList

# ------------------------------------------------------------------------------

def biggestProduct(inputList):
    print("biggestProduct called with: ", inputList)

    theContainer = ContainerForBiggestAbs()
    # iterate over the whole input
    for elem in inputList:
        theContainer.check(elem)

    print("biggestProduct: pos:", theContainer.getPositiveList())
    print("biggestProduct: neg:", theContainer.getNegativeList())

    returnValue = None

    return returnValue

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test0(self):
        inputList = [-10, -10, 5, 2]
        expectedResult = 500
        output = biggestProduct(inputList)
        self.assertEqual(output, expectedResult)
        print(" --> input", inputList, "yielded result:", output)


# # ------------------------------------------------------------------------------
#
# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


print("###############################")
inputList = [-5, -3, -4, -1, 90, 30, -2, -6, 80, 20, 100]
output = biggestProduct(inputList)
