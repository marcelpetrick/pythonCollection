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


#------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    pass
    
#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
