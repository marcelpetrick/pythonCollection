# Integer right triangles
#
# Problem 39
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# ------------------------------------------------------------------------------

# idea:
# create all possible compositions, use pythagorean theorem to check

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def checkTriangleForBeingRightAngled(a, b, c):
    # find the biggest by creating a sorted list
    sl = sorted([a, b, c])
    isRightAngled = sl[0] ** 2 + sl[1] ** 2 == sl[2] ** 2
    return isRightAngled

# ------------------------------------------------------------------------------
# print(checkTriangleForBeingRightAngled(20, 48, 52))
# print(checkTriangleForBeingRightAngled(20, 50, 50))
# ------------------------------------------------------------------------------

def findAllRightAngledPartitionsOfPerimeter(perimeter):
    result = set()
    for a in range(1, perimeter - 1): # edges cant be zero, so from 1 to perimeter-2
        for b in range(1, perimeter - a):
            c = perimeter - a - b
            # note: this simple approach also creates partitions like 1,2,3 and 1,3,2 for 6 - which are identical and therefore don't have to be checked multiple times ..
            #print(a,b,c, "=", a+b+c)

            if(checkTriangleForBeingRightAngled(a, b, c)):
                result.add(tuple(sorted([a, b, c])))

    #print(perimeter, " -->", result)
    return result

# ------------------------------------------------------------------------------

# import time
# currentTime = time.time()
# findAllRightAngledPartitionsOfPerimeter(120)
# print("computing all right-angled partitions of 120 took", time.time() - currentTime, "s")
# computing all right-angled partitions of 120 took 0.0 s
# ------------------------------------------------------------------------------

def findMaxPartitions(inclusiveLimit):
    # init
    maxLen = -1
    bestPerimeter = -1

    # loop
    for perimeter in range(3, inclusiveLimit + 1):
        amountResults = len(findAllRightAngledPartitionsOfPerimeter(perimeter))

        if amountResults > maxLen:
            maxLen = amountResults
            bestPerimeter = perimeter

    result = findAllRightAngledPartitionsOfPerimeter(bestPerimeter)
    print("bst perimeter would be ", bestPerimeter, " with ", len(result), " --> ", result)

# ------------------------------------------------------------------------------

import time
currentTime = time.time()
findMaxPartitions(1000)
print("computing the euler-result took", time.time() - currentTime, "s")
#

# ------------------------------------------------------------------------------

import unittest
class Testcase(unittest.TestCase):
    def test_isRightAngled(self):
        self.assertEqual(True, checkTriangleForBeingRightAngled(20, 48, 52))
        self.assertEqual(True, checkTriangleForBeingRightAngled(24, 45, 51))
        self.assertEqual(True, checkTriangleForBeingRightAngled(30, 40, 50))
        self.assertEqual(False, checkTriangleForBeingRightAngled(30, 42, 48))

    def test_properPartitions(self):
        testSet = set()
        testSet.add((20, 48, 52))
        testSet.add((24, 45, 51))
        testSet.add((30, 40, 50))

        self.assertEqual(testSet, findAllRightAngledPartitionsOfPerimeter(120))
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

