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

# idea: TODO

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

def lookAndSay(n):
    # todo return the nth term of the sequence

    if(n == 1):
        return 1

    pass

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        n = 1
        expectedOutput = 1
        computedOutput = lookAndSay(n)
        self.assertEqual(expectedOutput, computedOutput)
