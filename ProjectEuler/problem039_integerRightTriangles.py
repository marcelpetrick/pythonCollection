# Integer right triangles
#
# Problem 39
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# ------------------------------------------------------------------------------

# idea:
# create all possible compositions, use pythagorean theorem to check

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def function():
    pass

# ------------------------------------------------------------------------------

def checkTriangleForBeingRightAngled(a,b,c):
    # find the biggest by creating a sorted list
    sl = sorted([a,b,c])
    isRightAngled = sl[0] ** 2 + sl[1] ** 2 == sl[2] ** 2
    return isRightAngled

# ------------------------------------------------------------------------------
# print(checkTriangleForBeingRightAngled(20, 48, 52))
# print(checkTriangleForBeingRightAngled(20, 50, 50))
# ------------------------------------------------------------------------------

import unittest
class Testcase(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(True, checkTriangleForBeingRightAngled(20, 48, 52))
        self.assertEqual(True, checkTriangleForBeingRightAngled(24, 45, 51))
        self.assertEqual(True, checkTriangleForBeingRightAngled(30, 40, 50))
        self.assertEqual(False, checkTriangleForBeingRightAngled(30, 42, 48))

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

