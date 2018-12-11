# This problem was asked by Microsoft.
#
# Given an array of positive integers, divide the array into two subsets such that the difference
# between the sum of the subsets is as small as possible.
#
# For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which
# has a difference of 5, which is the smallest possible difference.
#
# ---------------------------------
#
# idea: solve this recursively.
#
# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def createPowerset(inputList):
    # question: is the input a seat or a list? does order matter? i think not
    pass

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_createPowerset(self):
        print("test 1 ")
        pass
    #     # empty or one item lists are always true
    #     self.assertEqual(True, canAdvanceToEnd([]))
    #     self.assertEqual(True, canAdvanceToEnd([1]))
    #     self.assertEqual(True, canAdvanceToEnd([31415]))
    #
    # def test_canAdvanceList1(self):
    #     # one jump needed to the end: but is the step-width enough?
    #     self.assertEqual(False, canAdvanceToEnd([0, 1]))
    #     self.assertEqual(True, canAdvanceToEnd([1, 0]))
    #
    #     self.assertEqual(False, canAdvanceToEnd([1, 0, 0]))
    #     self.assertEqual(True, canAdvanceToEnd([2, 0, 0]))
    #
    # def test_canAdvanceList_givenSamples(self):
    #     # a check with repeated jumps
    #     self.assertEqual(True, canAdvanceToEnd([1, 3, 1, 2, 0, 1]))
    #     self.assertEqual(False, canAdvanceToEnd([1, 2, 1, 0, 0]))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
