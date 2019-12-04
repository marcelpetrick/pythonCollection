# Number spiral diagonals
#
# Problem 28
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# ------------------------------------------------------------------------------

# idea:
# * first generate a function which creates a filled matrix.
# * then just sum along the diagonals
# * use the top-right (is always the last entry) with the highest value (is sidelength ** 2), then count down while
# filling the matrix counterclockwise (and by decreasing)
# if border or filled element is reached, then turn "left" (based on the current direction)

# idea number 2: simplified ...
# it is not necessary to create the spiral and then sum it up. the distance between the currentElem and nextElem
# is (starting with value 1): +2 +2 +2 +2, then +4 +4 +4 +4, then +6 +6 +6 +6 ...
# This happens four times, because of the four corners. The increase is by 2 because with each iteration the sidelength
# is growing by two

# ------------------------------------------------------------------------------
import unittest
# import numpy as np
# ------------------------------------------------------------------------------

# BIG QUESTION: what to do with halfway started implementations, which are superseeded by a more clever, simpler approach?
# Of course the domain of the problem is shifted and reduced (and therefore easier to compute). But what if the
# intermediate stages would have been a good building block for further issues?
#
# def createMatrix(sidelength):
#     if sidelength <= 0 or sidelength % 2 == 0:
#         raise ValueError("Just odd values are allowed for the side length.")
#
#     # changed: take Fortran style
#     matrix = np.zeros((sidelength, sidelength), dtype=np.int64, order='F')  # shape s*s; no special data type or style
#     print("matrix = ", matrix)
#
#     # TODO continue
#     currentValue = sidelength * sidelength
#     currentX, currentY = sidelength - 1, 0
#     currentDirection = 0 # TODO to be defined -> see below for usage
#
#     while currentValue > 0:
#         # assign current value
#         matrix[currentY, currentX] = currentValue
#         # decrease current value
#         currentValue -= 1
#         # adjust the position
#         # direction 0: left; 1: down; 2: right; 3: up - by doing +1 and hen mod 4 it would cycle :)
#         # todo must be fully implemented: should have a method if the movement in the current direction would be a valid cell. if yes, then assign that ... else abort
#         currentX -= 1 # not proper!
#         currentY -= 0
#
#         print("matrix:")
#         print(matrix)
#
#         # make it halt before abort
#         if currentX < 0:
#             break

# ------------------------------------------------------------------------------

def computeDiagonalsSum(sidelength):
    if (sidelength <= 0) or (sidelength % 2 == 0):
        raise ValueError("Just odd values are allowed for the side length.")

    finalValue = sidelength * sidelength
    #print("count up to", finalValue)
    resultValue = 1  # TODO implement
    currentItem = 1 #starts at the first position, which is the center with 1
    stepSize = 2

    while currentItem < finalValue:

        # add four times the steps
        for i in range(4):
            currentItem += stepSize
            resultValue += currentItem
            #print("currentItem:", currentItem)

        # adjust the stepSize
        stepSize += 2

    return resultValue

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(True, True)

    def test_computeDiagonalsSum1(self):
        sideLength = 1
        expectedResult = 1
        output = computeDiagonalsSum(sideLength)
        self.assertEqual(output, expectedResult)
        print("sideLength", sideLength, " --> yielded result:", output)

    def test_computeDiagonalsSum3(self):
        sideLength = 3
        expectedResult = 1 + 3 + 5 + 7 + 9
        output = computeDiagonalsSum(sideLength)
        self.assertEqual(output, expectedResult)
        print("sideLength", sideLength, " --> yielded result:", output)

    def test_computeDiagonalsSum5(self):
        sideLength = 5
        expectedResult = 101 # given by task itself
        output = computeDiagonalsSum(sideLength)
        self.assertEqual(output, expectedResult)
        print("sideLength", sideLength, " --> yielded result:", output)

    def test_computeDiagonalsSum1001(self):

        # this is the final run!
        sideLength = 1001
        import time
        startTime = time.time()
        output = computeDiagonalsSum(sideLength)
        print("sideLength", sideLength, " --> yielded result:", output)
        print("computation took:", time.time() - startTime, "s")

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# Launching unittests with arguments python -m unittest C:/Users/mpe/Desktop/MarcelsFolder/coding/pythonCollection/ProjectEuler/problem028_numberSpiralDiagonals.py in C:\Users\mpe\Desktop\MarcelsFolder\coding\pythonCollection\ProjectEuler
#
# sideLength 1  --> yielded result: 1
# sideLength 1001  --> yielded result: 669171001
# computation took: 0.0 s
# sideLength 3  --> yielded result: 25
# sideLength 5  --> yielded result: 101
#
#
# Ran 5 tests in 0.013s
#
# OK

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 28 is correct.
#
# You are the 101057th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%.
