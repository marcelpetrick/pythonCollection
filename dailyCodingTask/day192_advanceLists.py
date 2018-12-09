# This problem was asked by Google.
#
# You are given an array of nonnegative integers. Let's say you start at the beginning of the array
# and are trying to advance to the end. You can advance at most, the number of steps that you're currently on.
# Determine whether you can get to the end of the array.
#
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.
#
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
#
# ---------------------------------
#
# idea: solve this recursively.
# end of array: last element; value does not matter
# begin of array: first element
#
# if canAdvanceToEnd([n]): return true, because at the end of the array
# else: for(all possible reachable starting-elements for the remaining list): call  canAdvanceToEnd([restList with start])
#
# since this is recursive, it will do depth-first-search
#
# stop if one of the calls returns true (break early?)
#
# ---------------------------------


def canAdvanceToEnd(inputArray):
    if(len(inputArray) <= 1):
        return True
    else:
        # split list in head and remainder
        first, rest = inputArray[0], inputArray[1:]

        # todo
        return False

#----------------

def helper(inputArray):
    result = canAdvanceToEnd(inputArray)
    print("canAdvanceToEnd(", inputArray, ") returns:", result)
    return

# ----------------

helper([])

helper([1])