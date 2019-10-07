# Maximum path sum II
#
# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this
# problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take
# over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

## ------------------------------------------------------------------------------

# idea: (TAKE OVER THE CODE FROM 018! and add a file-reader :))
# from bottom line to top: create for each entry the maximum path sum (msp): save inside the node then the maximum
# of both alternatives (except for the leaves, which are already "processed") plus the current node.
# Do this from down to top .. should work.

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# reusing the code would work like this
# from ProjectEuler import problem018_maximumPathSum as p018
# p018.processTriangle()
# but there are some flaws, because no proper separation of functionality .... so let us just copy and modify the stuff

# ------------------------------------------------------------------------------

def prepareInput():
    listOfNumbers = [[int(v) for v in line.split()] for line in open('problem067_triangle.txt')]
    return listOfNumbers

# ------------------------------------------------------------------------------

#print(prepareInput())

# algo: (loop from bottom-1 to top):
# 0. take line, go from left to right: put for each pair the maximum as new elem (not in place!)
# 1. add the line above to it

def processTriangle():
    # prearation: read input and reverse
    original = prepareInput()
    # reverse IN PLACE!
    original.reverse()
    print(original) # todo remove

    # prepare a temporary line
    initialLengthFirstRow = len(original[0])
    print("initialLengthFirstRow:", initialLengthFirstRow)

    lastLine = [0] * (initialLengthFirstRow + 1)
    print(lastLine)

    # sum up
    for index in range(len(original)):
        # create a new selected list out of the temporary
        pickedMaxList = []
        for listIndex in range(len(lastLine) - 1):
            a = lastLine[listIndex + 0]
            b = lastLine[listIndex + 1]
            pickedMaxList.append(max(a, b))
        print(pickedMaxList)

        # sum with temporary line
        lastLine = [x+y for x,y in zip(pickedMaxList, original[index])]
        print(lastLine)

    # first element should be now the result
    print("final state:", lastLine)

# -- test call --
processTriangle()

#------------------
# ..
# [7141, 7129]
# [7214, 7170]
# [7214]
# [7273]
# final state: [7273]

# Congratulations, the answer you gave to problem 67 is correct.
#
# You are the 88732nd person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%.
