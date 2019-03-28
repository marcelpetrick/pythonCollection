# description: state the problem here

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

    def test_expectFail(self):
        self.assertFalse(1 < 0, "hell has frozen over")
