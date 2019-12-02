# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given an array of numbers arr and a window of size k, print out the median of each window of size k starting from the left and moving right by one position each time.
#
# For example, given the following array and k = 3:
#
# [-1, 5, 13, 8, 2, 3, 3, 1]
# Your function should print out the following:
#
# 5 <- median of [-1, 5, 13]
# 8 <- median of [5, 13, 8]
# 8 <- median of [13, 8, 2]
# 3 <- median of [8, 2, 3]
# 3 <- median of [2, 3, 3]
# 3 <- median of [3, 3, 1]
# Recall that the median of an even-sized list is the average of the two middle numbers.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def getMedian(inputList):
    length = len(inputList)

    inputList.sort()

    if length == 0:
        raise ValueError("not defined")
    elif length == 1:
        return inputList[0]
    elif length % 2 == 1:
        return inputList[length // 2]
    else:
        secondPos = length // 2
        a = inputList[secondPos - 1]
        b = inputList[secondPos]
        return (a + b) / 2

# ------------------------------------------------------------------------------

def slidingWindowToOutputString(slidingWindow):
    resultString = str(getMedian(slidingWindow))
    resultString += " <- median of " + str(slidingWindow)
    return resultString

# ------------------------------------------------------------------------------

def slidingMedian(inputList, k):
    ''' will return a list of strings '''

    result = []

    for startIndex in range(len(inputList) - k + 1):
        slidingWindow = inputList[startIndex:startIndex+k] # start, stop, step
        print(slidingWindow)
        string = slidingWindowToOutputString(slidingWindow)
        result.append(string)

    return result

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):

    def test_givenExample(self):
        givenInput = [-1, 5, 13, 8, 2, 3, 3, 1]
        givenK = 3
        expectedOutput = ["5 <- median of [-1, 5, 13]",
                          "8 <- median of [5, 13, 8]",
                          "8 <- median of [13, 8, 2]",
                          "3 <- median of [8, 2, 3]",
                          "3 <- median of [2, 3, 3]",
                          "3 <- median of [3, 3, 1]"]
        computedOutput = slidingMedian(givenInput, givenK)
        self.assertEqual(expectedOutput, computedOutput)

    def test_getMedian(self):
        # TODO fix this
        # self.assertRaises(getMedian([]), ValueError)

        self.assertEqual(getMedian([3]), 3)

        self.assertEqual(getMedian([1, 2]), 1.5)

        self.assertEqual(getMedian([1, 2, 3]), 2)

        self.assertEqual(getMedian([10, 4, 3, 1]), 3.5)

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

givenInput = [-1, 5, 13, 8, 2, 3, 3, 1]
print(slidingMedian(givenInput, 3))

