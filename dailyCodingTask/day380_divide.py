# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Nextdoor.
#
# Implement integer division without using the division operator. Your function should return a tuple of
# (dividend, remainder) and it should take two numbers, the product and divisor.
#
# For example, calling divide(10, 3) should return (3, 1) since the divisor is 3 and the remainder is 1.
#
# Bonus: Can you do it in O(log n) time?

# ------------------------------------------------------------------------------

def divide(product, divisor):
    if divisor == 0:
        raise ValueError("div by zero not allowed")

    # TODO handle negative input
    # consider this: https://chortle.ccsu.edu/java5/Notes/chap09B/ch09B_17.html

    dividend, remainder = 0, 0
    while product > divisor:
        product -= divisor
        dividend += 1

    remainder = product

    return dividend, remainder


# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
import unittest
class Testcase(unittest.TestCase):

    def test_givenExample(self):
        expectedDiv, expectedRemainder = 3, 1
        computedDiv, computedRemainder = divide(10, 3)
        self.assertEqual(expectedDiv, computedDiv)
        self.assertEqual(expectedRemainder, computedRemainder)
    #
    # def test_getMedian(self):
    #     # TODO fix this
    #     # self.assertRaises(getMedian([]), ValueError)
    #
    #     self.assertEqual(getMedian([3]), 3)
    #
    #     self.assertEqual(getMedian([1, 2]), 1.5)
    #
    #     self.assertEqual(getMedian([1, 2, 3]), 2)
    #
    #     self.assertEqual(getMedian([10, 4, 3, 1]), 3.5)

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

