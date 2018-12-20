# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome,
# as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
# ------------------------------------------------------------------------------

import unittest
import math

# ------------------------------------------------------------------------------

def isPalindrome(input, shouldPrint=False):
    # if the number is negative, then never a palindrome
    if input < 0:
        return False

    # prevent that log(0, 10) results in an error
    if input == 0:
        return True

    # find first the power of 10
    power = math.log(input, 10)
    # if the number has just one digit, it is palindrome
    if power < 1:
        return True

    # means: now we got a call with at least two digits!
    if shouldPrint:
        print("at least two digits?", input, "has log", power)

    # now check for those bigger (10 and upwards)
    # if the first digit has the same value like the last one
    # - then check the inner part (in case it exists!) and return that result-value
    # - else: return false

    # get last digit: modulo by 10
    # get first digit: div
    #256 -> should give 2
    #log=2 --> 10^floor(power) -> 100
    #256 div 100 -> 2

    lastDigit = input % 10
    highestPowerOfTen = 10**int(power)
    firstDigit = input // highestPowerOfTen # attention: use integer division with //
    if shouldPrint:
        print("firstDigit:", firstDigit)
        print("lastDigit:", lastDigit)

    if firstDigit == lastDigit:
        middlePartOfNumber = (input % highestPowerOfTen) // 10

        # attention: doing this for 10201 results in: 20 and not 020. 20 is not palindrome, therefore follow-up error
        # workaround: separate into chunks of one digit and then check the array from each side ..

        if shouldPrint:
            print("middlePartOfNumber:", middlePartOfNumber)
        return isPalindrome(middlePartOfNumber)
    else:
        return False

    # we should never reach here ...
    return False

# ------------------------------------------------------------------------------

def driver(input):
    print("input", input, ("is a palindrome" if isPalindrome(input) else "is not a palindrome"))

# ------------------------------------------------------------------------------

# driver(-1)
# driver(0)
# driver(2)
# driver(9)
# driver(10) # wrong, of course
# driver(11)
# driver(100)
# driver(101)

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(False, isPalindrome(-10))
        self.assertEqual(False, isPalindrome(-1))

        # special case because of log-definition
        self.assertEqual(True, isPalindrome(0))
        # all single digit values are palindromes
        self.assertEqual(True, isPalindrome(1))
        self.assertEqual(True, isPalindrome(2))
        self.assertEqual(True, isPalindrome(3))
        self.assertEqual(True, isPalindrome(9))

        # dual digits
        self.assertEqual(False, isPalindrome(10))
        self.assertEqual(True, isPalindrome(11))
        self.assertEqual(False, isPalindrome(42))
        self.assertEqual(True, isPalindrome(99))

        # # three or more
        self.assertEqual(True, isPalindrome(101))
        self.assertEqual(True, isPalindrome(232))
        self.assertEqual(True, isPalindrome(41514))
        self.assertEqual(True, isPalindrome(40504, True)) # problematic because of the zeroes

        self.assertEqual(False, isPalindrome(102))
        self.assertEqual(False, isPalindrome(543))
        self.assertEqual(False, isPalindrome(12345))
        #self.assertEqual(False, isPalindrome(12345678900987654321)) # problematic because of the zeroes

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
