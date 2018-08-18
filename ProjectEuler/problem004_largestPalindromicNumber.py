# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# ------------------------------------------------------------------------------
import unittest
import time
# ------------------------------------------------------------------------------

# idea: try to check downwards: use two loops over the input; starting with the biggest possible number from the amount of digits
def findLargestPalindromicNumberFromTwoXDigitNumbers(digits):
    biggestNumber = 10 ** digits - 1
    #print(biggestNumber)
    foundBiggestNumber = -1

    for a in range(biggestNumber, 1, -1):
        #print(a)
        for b in range(biggestNumber, 1, -1):
            product = a*b
            #print("do:", a, "*", b, "=", product)
            # stop this path in case we have already something bigger here
            if product < foundBiggestNumber:
                #print("break because: if product < foundBiggestNumber:")
                break
            # check for the required attribute
            if isPalindrome(product):
                #print("palindrom:", a, "*", b, "=", product)
                if product > foundBiggestNumber:
                    foundBiggestNumber = product
                    # print(foundBiggestNumber) # un-comment this line to see some "progress"
                break # because all following computations can just yield a smaller product

    return foundBiggestNumber #error!

# ------------------------------------------------------------------------------

# todo rename the function name: e at suffix missing
def isPalindrome(input):
    return isPalindrome2(str(input))

    # #print("-----------------------")
    # #print("isPalindrome called with", input)
    # if input < 0: # all negative numbers are not palindromic
    #     return False
    # elif input < 10: # all single digit numbers are palindromic
    #     return True
    # else: # first is equal the last digit? then check for the inner core
    #     stringifiedNumber = str(input)
    #     #print(stringifiedNumber[0], stringifiedNumber[-1]) # -1 is last elem
    #     if stringifiedNumber[0] == stringifiedNumber[-1]:
    #         #print("same!")
    #         substring = stringifiedNumber[1:-1]
    #         if substring.__len__() > 0:
    #             #print("call with substring", substring, "the function")
    #             if str(int(substring)) != substring: # ATTENTION this check is needed, else 009 is converted to 9, which is palindromic!
    #                 #print("big fuckup!:", substring)
    #                 # in case of 0 or 0000
    #                 if int(substring) == 0:
    #                     return True
    #                 # else
    #                 return False
    #             return isPalindrome(int(substring))
    #         else:
    #             #print("no more stuff left - return True")
    #             return True
    #     else:
    #         #print("begin and end not equal :'(")
    #         return False

# ------------------------------------------------------------------------------

def isPalindrome2(input):
    if input[0] != input[-1]:
        return False

    return input == input[::-1]

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(True, isPalindrome(1))
        self.assertEqual(True, isPalindrome(11))
        self.assertEqual(False, isPalindrome(12))
        self.assertEqual(True, isPalindrome(121))
        self.assertEqual(True, isPalindrome(1221))
        self.assertEqual(False, isPalindrome(123421))
        self.assertEqual(True, isPalindrome(123321))
        self.assertEqual(False, isPalindrome(-2))
        self.assertEqual(False, isPalindrome(900099))
        self.assertEqual(True, isPalindrome(9009)) # has to work
        self.assertEqual(True, isPalindrome(906609))  # has to work

    def test_largestPalindromic(self):
        self.assertEqual(9009, findLargestPalindromicNumberFromTwoXDigitNumbers(2))
        #self.assertEqual(906609, findLargestPalindromicNumberFromTwoXDigitNumbers(3)) # googled ... but why is mine wrong?

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# should return 91x99 --> 9009
#findLargestPalindromicNumberFromTwoXDigitNumbers(2)

print("#############################################")
for x in range(0, 10):
    start = time.time()
    print(x, "digits:", findLargestPalindromicNumberFromTwoXDigitNumbers(x), "in", time.time() - start, "seconds")

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 4 is correct.
#
# You are the 395508th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.

# ------------------------------------------------------------------------------

# 0 digits: -1 in 2.1457672119140625e-06 seconds
# 1 digits: 9 in 3.075599670410156e-05 seconds
# 2 digits: 9009 in 5.316734313964844e-05 seconds
# 3 digits: 906609 in 0.004776716232299805 seconds
# 4 digits: 99000099 in 0.009120464324951172 seconds
# 5 digits: 9966006699 in 0.46706056594848633 seconds
# 6 digits: 999000000999 in 0.5814318656921387 seconds
# 7 digits: 99956644665999 in 93.65605902671814 seconds
# 8 digits: 9999000000009999 in 59.7429838180542 seconds
