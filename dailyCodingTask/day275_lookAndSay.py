# This problem was asked by Epic.
#
# The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually
# describes the digits appearing in the previous term. The first few terms are as follows:
#
# 1
# 11
# 21
# 1211
# 111221
#
# As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
#
# Given an integer N, print the Nth term of this sequence.

# ------------------------------------------------------------------------------

# idea:
# * split the given string into blocks of equal digits
# * count the length of that block and determine the "type"; then create a block-result like: "n""type"
# * combine all block results

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def lookAndSay(n):
    # todo return the nth term of the "look and say"-sequence

    if n <= 0:
        raise ValueError("Pascal's Triangle only defined for integer values bigger 0")

    counter = 1
    currentState = "1"
    while counter < n:
        counter += 1
        currentState = createNextStage(currentState)
        #print("counter:" + str(counter) + " | currentState:" + currentState)

    return currentState

# ------------------------------------------------------------------------------

def createBlockList(input):
    # take String; split into blocks of similar digits

    if len(input) == 0:
        raise Exception("input too short")

    blockList = []
    separator = input[0]
    currentBlock = ""
    for digit in input:
        if digit == separator:
            currentBlock += digit
        else:
            separator = digit
            blockList.append(currentBlock)
            currentBlock = digit
    blockList.append(currentBlock)

    return blockList

# ------------------------------------------------------------------------------

def createBlockResult(input):
    # todo maybe check if the type of the input is uniform

    type = input[0]
    length = len(input)
    result = str(length) + str(type)

    return result

# ------------------------------------------------------------------------------

def createNextStage(input):
    result = ""
    for elem in createBlockList(input):
        result += createBlockResult(elem)

    return result

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    # tests for lookAndSay
    def test_givenExample0(self):
        n = 1
        expectedOutput = "1"
        computedOutput = lookAndSay(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample1(self):
        n = 5
        expectedOutput = "111221"
        computedOutput = lookAndSay(n)
        self.assertEqual(expectedOutput, computedOutput)

    # TODO add a test which checks for the thrown exception
    def test_exceptionThrowing(self):
        self.assertRaises(ValueError, lookAndSay, -1337)

    # tests for createBlockList
    def test_createBlockListException(self):
        self.assertRaises(Exception, createBlockList, "")

    def test_createBlockList0(self):
        input = "2"
        expectedOutput = ["2"]
        computedOutput = createBlockList(input)
        self.assertEqual(expectedOutput, computedOutput)

    def test_createBlockList1(self):
        input = "222"
        expectedOutput = ["222"]
        computedOutput = createBlockList(input)
        self.assertEqual(expectedOutput, computedOutput)

    def test_createBlockList2(self):
        input = "1337"
        expectedOutput = ["1", "33", "7"]
        computedOutput = createBlockList(input)
        self.assertEqual(expectedOutput, computedOutput)

    def test_createBlockList3(self):
        input = "1223334112351"
        expectedOutput = ["1", "22", "333", "4", "11", "2", "3", "5", "1"]
        computedOutput = createBlockList(input)
        self.assertEqual(expectedOutput, computedOutput)

    # tests for createBlockResult
    def test_createBlockResult0(self):
        input = "1"
        expectedOutput = "11"
        computedOutput = createBlockResult(input)
        self.assertEqual(expectedOutput, computedOutput)

    def test_createBlockResult1(self):
        input = "444"
        expectedOutput = "34"
        computedOutput = createBlockResult(input)
        self.assertEqual(expectedOutput, computedOutput)

    # tests for createNextStage
    def test_createBlockResult0(self):
        input = "1211"
        expectedOutput = "111221"
        computedOutput = createNextStage(input)
        self.assertEqual(expectedOutput, computedOutput)


# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

print(lookAndSay(20))

# result:
#11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211
#Ran 10 tests in 0.016s