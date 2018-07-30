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
import copy

# ------------------------------------------------------------------------------

def partitionIntoEqualSumMultiset(multiset):
    '''
    :param s - input string
    :param k - length in integer of desired substrings'''
    print("partitionIntoEqualSumMultiset called with: ", multiset)
    returnValue = False

    output = generateAllSubsetsForSet(multiset)

    print("final set:", output)

    return returnValue

# ------------------------------------------------------------------------------

def generateAllSubsetsForSet(multiset): # input-param multiset is a list
    ''' Generate all possible sets for the given list. '''

    print("generateAllSubsetsForSet called with: ", multiset)

    resultSet = list() # set of lists or list of lists?
    resultSet.append([])

    for elem in multiset:
        print("up:", resultSet, " ::", len(resultSet))
        #original = list(resultSet) # the original content has to be retained
        original = copy.deepcopy(resultSet) # ATTENTION: just this works, not just cloning or copying the list (of lists) ..
        print("original has x elems: ", original.__len__(), ":", original)

        for index in range(len(resultSet)):
            print("current elem:", resultSet[index])
            resultSet[index].append(elem) # immediately change the items
            print("\t after change elem:", resultSet[index])

        print("original has x elems: ", original.__len__(), ":", original)
        print("resultlist has x elems: ", resultSet.__len__(), ":", resultSet)

        resultSet = resultSet + original # add the copied initial list
        print("appended version has x elems: ", resultSet.__len__(), "--->", resultSet)
        print("----------------------")

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

multiset = [1, 2, 3]
partitionIntoEqualSumMultiset(multiset)
# expected: [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]
