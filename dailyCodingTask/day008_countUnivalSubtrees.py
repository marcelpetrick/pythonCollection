import unittest

# This problem was asked by Google.
#
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

# a tree consists of nodes with up to two children.

# should be: TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(1,TreeNode(1),TreeNode(1)), TreeNode(0)))

#------------------------------------------------------------------------------

class TreeNode:
    def __init__(self, value = -1, leftNode = None, rightNode = None):
        # todo assert that value is just (0,1) - else throw an exception
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def isUnival(self):
        ''' needed to check for each node if that is a valid subtree '''
        # it is not enough that both children are unival, but also have the same value!
        returnValue = False
        returnValue = returnValue or (self.leftNode is None) and (self.rightNode is None)
        if (self.leftNode is not None) and (self.rightNode is not None):
            returnValue = returnValue or (self.leftNode.isUnival() and self.rightNode.isUnival() and self.leftNode.value == self.rightNode.value)

        #print(returnValue)
        return returnValue

    def countUnivalTrees(self):
        ''' this was the initial task of the exercise :') '''
        returnValue = 0
        if self.isUnival():
            returnValue += 1
        if self.leftNode is not None:
            returnValue += self.leftNode.countUnivalTrees()
        if self.rightNode is not None:
            returnValue += self.rightNode.countUnivalTrees()

        #print(returnValue)
        return returnValue

    def getTreeString(self):
        ''' recursive iteration '''
        returnValue = str(self.value)

        if self.leftNode is not None:
            returnValue += "(" + self.leftNode.getTreeString() + ")"

        if self.rightNode is not None:
            returnValue += "[" + self.rightNode.getTreeString() + "]"

        #print(returnValue)
        return returnValue

#------------------------------------------------------------------------------

class UnivalTestcase(unittest.TestCase):
    ''' Tests for day008_countUnivalSubtrees.py '''

    def testUnivalDetection0(self):
        inputTree = TreeNode(1)
        self.assertTrue(inputTree.isUnival())

    def testUnivalDetection1(self):
        inputTree = TreeNode(1, TreeNode(0))
        #print(inputTree.getTreeString())
        self.assertFalse(inputTree.isUnival())

    def testUnivalDetection2(self):
        inputTree = TreeNode(1, TreeNode(0), TreeNode(0))
        self.assertTrue(inputTree.isUnival())

    def testUnivalDetection3(self):
        inputTree = TreeNode(1, TreeNode(0), TreeNode(1))
        #print(inputTree.countUnivalTrees())
        self.assertFalse(inputTree.isUnival())
        self.assertEquals(2, inputTree.countUnivalTrees()) # done in that case: 2

    # todo: add some tests for the count-method ... or even better: put them into the existing methods for unival-test!

#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


# just for additional testing
#print("single item tree:", TreeNode(1).getTreeString())
#print("tree with two children:", TreeNode(0, TreeNode(1), TreeNode(2)).getTreeString())

print("######################################################")
givenTree = TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(1,TreeNode(1),TreeNode(1)), TreeNode(0)))
print(givenTree.getTreeString())
print(givenTree.countUnivalTrees())
