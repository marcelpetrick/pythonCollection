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
    result = inputList[:1]
    #print("first item:", result)

    # in case of zero or one element, just return the resultList
    if(inputList.__len__() < 2):
        #print("if(inputList.__len__() < 2): do nothing: just return the elem or zero")
        result =  result[0] if result.__len__() == 1 else 0
    else:
        #print("more than one element in input!")

        # split the list into the first element and the rest
        head, rest = inputList[:1], inputList[1:]
        #print("head:", head, "rest:", rest) # todom: remove

        result = head[0]
        for element in rest:
            result = greatestCommonDivisor(result, element)
            #print("intermediate result:", result)

    print("getDivisors:", inputList, " --> final result:", result)
    return result

#------------------------------------------------------------------------------

class Testcase(unittest.TestCase):

    def test_greatestCommonDivisor(self):
        self.assertEqual(0, greatestCommonDivisor(0, 0))
        self.assertEqual(2, greatestCommonDivisor(0, 2))
        self.assertEqual(2, greatestCommonDivisor(2, 0))
        self.assertEqual(2, greatestCommonDivisor(2, 2))
        self.assertEqual(5, greatestCommonDivisor(5, 5))
        self.assertEqual(1, greatestCommonDivisor(3, 5))
        self.assertEqual(8, greatestCommonDivisor(24, 32))

    def test_getDivisors(self):
        # empty list
        self.assertEqual(0, getDivisors([]))
        # single element list with primes
        self.assertEqual(2, getDivisors([2]))
        self.assertEqual(3, getDivisors([3]))
        self.assertEqual(5, getDivisors([5]))
        # double list
        self.assertEqual(1, getDivisors([2,3]))
        # the task!
        self.assertEqual(14, getDivisors([42, 56, 14]))

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
print("## list: [42, 56, 14]")
print(getDivisors([42, 56, 14]))
print("-------- additional output: end ---------------------------------------------------------------------")
