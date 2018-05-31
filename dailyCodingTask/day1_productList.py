# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would
# be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

# done: implement the task
# done: write some unit-test

import unittest

# idea:
# 0. create outputList with same size as given inputList; initialized with 1
# 1. iterate once over the inputList; multiply this element-wise to the outputList except at current position
def produceProductList(inputList):
    # save the length, because needed three times
    listLength = len(inputList)

    # prepare an initialized list (value 1) of the given input-length
    returnValue = [1] * listLength

    # do the multiplication
    for indexInput in range(listLength):
        currentMultiplier = inputList[indexInput]
        # inner loop
        #print(range(len(returnValue))) #todom remove
        for indexOutput in range(len(returnValue)):
            if indexInput != indexOutput:
                #print("indexOutput: ", indexOutput) #todom remove
                returnValue[indexOutput] *= currentMultiplier

    return returnValue

#---------------------------------------------

# inputList0 = [1, 2, 3, 4, 5] # expected result: [120, 60, 40, 30, 24]
# inputList1 = [3, 2, 1] # expected result: [2, 3, 6]
#
# #todo write a decorator for that
# print(inputList0, "->", produceProductList(inputList0))
# print(inputList1, "->", produceProductList(inputList1))


# now we add some unit-testing :)
# https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
# also: http://docs.python-guide.org/en/latest/writing/tests/

class ProductListTestCase(unittest.TestCase):
    ''' Tests for day1_productList.py '''

    def testExampleOneWorks(self):
        inputList = [1, 2, 3, 4, 5]
        expectedOutputList = [120, 60, 40, 30, 24]
        self.assertTrue(expectedOutputList == produceProductList(inputList))

    def testExampleTwoWorks(self):
        inputList = [3, 2, 1]
        expectedOutputList = [2, 3, 6]
        self.assertTrue(expectedOutputList == produceProductList(inputList))

    # self defined failures - which are checked with assertFalse
    def testExampleWrongLength(self):
        ''' should fail intentionally: expected 3, got 2 '''
        inputList = [2, 3, 4]
        expectedOutputList = [1, 1]
        self.assertFalse(expectedOutputList == produceProductList(inputList))

    def testExampleTwoFailure(self):
        inputList = [3, 2, 1]
        expectedOutputList = [2, 3, 5]
        self.assertFalse(expectedOutputList == produceProductList(inputList))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
