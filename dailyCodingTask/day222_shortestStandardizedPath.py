# This problem was asked by Quora.
#
# Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.
#
# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

# ------------------------------------------------------------------------------

# from: https://blogs.msdn.microsoft.com/jeremykuhne/2016/04/21/path-normalization/
# Evaluating Relative Components
#
# As the path is processed, any components/segments that are comprised of a single or double period are evaluated.
# For a single period (.) the current segment is removed (as it means current directory).
# For a double period (..) the current segment and the parent segment are removed (as it means parent directory).
#
# Parent directories are only removed if they aren't past the "root" of the path.
# The root of the path depends on the type of path. It is the drive (C:\) for DOS paths,
# the server/share for UNCs (\\Server\Share), and the device path prefix for device paths (\\?\ or \\.\).

# Also check: https://www.geeksforgeeks.org/simplify-directory-path-unix-like/

# ------------------------------------------------------------------------------

import unittest
from dailyCodingTask.Stack import Stack

# ------------------------------------------------------------------------------

# *** idea ***
# todo prevent that the root is removed by too much ..
# todo implement tokenization
# todo put elements to a stack by consuming the tokens
# in case of . do nothing
# in case of .. remove last element
# else: add the element
#
# finally: reverse the stack-content, put delimiters (/() between the items, done :)

def getShortestStandardizedPath(inputPath):
    #print("\n")
    #print("############ getShortestStandardizedPath:", inputPath," ############")

    # split into tokens
    splittedString = inputPath.split("/")
    #print("splittedString:", splittedString)

    # if no tokens are left, return some error
    if len(splittedString) == 0:
        return "error"

    # smol helper-stack
    stack = Stack()

    # handle each token
    for elem in splittedString:
        #print("elem is:", elem)

        if elem == ".":
            # do nothing
            pass
            #print(" -> do nothing")
        elif elem == "..":
            #print(" -> stack pop")
            stack.pop()
        elif elem == "":
            #print(" -> empty string -> do nothing!")
            pass
        else:
            #print(" -> do something else; like push")
            stack.push(elem)

    # puzzle all pieces together
    currentStack = stack.__repr__()
    #print("\n before puzzling: stack content is:", currentStack, "size:", stack.currentSize())
    result = ""

    if currentStack == "":
        # result = "/"
        pass
    else:
        for elem in currentStack.split(";"):
            if elem is not "":
                result += "/" + elem

    # add one final slash
    result += "/"

    #print("result:", result) # todom remove

    return result

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
# commented until the implementation is working
    def test_QuoraExample(self):
        input  = "/usr/bin/../bin/./scripts/../"
        expectedOutput = "/usr/bin/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

    def test_simpleTests(self):
        input = "/"
        expectedOutput = "/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        # what about this? should it have some shortest path-representation?
        # I think not.
        input = ""
        expectedOutput = "/" # better return some error (of course, exception is much better)
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a"
        expectedOutput = "/a/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a/b/b/b"
        expectedOutput = "/a/b/b/b/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a/b/b/b/"
        expectedOutput = "/a/b/b/b/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        # double slashes
        input = "//"
        expectedOutput = "/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a//"
        expectedOutput = "/a/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
