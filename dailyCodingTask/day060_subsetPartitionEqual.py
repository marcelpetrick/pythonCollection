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
    returnValue = None

    # first note: if the multiset has odd sum, then it can't be partitioned into two equal sets!
    sumOfMultiset = sum(multiset)
    print("sumOfMultiset: ", sumOfMultiset)
    if(sumOfMultiset %2 == 1):
        print("no fitting sum -> no luck")
        returnValue = False
    else:
        powerset = generatePowersetForSet(multiset)
        print("final set has", powerset.__len__(), "elements:", powerset)

        for set in powerset:
            if(sum(set) * 2 == sumOfMultiset):
                print("this set", set, "is correct partition of the set", multiset)
                returnValue = True
                break

    return returnValue

# ------------------------------------------------------------------------------

def generatePowersetForSet(multiset): # input-param multiset is a list
    ''' Generate all possible sets for the given list. '''

    #print("generatePowersetForSet called with: ", multiset)

    resultSet = list()
    resultSet.append([])

    for elem in multiset:
        #print("up:", resultSet, " ::", len(resultSet))
        #original = list(resultSet) # the original content has to be retained
        original = copy.deepcopy(resultSet) # ATTENTION: just this works, not just cloning or copying the list (of lists) ..
        #print("original has x elems: ", original.__len__(), ":", original)

        for index in range(len(resultSet)):
            #print("current elem:", resultSet[index])
            resultSet[index].append(elem) # immediately change the items
            #print("\t after change elem:", resultSet[index])

        #print("original has x elems: ", original.__len__(), ":", original)
        #print("resultlist has x elems: ", resultSet.__len__(), ":", resultSet)

        resultSet = resultSet + original # add the copied initial list
        #print("appended version has x elems: ", resultSet.__len__(), "--->", resultSet)
        #print("----------------------")

    return resultSet

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test0_partitionIntoEqualSumMultiset(self):
        multiset = [15, 5, 20, 10, 35, 15, 10] # interpret the multiset as list .. {15, 5, 20, 10, 35, 15, 10}
        expectedResult = True
        output = partitionIntoEqualSumMultiset(multiset)
        self.assertEqual(output, expectedResult)
        print(" --> input", multiset, "yielded result:", output)

    def test1_partitionIntoEqualSumMultiset(self):
        multiset = [15, 5, 20, 10, 35]
        expectedResult = False
        output = partitionIntoEqualSumMultiset(multiset)
        self.assertEqual(output, expectedResult)
        print(" --> input", multiset, "yielded result:", output)

    def test2_partitionIntoEqualSumMultiset(self):
        multiset = [1, 2, 3, 6]
        expectedResult = True
        output = partitionIntoEqualSumMultiset(multiset)
        self.assertEqual(output, expectedResult)
        print(" --> input", multiset, "yielded result:", output)

    # test the "Potenzmenge"-generator (power set)
    # proves everything, since recursive
    def test0_generateAllSubsetsForSet(self):
        set = []
        expectedResult = [[]]
        output = generatePowersetForSet(set)
        self.assertEqual(output.sort(), expectedResult.sort()) # sort to prevent that
        #print("test0_generateAllSubsetsForSet", set, "yielded result:", output)

    def test1_generateAllSubsetsForSet(self):
        set = [1]
        expectedResult = [[], [1]]
        output = generatePowersetForSet(set)
        self.assertEqual(output.sort(), expectedResult.sort())
        #print("test1_generateAllSubsetsForSet", set, "yielded result:", output) # can the name of the function be printed?

    def test2_generateAllSubsetsForSet(self):
        set = [1, 2]
        expectedResult = [[], [1], [2], [1,2]]
        output = generatePowersetForSet(set)
        self.assertEqual(output.sort(), expectedResult.sort())
        #print("test2_generateAllSubsetsForSet", set, "yielded result:", output)

    def test3_generateAllSubsetsForSet(self):
        set = [1, 2, 3]
        expectedResult = [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]
        output = generatePowersetForSet(set)
        self.assertEqual(output.sort(), expectedResult.sort())
        #print("test3_generateAllSubsetsForSet", set, "yielded result:", output)

    def test4_generateAllSubsetsForSet(self):
        set = [3, 3, 3]
        expectedResult = [[3, 3, 3], [3, 3], [3, 3], [3, 3], [3], [3], [3], []] # 1, 3, 3, 1 ... binomial numbers :)
        output = generatePowersetForSet(set)
        self.assertEqual(output.sort(), expectedResult.sort())
        #print("test4_generateAllSubsetsForSet", set, "yielded result:", output)

# # ------------------------------------------------------------------------------
#
# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

#multiset = [1, 2, 3]
#partitionIntoEqualSumMultiset(multiset)
# expected: [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]

