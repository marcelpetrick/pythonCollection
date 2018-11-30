# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given n numbers, find the greatest common denominator between them.
#
# For example, given the numbers [42, 56, 14], return 14.


# ------------------------------------------------------------------------------

# idea:
# * for each element, determine the divisor and store them
# * check for each possible divisor then the biggest shared quantity
# * multiply all the found divisors in their quantity -> result

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def getDivisors(list):
    list = []

    return list

#------------------------------------------------------------------------------

class Testcase(unittest.TestCase):

    def test_getDivisors(self):
        # empty list
        self.assertEqual([], getDivisors([]))
        # single element list with primes
        self.assertEqual([2], getDivisors([2]))
        self.assertEqual([5], getDivisors([5]))
        self.assertEqual([5], getDivisors([5]))
        # double list
        self.assertEqual([2,3], getDivisors([2,3]))

    # def test_computeMinimumNumberOfParenthesesToBeRemoved(self):
    #     self.assertEqual(0, computeMinimumNumberOfParenthesesToBeRemoved(""))
    #     self.assertEqual(1, computeMinimumNumberOfParenthesesToBeRemoved("("))
    #     self.assertEqual(1, computeMinimumNumberOfParenthesesToBeRemoved(")"))
    #     self.assertEqual(0, computeMinimumNumberOfParenthesesToBeRemoved("()"))
    #     self.assertEqual(3, computeMinimumNumberOfParenthesesToBeRemoved(")))"))
    #     self.assertEqual(3, computeMinimumNumberOfParenthesesToBeRemoved("((("))
    #     # todo add more
    #
    # # For example, given the string "()())()", you should return 1.
    # def test_fromTask0(self):
    #     self.assertEqual(1, computeMinimumNumberOfParenthesesToBeRemoved("()())()"))
    #
    # # Given the string ")(", you should return 2, since we must remove all of them.
    # def test_fromTask1(self):
    #     self.assertEqual(2, computeMinimumNumberOfParenthesesToBeRemoved(")("))

#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


#------------------------------------------------------------------------------
print("-------- additional output: begin -------------------------------------------------------------------")
print("test")
print("-------- additional output: end ---------------------------------------------------------------------")