# This problem was asked by Facebook.
#
# Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed
# using elements from L.
#
# For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.

# ------------------------------------------------------------------------------

def longestConsecutiveSequence(inputList):
    if len(inputList) == 0:
        raise ValueError("wrong input, just a list please")

    if len(inputList) == 1:
        return 1 # shortcut ..

    # sort first ascending
    inputList.sort()
    #print(inputList)

    # find the longest sequence by going through the whole list and check for sequences
    longestSequence = 0
    currentSequence = 0
    lastValue = inputList[0] - 1 # init it properly
    for index in range(len(inputList)):
        if inputList[index] == lastValue + 1:
            #print("+1")
            currentSequence += 1
        else:
            #print("fail. was", currentSequence)
            longestSequence = currentSequence
            currentSequence = 1
        lastValue = inputList[index]

    return longestSequence

# ------------------------------------------------------------------------------
# proper unit-test
import unittest
class Testcase(unittest.TestCase):
    def test_givenExample(self):
        giveInput = [5, 2, 99, 3, 4, 1, 100]
        expectedOutput = 5
        computedOutput = longestConsecutiveSequence(giveInput)
        self.assertEqual(expectedOutput, computedOutput)

    def test_ownTrack0(self):
        giveInput = [2, 4, 11, 12, 5, 7, 8, 9]
        expectedOutput = 3
        computedOutput = longestConsecutiveSequence(giveInput)
        self.assertEqual(expectedOutput, computedOutput)

    def test_ownTrack1(self):
        giveInput = [2]
        expectedOutput = 1
        computedOutput = longestConsecutiveSequence(giveInput)
        self.assertEqual(expectedOutput, computedOutput)

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
