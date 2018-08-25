# This problem was asked by Google.
#
# Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed
# to make the string valid (i.e. each open parenthesis is eventually closed).
#
# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2,
# since we must remove all of them.

# ------------------------------------------------------------------------------

# idea:
# parentheses come in pairs. So a "closed" valid expression has the value 0 if ( stands for +1 and ) for -1.
# values below zero are not possible: the counter should be then increased by one.
# additionally after parsing the whole input-string, the remaining (positive) value has to be added to the counter.
# counter gives then the amount of minimum parentheses to remove

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def computeMinimumNumberOfParenthesesToBeRemoved(input):
    # todo maybe check for invalid input which does not consist of ( or ) ..

    parenthesesToRemove = 0
    counter  = 0
    while input.__len__() > 0:
        head = input[0:1]
        input = input[1:]
        #print("this run:", head, "+", input)
        if head == "(":
            counter += 1 # todo again, check how to increment instead of doing this weird "+= 1 thing"
        elif head == ")":
            counter -= 1
            if counter < 0: # should be just with -1 the one, lower is not possible
                counter = 0
                parenthesesToRemove += 1

        #print("counter:", counter)
        #print("parenthesesToRemove:", parenthesesToRemove)

    #print("end of function!")
    return parenthesesToRemove + counter

#------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_computeMinimumNumberOfParenthesesToBeRemoved(self):
        self.assertEqual(0, computeMinimumNumberOfParenthesesToBeRemoved(""))
        self.assertEqual(1, computeMinimumNumberOfParenthesesToBeRemoved("("))
        self.assertEqual(1, computeMinimumNumberOfParenthesesToBeRemoved(")"))
        self.assertEqual(0, computeMinimumNumberOfParenthesesToBeRemoved("()"))
        # todo add more

    # For example, given the string "()())()", you should return 1.
    def test_fromTask0(self):
        self.assertEqual(1, computeMinimumNumberOfParenthesesToBeRemoved("()())()"))

    # Given the string ")(", you should return 2, since we must remove all of them.
    def test_fromTask1(self):
        self.assertEqual(2, computeMinimumNumberOfParenthesesToBeRemoved(")("))

#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
