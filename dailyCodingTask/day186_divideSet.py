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
    # question: is the input a set or a list? does order matter? i think not

    # idea:
    # iterate over all elements of the input list: with each do a combination with all elements of the
    # current elements (are already sets) of the result set. then append this to the intermediate result set.
    # (repeat with all remaining elements.)
    # maybe: sort the list

    result = [[]] # the list which includes at least the empty list
    for elemFromOriginalList in inputList:
        #print("current item:", elemFromOriginalList) # todom remove
        newList = [] # totally empty in the beginning
        for elemIntermediateList in result:
            newItem = elemIntermediateList.copy()
            newItem.append(elemFromOriginalList)
            #print("newItem:", newItem)
            newList.append(newItem)
        #print("newList (applied item to old resultList):", newList)
        result = result + (newList)
        #print("current resultlist:", result)

    return result
#    def getKey(item):
#        return item[0]

#    return sorted(result, key=getKey)

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_createPowerset(self):

#        powerSet = createPowerset([1,2]) # expected [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] --> 6 elems
#        print("powerSet:", powerSet)

        print("powerSet [1]   ::", createPowerset([1]))
        print("powerSet [1,2] ::", createPowerset([1,2]))
        print("powerSet [1,3] ::", createPowerset([1,2,3]))

        hasEmptyList = createPowerset([1,2,3]).__contains__([5])
        print("has empty:", hasEmptyList)

        #---------- inline helper-function ----------
        def compareLists(list0, list1):
            ''' helper to compare if both compare the same elements (type and amount ..) '''

            if len(list0) != len(list1):
                return False

            returnValue = True
            for elem0 in list0:
                if elem0 not in  list1:
                    returnValue = False

            return returnValue

        #---------- end of inline helper-function ----------


        self.assertEqual(True, compareLists(createPowerset([1]),  [[], [1]]))
        self.assertEqual(False, compareLists([1],  [[], [1]]))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
