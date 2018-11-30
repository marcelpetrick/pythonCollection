# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given n numbers, find the greatest common denominator between them.
#
# For example, given the numbers [42, 56, 14], return 14.


# ------------------------------------------------------------------------------

# idea:
# * for each element, determine the divisor and store them
# * check for each possible divisor then the biggest shared quantity
# * multiply all the found divisors in their quantity -> result

# other idea: apply the gdc to the first two numbers. then compute gdc of the result and all following elements (iteratively).

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def greatestCommonDivisor(a, b):
    if(a == 0): # check if a is zero: if yes, then return b, because it is the biggest divisor
        return b

    return greatestCommonDivisor(b % a, a)

#------------------------------------------------------------------------------

def getDivisors(inputList):
    resultList = []

    # in case of zero or one element, just return the resultList
    if(inputList.__len__() < 2):
        print("if(inputList.__len__() < 2): do nothing")
        resultList = inputList
        pass
    else:
        print("more than one element in input!")

        # split the list into the first element and the rest
        head, rest = inputList[:1], inputList[1:]
        print("head:", head, "rest:", rest) # todom: remove

        result = head
        for element in rest:
            result = greatestCommonDivisor(result, element)
            print("intermediate result:", result)


    return resultList

#------------------------------------------------------------------------------

class Testcase(unittest.TestCase):

    def test_greatestCommonDivisor(self):
        self.assertEqual(0, greatestCommonDivisor(0, 0))
        self.assertEqual(2, greatestCommonDivisor(0, 2))
        self.assertEqual(2, greatestCommonDivisor(2, 0))
        self.assertEqual(2, greatestCommonDivisor(2, 2))
        self.assertEqual(5, greatestCommonDivisor(5, 5))
        self.assertEqual(1, greatestCommonDivisor(3, 5))
        pass

    def test_getDivisors(self):
        # empty list
        self.assertEqual([], getDivisors([]))
        # single element list with primes
        self.assertEqual([2], getDivisors([2]))
        self.assertEqual([5], getDivisors([5]))
        self.assertEqual([5], getDivisors([5]))
        # double list
        self.assertEqual([2,3], getDivisors([2,3]))

#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()


#------------------------------------------------------------------------------
print("-------- additional output: begin -------------------------------------------------------------------")
print("## first some empty list")
print(getDivisors([]))
print("## list with two elems")
print(getDivisors([3]))
print("## list with three elems")
print(getDivisors([2, 4, 6]))
print("-------- additional output: end ---------------------------------------------------------------------")
