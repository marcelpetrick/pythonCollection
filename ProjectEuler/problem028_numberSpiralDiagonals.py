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

# ------------------------------------------------------------------------------
import unittest
import numpy as np
# ------------------------------------------------------------------------------

def createMatrix(sidelength):
    if sidelength <= 0 or sidelength % 2 == 0:
        raise ValueError("Just odd values are allowed for the side length.")

    # changed: take Fortran style
    matrix = np.zeros((sidelength, sidelength), dtype=np.int64, order='F')  # shape s*s; no special data type or style
    print("matrix = ", matrix)

    # TODO continue
    currentValue = sidelength * sidelength
    currentX, currentY = sidelength - 1, 0
    currentDirection = 0 # TODO to be defined -> see below for usage

    while currentValue > 0:
        # assign current value
        matrix[currentY, currentX] = currentValue
        # decrease current value
        currentValue -= 1
        # adjust the position
        # direction 0: left; 1: down; 2: right; 3: up - by doing +1 and hen mod 4 it would cycle :)
        # todo must be fully implemented: should have a method if the movement in the current direction would be a valid cell. if yes, then assign that ... else abort
        currentX -= 1 # not proper!
        currentY -= 0

        print("matrix:")
        print(matrix)

        # make it halt before abort
        if currentX < 0:
            break

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(True, True)
    #     self.assertEqual(True, isPrime(3))
    #     self.assertEqual(False, isPrime(6))
    #     self.assertEqual(True, isPrime(7))
    #     self.assertEqual(False, isPrime(16))
    #     self.assertEqual(False, isPrime(25))
    #     self.assertEqual(True, isPrime(29))
    #     self.assertEqual(False, isPrime(87))
    #     self.assertEqual(True, isPrime(89))
    #
    # def test_findLargestPrimeFactor(self):
    #     input = 13195
    #     expectedResult = 29
    #     output = findLargestPrimeFactor(input)
    #     self.assertEqual(output, expectedResult)
    #     print(" --> input", input, "yielded result:", output)

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
createMatrix(5)
