# Bouncy numbers
#
# Problem 112
#
# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
# for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below
# one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first
# reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy
# numbers is equal to 90%.
#
# Find the least number for which the proportion of bouncy numbers is exactly 99%.

# ------------------------------------------------------------------------------

# idea:
# TODO

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

import enum
class Type(enum.Enum):
    ''' Enum to determine which type a number is. '''
    Increasing = 0
    Decreasing = 1
    Bouncy = 2

# ------------------------------------------------------------------------------

# class Direction(enum.Enum):
#     ''' Enum to determine which type a number is. '''
#     Equal = 0
#     Up = 1
#     Down = 2
# ------------------------------------------------------------------------------

def determineType(number):
    ''' Returns Increasing, Decreasing or Bouncy :) '''

    # note: funny: single-digit-numbers can be Increasing and Decreasing at the same time ..

    # parsing direction is left-to-right

    # *** test: INCREASING ***
    rising = True
    numberStr = str(number)
    lastValue = int(numberStr[0]) # will have at least one digit
    for elem in numberStr[1:]:
        currentValue = int(elem)
        if currentValue < lastValue:
            rising = False
            break
        lastValue = currentValue

    if rising:
        return Type.Increasing

    # *** test: DECREASING ***
    rising = True
    numberStr = str(number)
    lastValue = int(numberStr[0]) # will have at least one digit
    for elem in numberStr[1:]:
        currentValue = int(elem)
        if currentValue > lastValue:
            rising = False
            break
        lastValue = currentValue

    if rising:
        return Type.Decreasing

    # *** else: DECREASING ***
    return Type.Bouncy

# ------------------------------------------------------------------------------

def determineAmountOfBouncyNumbersBelowLimit(limit):
    # do a raw loop over the range up to limit and check each for type
    # return the summed amount

    nrOfBouncyNumbers = 0
    for number in range(0, limit):
        if determineType(number) == Type.Bouncy:
            nrOfBouncyNumbers -=- 1

    return nrOfBouncyNumbers

# ------------------------------------------------------------------------------

def findNumberWhereBouncyNumbersReachGivenPercentageFirst(percentage):

    nrOfBouncyNumbers = 0
    totalAmount = 0
    number = 1
    while True:
        # +1 for the amount
        totalAmount += 1
        # check the current one
        if determineType(number) == Type.Bouncy:
            nrOfBouncyNumbers += 1
        # check if the target was reached
        currentPercentage = nrOfBouncyNumbers / totalAmount * 100
        #print(number, ":", currentPercentage)
        if currentPercentage >= percentage:
            #print("reached percentage")
            break

        # go to the next number
        number += 1

    return number

# ------------------------------------------------------------------------------
import unittest

class Testcase(unittest.TestCase):

    def test_determineType(self):
        # given input from Project Euler itself
        self.assertEqual(Type.Increasing, determineType(134468))
        self.assertEqual(Type.Decreasing, determineType(66420))
        self.assertEqual(Type.Bouncy, determineType(155349))

    def test_determineAmountOfBouncyNumbersBelowLimit(self):
        # given input from Project Euler itself
        self.assertEqual(525, determineAmountOfBouncyNumbersBelowLimit(1000))

    def test_percentage(self):
        self.assertEqual(538, findNumberWhereBouncyNumbersReachGivenPercentageFirst(50))
        self.assertEqual(21780, findNumberWhereBouncyNumbersReachGivenPercentageFirst(90))

    def test_createSolution(self):
        import time
        startTime = time.time()
        print("solution: 99 percent bouncyness is reached at number:", findNumberWhereBouncyNumbersReachGivenPercentageFirst(99))
        print("calculation took", time.time() - startTime, "s")

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# solution: 99 percent bouncyness is reached at number: 1587000
# calculation took 3.1421914100646973 s
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 3.182s
#
# OK

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 112 is correct.
#
# You are the 22801st person to have solved this problem.
#
# This problem had a difficulty rating of 15%. The highest difficulty rating you have solved so far is 25%.
