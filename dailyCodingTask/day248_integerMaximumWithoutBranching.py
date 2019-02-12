# This problem was asked by Nvidia.
#
# Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.

# ------------------------------------------------------------------------------

# idea: some XOR-magic

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def maximum(a, b):
    result = b ^ ((a ^ b) & -(a < b))

    return result

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_maximum0(self):
        a, b = 0, 0
        expectedOutput = 0
        computedOutput = maximum(0,0)
        self.assertEqual(expectedOutput, computedOutput)

    def test_maximum1(self):
        a, b = 2, 3
        expectedOutput = 3
        computedOutput = maximum(0,0)
        self.assertEqual(expectedOutput, computedOutput)

    def test_maximum2(self):
        a, b = 3, 2
        expectedOutput = 3
        computedOutput = maximum(0,0)
        self.assertEqual(expectedOutput, computedOutput)
