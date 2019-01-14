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
    # todo implement this

    splittedString = inputPath.split("/")
    print("splittedString:", splittedString)

    for elem in splittedString:
        if elem == ".":
            # do nothing
            print(" -> do nothing")
        elif elem == "..":
            print(" -> stack pop")
            pass # todo
        else:
            print(" -> do something else; like push")
    pass

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
# commented until the implementation is working
    # def test_QuoraExample(self):
    #     input  = "/usr/bin/../bin/./scripts/../"
    #     expectedOutput = "/usr/bin/"
    #     self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

    def test_simpleTests(self):
        input = "/"
        expectedOutput = "/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        # what about this? should it have some shortest path-representation?
        # I think not.
        input = ""
        expectedOutput = "error" # better return some error (of course, exception is much better)
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a"
        expectedOutput = "/a"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a/b/b/b"
        expectedOutput = "/a/b/b/b"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a/b/b/b/"
        expectedOutput = "/a/b/b/b/"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        # double slashes
        input = "//"
        expectedOutput = "//"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

        input = "/a//"
        expectedOutput = "/a//"
        self.assertEqual(expectedOutput, getShortestStandardizedPath(input))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
