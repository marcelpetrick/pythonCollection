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

    if(n == 1):
        return 1


    pass

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
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        n = 1
        expectedOutput = 1
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

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


createBlockList("1223334112351")