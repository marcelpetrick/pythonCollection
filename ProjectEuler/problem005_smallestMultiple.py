# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# ------------------------------------------------------------------------------
import unittest

# ------------------------------------------------------------------------------

def smallestMultiple(start, end):
    # todo first check if start <= end
    if start > end:
        return None

    # todo for each of the numbers in the range, do some prime-factorization
    # todo put them into some dictionary, where just the exponent of each prime-factor is saved: like for 8 == 2**3
    # mulitply all entries from the dictionary - the result is the wanted number

    return None

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test(self):
        self.assertIsNone(smallestMultiple(2,1)) # should return None, because not possible
        self.assertEqual(1, smallestMultiple(1,1))
        self.assertEqual(20, smallestMultiple(4, 5))
        self.assertEqual(2520, smallestMultiple(1, 10)) # from the task

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# todo add here code for
smallestMultiple(1, 20)