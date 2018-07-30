# This problem was asked by Facebook.
#
# Given a multiset of integers, return whether it can be partitioned into two subsets
# whose sums are the same.
#
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into
# {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
#
# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two
# subsets that add up to the same sum.

import unittest

# ------------------------------------------------------------------------------

def partitionIntoEqualSumMultiset(multiset):
    '''
    :param s - input string
    :param k - length in integer of desired substrings'''
    print("partitionIntoEqualSumMultiset called with: ", multiset)
    returnValue = False

    generateAllSubsetsForSet(multiset)

    return returnValue

# ------------------------------------------------------------------------------

def generateAllSubsetsForSet(multiset): # input-param multiset is a list
    ''' Generate all possible sets for the given list. '''
    resultSet = list() # set of lists or list of lists?
    # decision: set of lists!
    print("generateAllSubsetsForSet called with: ", multiset)

    for elem in multiset:
        resultSet.append([])
        print("up:", resultSet, " ::", len(resultSet))
        #copy = resultSet.copy()
        for index in range(len(resultSet)):
            print("current elem:", resultSet[index])
            resultSet[index].append(elem)
        #resultSet += copy
        print("down:", resultSet, " ::", len(resultSet))


    return resultSet

# ------------------------------------------------------------------------------

# class Testcase(unittest.TestCase):
#     def test0(self):
#         multiset = [15, 5, 20, 10, 35, 15, 10] # interpret the multiset as list .. {15, 5, 20, 10, 35, 15, 10}
#         expectedResult = True
#         output = partitionIntoEqualSumMultiset(multiset)
#         self.assertEqual(output, expectedResult)
#         print(" --> input", multiset, "yielded result:", output)
#
#     def test1(self):
#         multiset = [15, 5, 20, 10, 35]
#         expectedResult = False
#         output = partitionIntoEqualSumMultiset(multiset)
#         self.assertEqual(output, expectedResult)
#         print(" --> input", multiset, "yielded result:", output)
#
# # ------------------------------------------------------------------------------
#
# # ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     unittest.main()

multiset = [1, 2, 3, 4]
partitionIntoEqualSumMultiset(multiset)
