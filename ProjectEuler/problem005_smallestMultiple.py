# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible* by all of the numbers from 1 to 20?
# * means: remainder == 0

# ------------------------------------------------------------------------------
import unittest

# ------------------------------------------------------------------------------

def smallestMultiple(start, end):
    # todo first check if start <= end
    if start > end:
        return None

    # todo for each of the numbers in the range, do some prime-factorization
    # todo put them into some dictionary, where just the exponent of each prime-factor is saved: like for 8 == 2**3
    # mulitply all entries from the dictionary - the result is the wanted number

    return None

# ------------------------------------------------------------------------------

def smallestMultipleBruteForce(start, end):
    if start > end:
        return None

    listOfDividers = list(range(start, end+1))

    number = 0
    foundAResult = False
    while not foundAResult:
        number += 1
        if isDivideableBy(number, listOfDividers):
            return number # hard return - no boolean needed :D

    return None

# ------------------------------------------------------------------------------

def isDivideableBy(number, listOfDividers):
    for divider in listOfDividers:
        if number % divider != 0:
            return False

    return True

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test(self):
        self.assertIsNone(smallestMultiple(2,1)) # should return None, because not possible
        self.assertEqual(1, smallestMultiple(1,1))
        self.assertEqual(20, smallestMultiple(4, 5))
        self.assertEqual(2520, smallestMultiple(1, 10)) # from the task

# ------------------------------------------------------------------------------

# # ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     unittest.main()
# 
# # ------------------------------------------------------------------------------
# 
# # todo add here code for
# print("smallestMultiple(1, 20):", smallestMultiple(1, 20))

# ------------------------------------------------------------------------------

print("smallestMultipleBruteForce(1, 4):", smallestMultipleBruteForce(1, 4))
print("smallestMultipleBruteForce(1, 10):", smallestMultipleBruteForce(1, 10))
print("smallestMultipleBruteForce(1, 20):", smallestMultipleBruteForce(1, 20))

# smallestMultipleBruteForce(1, 4): 12
# smallestMultipleBruteForce(1, 10): 2520
# smallestMultipleBruteForce(1, 20): 232792560

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 5 is correct.

# You are the 403707th person to have solved this problem.

# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.