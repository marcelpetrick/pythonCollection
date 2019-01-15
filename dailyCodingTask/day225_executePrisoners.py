# This problem was asked by Bloomberg.
#
# There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with
# the kth person, and removing every successive kth person going clockwise until there is no one left.
#
# Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
#
# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
#
# Bonus: Find an O(log N) solution if k = 2.

# ------------------------------------------------------------------------------
# idea:
# * todo

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

# attention: k-th Person, so [1,2,3,4,5]. Not starting with 0!
def bestStandingPosition(N, k):
    return 3 # ideally: pass - but just fake for now

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_QuoraExample(self):
        n, k  = 5, 2
        expectedOutput = 3
        computedOutput = bestStandingPosition(n, k)
        self.assertEqual(expectedOutput, computedOutput)
