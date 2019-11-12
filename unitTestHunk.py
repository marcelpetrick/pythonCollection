# description:
# TODO state the problem here

# ------------------------------------------------------------------------------

# idea:
# TODO describe the approach wanted to solve the task

# ------------------------------------------------------------------------------

# dummy function
def lookAndSay(n):
    # todo description of the method

    if n == 1:
        return 1

    pass

# ------------------------------------------------------------------------------

# proper unit-test

import unittest
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        n = 1
        expectedOutput = 1
        computedOutput = lookAndSay(n)
        self.assertEqual(expectedOutput, computedOutput)

    def test_expectFail(self):
        self.assertFalse(1 < 0, "hell has frozen over")

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
