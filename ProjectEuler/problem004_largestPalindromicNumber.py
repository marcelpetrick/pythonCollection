# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

# idea: try to check downwards: use two loops over the input; starting with the biggest possible number from the amount of digits
def findLargestPalindromicNumberFromTwoXDigitNumbers(digits):
    pass

# ------------------------------------------------------------------------------

# todo rename the function name: e at suffix missing
def isPalindrom(input):
    #print("-----------------------")
    #print("isafdasf called with", input)
    if input < 0: # all negative numbers are not palindromic
        return False
    elif input < 10: # all single digit numbers are palindromic
        return True
    else: # first is equal the last digit? then check for the inner core
        stringifiedNumber = str(input)
        #print(stringifiedNumber[0], stringifiedNumber[-1]) # -1 is last elem
        if stringifiedNumber[0] == stringifiedNumber[-1]:
            #print("same!")
            substring = stringifiedNumber[1:-1]
            if substring.__len__() > 0:
                #print("call with substring", substring, "the function")
                return isPalindrom(int(substring))
            else:
                #print("no more stuff left - return True")
                return True
        else:
            #print("begin and end not equal :'(")
            return False

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(True, isPalindrom(1))
        self.assertEqual(True, isPalindrom(11))
        self.assertEqual(False, isPalindrom(12))
        self.assertEqual(True, isPalindrom(121))
        self.assertEqual(True, isPalindrom(1221))
        self.assertEqual(False, isPalindrom(123421))
        self.assertEqual(True, isPalindrom(123321))
        self.assertEqual(False, isPalindrom(-2))

    def test_largestPalindromic(self):
        print("dsfsafsadf")
        self.assertEqual(9009, findLargestPalindromicNumberFromTwoXDigitNumbers(2))

# ------------------------------------------------------------------------------

# should return 91x99 --> 9009
#findLargestPalindromicNumberFromTwoXDigitNumbers(2)

#print("##################################")
#isPalindrom(123421)