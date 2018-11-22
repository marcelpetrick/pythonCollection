# This problem was asked by Microsoft.
#
# A number is considered perfect if its digits sum up to exactly 10.
#
# Given a positive integer n, return the n-th perfect number.
#
# For example, given 1, you should return 19. Given 2, you should return 28.

# question: does it mean just once sum of the digits or repeatedly? (like for 991 -> 19 -> 10?)

import unittest
# import this

# ------------------------------------------------------------------------------

def nthPerfectNumber(input):
    # todo idea: make a generator? have to inform myself how this was done via python

    currentOne = 0
    number = -1
    while currentOne != input:
        number += 1
        if calculateCrossfoot(number) == 10:
            currentOne += 1 # todo howto ++ in  python?!?
            print("perfect number", currentOne, "is", number)
        #else:
            #print(number, "not perfect")

    #print("will return:", number)
    return number

# ------------------------------------------------------------------------------

def calculateCrossfoot(input):
    digitSum = 0
    while input > 0:
        #print("input:", input, "digitSum:", digitSum)
        digit = input % 10 # could be as well immediately summed up, but for the sake of readability
        input = input // 10
        digitSum += digit

    return digitSum

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test0(self):
        input = 1
        expectedResult = 19
        output = nthPerfectNumber(input)
        self.assertEqual(output, expectedResult)
        print(" --> input", input, "yielded result:", output)

    def test1(self):
        input = 2
        expectedResult = 28
        output = nthPerfectNumber(input)
        self.assertEqual(output, expectedResult)
        print(" --> input", input, "yielded result:", output)

# # ------------------------------------------------------------------------------
#
# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# todo make this unit-tests
print(calculateCrossfoot(1)) # 1
print(calculateCrossfoot(12)) # 3
print(calculateCrossfoot(123)) # 6

nthPerfectNumber(20)
