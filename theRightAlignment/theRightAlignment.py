# idea:
# * read the whole file given by param
# * find the length of the longest line
# * add for each line enough whitespace (spaces, of course! not tabs) to make them all aligned to the right
# * weird 80 character-rules can be just satisfied if the longest line would be <= 80 chars

# ------------------------------------------------------------------------------

# motivation:
#  a small test-balloon during lunch-break about code-styling and if we should use, for instance, clang-format,
#  resulted in a argument. if applying a "one rule fits the whole team" is proper and good or not. or if your
#  personal way to write code is suppressed. my argument was then, that if we have no codes-styling-agreement, i could
#  also commit my new files with proper right-alignment, or? since it is not forbidden or wanted to have left-aligned
#  style.
#
#  of course, i doubt that i would pull this of (professionalism), but the idea sparked my interest. shouldn't be too
#  hard to write a python-script which can be used with xargs/parallel on bash on all the touched files in the last
#  git-commit.

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def determineMaxLineLength(filePath):
    print("determineMaxLineLength: handle now:", filePath)

    # todo rewrite with RAII-opening&closing ..
    file = open(filePath, 'r')

    maxLineLength = -1

    # read content
    for line in file.readlines():
        currentLength = len(line.rstrip()) # check the stripped length (just trailing whitespce)

        if currentLength > maxLineLength:
            maxLineLength = currentLength

    file.close() # needed, else complains about left-open file ..

    return maxLineLength

# ------------------------------------------------------------------------------

def padFile(filePath, maxLineLength):
    # pad the file with ljust to the left ...
    # Attention: maybe exclude lines like #include or other macros

    print("padFile: handle now:", filePath)

    # todo add code

# ----------------- main function -----------------
def main():
    import sys

    # get the parameters
    if len(sys.argv) == 2:
        fileToProcessPath = sys.argv[1]
    else:
        raise Exception("Not enough parameters specified: first must be fileToProcessPath.")

    # first determine the maximum
    maxLength = determineMaxLineLength(fileToProcessPath)
    print("maximum line length of", fileToProcessPath, "is", maxLength, "chars")

    # then adjust the file
    padFile(fileToProcessPath, maxLength)

    # todo add the real functionality

# ----------------- execution -----------------

if __name__ == "__main__":
    main()

# todo: idea: to make unit-tests and the real usage work at the same time, parse the argument1 and then select the correct subsequent calls

# ------------------------------------------------------------------------------
# unit-tests
# ------------------------------------------------------------------------------
import unittest
class Testcase(unittest.TestCase):
    def test_determineMaxLineLength(self):
        fileToCheck = "testFile0.txt"
        maxLineLength = determineMaxLineLength(fileToCheck)
        self.assertEqual(40, maxLineLength, "detected maximum line length is not fitting to the expectation")

    def test_padFile(self):
        print("todo: implement")

# ------------------------------------------------------------------------------

# # ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     unittest.main()
