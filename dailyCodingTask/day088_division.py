# This question was asked by ContextLogic.
#
# Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def divide(a,b):
    if b == 0:
        return None

    quotient = 0
    while a >= b:
        a -= b
        quotient += 1

    return quotient

#------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(0, divide(0, 3))
        self.assertEqual(2, divide(4, 2))
        self.assertEqual(2, divide(5, 2))
        self.assertEqual(3, divide(6, 2))
        self.assertEqual(None, divide(5, 0))

#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
