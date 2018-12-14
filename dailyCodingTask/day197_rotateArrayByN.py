# This problem was asked by Amazon.
#
# Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def rotateArrayByK(array, k):
    # todo: implement
    return array

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_rotateArrayByK(self):
        self.assertEqual(True, [0, 1, 2] == rotateArrayByK([0, 1, 2], 0))
        self.assertEqual(True, [1, 2, 0] == rotateArrayByK([0, 1, 2], 1))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
