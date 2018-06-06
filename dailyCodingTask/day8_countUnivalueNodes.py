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

class TreeNode:
    value = 0
    left = None
    right = None

    def __init__(self, value = -1, leftNode = None, rightNode = None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def isUnival(self):
        # todo: not complete: it is not enough that both children are unival, but also have the same value!
        return (self.leftNode is None) AND (self.rightNode is None) # OR (self.leftNode.isUnival() AND self.rightNode.isUnival()))
        #return True


class ProductListTestCase(unittest.TestCase):
    ''' Tests for day8.py '''

    def testUnivalDetection0(self):
        inputTree = TreeNode(1, None, None)
        self.assertTrue(inputTree)
#        print("countDecodePossibilities(" + inputString + ") = " + str(countDecodePossibilities(inputString)))

    def testUnivalDetection1(self):
        inputTree = TreeNode(1, TreeNode(0, None, None), None)
        self.assertFalse(inputTree)

    def testUnivalDetection2(self):
        inputTree = TreeNode(1, None, TreeNode(0, None, None))
        self.assertFalse(inputTree)

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()