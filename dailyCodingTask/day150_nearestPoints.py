# This problem was asked by LinkedIn.
#
# Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
#
# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].

# ------------------------------------------------------------------------------

# idea:

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

#------------------------------------------------------------------------------

class Testcase(unittest.TestCase):

    def test_foo(self):
        pass

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
print("-------- additional output ----------------------------------------------------------------------")
print("test")
#print("foo")
#print("globals:", globals())
#print("locals:", locals())
