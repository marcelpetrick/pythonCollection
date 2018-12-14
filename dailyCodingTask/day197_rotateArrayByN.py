# This problem was asked by Amazon.
#
# Given an array and a number k that's smaller than the length of the array,
# rotate the array to the right k elements in-place.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def rotateByOne(array):
    lengthOfArray = len(array)
    if lengthOfArray == 0:
        return array

    firstElenm = array[0]
    for index in range(0, lengthOfArray - 1):
        array[index] = array[index + 1]

    array[lengthOfArray - 1] = firstElenm

    return array

# ------------------------------------------------------------------------------

def rotateArrayByK(array, k):
    #print("rotateArrayByK: ", array, "k=", k)
    for applications in range(0, k):
        array = rotateByOne(array)
        #print("\t array:", array)

    return array

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_rotateByOne(self):
        self.assertEqual(True, [] == rotateByOne([]))
        self.assertEqual(True, [1] == rotateByOne([1]))
        self.assertEqual(True, [1, 0] == rotateByOne([0, 1]))
        self.assertEqual(True, [1, 2, 0] == rotateByOne([0, 1, 2]))

    def test_rotateArrayByK(self):
        self.assertEqual(True, [0, 1, 2] == rotateArrayByK([0, 1, 2], 0))
        self.assertEqual(True, [1, 2, 0] == rotateArrayByK([0, 1, 2], 1))
        self.assertEqual(True, [2, 0, 1] == rotateArrayByK([0, 1, 2], 2))

        self.assertEqual(True, [0, 1, 2, 4] == rotateArrayByK([0, 1, 2, 4], 4))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
