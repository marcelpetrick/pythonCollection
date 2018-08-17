# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def findLargestPalindromicNumberFromTwoXDigitNumbers(digits):
    pass

# ------------------------------------------------------------------------------

def isPalindrom(input):
    if input < 0: # all negative numbers are not palindromic
        return False
    elif input < 10: # all single digit numbers are palindromic
        return True
    else: # first is equal the last digit? then check for the inner core
        return None

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPalindrom(self):
        self.assertEqual(True, isPalindrom(1))
        self.assertEqual(True, isPalindrom(11))
        self.assertEqual(False, isPalindrom(12))
        self.assertEqual(True, isPalindrom(121))
        self.assertEqual(True, isPalindrom(1221))
        self.assertEqual(False, isPalindrom(123421))
        self.assertEqual(True, isPalindrom(123321))
        self.assertEqual(False, isPalindrom(-2))

# ------------------------------------------------------------------------------

# should return 91x99 --> 9009
findLargestPalindromicNumberFromTwoXDigitNumbers(2)
