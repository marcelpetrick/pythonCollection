# This problem was asked by Nvidia.
#
# Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.

# ------------------------------------------------------------------------------

# idea: some XOR-magic

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def maximum(a, b):
    pass

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_maximum(self):
        a, b = 0, 0
        expectedOutput = 0
        computedOutput = maximum(0,0)
        self.assertEqual(expectedOutput, computedOutput)
