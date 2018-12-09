# This problem was asked by Google.
#
# You are given an array of nonnegative integers. Let's say you start at the beginning of the array
# and are trying to advance to the end. You can advance at most, the number of steps that you're currently on.
# Determine whether you can get to the end of the array.
#
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.
#
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
#
# ---------------------------------
#
# idea: solve this recursively.
# end of array: last element; value does not matter
# begin of array: first element
#
# if canAdvanceToEnd([n]): return true, because at the end of the array
# else: for(all possible reachable starting-elements for the remaining list): call  canAdvanceToEnd([restList with start])
#
# since this is recursive, it will do depth-first-search
#
# stop if one of the calls returns true (break early?)
#
# ---------------------------------

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def canAdvanceToEnd(inputArray):
    if(len(inputArray) <= 1):
        return True
    else:
        numberOfAllowedSteps = inputArray[0]
        #print("allowed steps:", numberOfAllowedSteps)

        # assume the number is bigger 0
        for step in range(1, numberOfAllowedSteps + 1): # ATTENTION: big fat error, range does not include the end!
            restList = inputArray[step:]
            result = canAdvanceToEnd(restList)

            if(result == True):
                #print("found one! :)")
                return True
        else:
            #print("did all steps - dough!")
            return False


        return False

#----------------

def helper(inputArray):
    result = canAdvanceToEnd(inputArray)
    print("canAdvanceToEnd(", inputArray, ") returns:", result)
    return

# ----------------

# helper([])
#
# helper([1])
#
# helper([1, 1]) # should return True
#
# helper([0, 1]) # should return False
#
# helper([1, 3, 1, 2, 0, 1])
#
# helper([1, 2, 1, 0, 0])

# # test - should print nothing, because the range is empty
# print("###################### test #############")
# for x in range(1, 0):
#     print(x)
# else:
#     print("else of the 'for'")

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_canAdvanceList0(self):
        # empty or one item lists are always true
        self.assertEqual(True, canAdvanceToEnd([]))
        self.assertEqual(True, canAdvanceToEnd([1]))
        self.assertEqual(True, canAdvanceToEnd([31415]))

    def test_canAdvanceList1(self):
        # one jump needed to the end: but is the step-width enough?
        self.assertEqual(False, canAdvanceToEnd([0, 1]))
        self.assertEqual(True, canAdvanceToEnd([1, 0]))

        self.assertEqual(False, canAdvanceToEnd([1, 0, 0]))
        self.assertEqual(True, canAdvanceToEnd([2, 0, 0]))

    def test_canAdvanceList_givenSamples(self):
        # a check with repeated jumps
        self.assertEqual(True, canAdvanceToEnd([1, 3, 1, 2, 0, 1]))
        self.assertEqual(False, canAdvanceToEnd([1, 2, 1, 0, 0]))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
