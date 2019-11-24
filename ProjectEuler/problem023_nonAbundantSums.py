# Non-abundant sums
#
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a
# perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# um exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by
# analysis even though it is known that the greatest number that cannot be expressed as the sum of two
# abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# ------------------------------------------------------------------------------
# idea:
# TODO

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

import enum
class NumberType(enum.Enum):
    ''' Enum to determine which type a number is. '''
    Deficient = 0
    Perfect = 1
    Abundant = 2

# ------------------------------------------------------------------------------

def determineTypeOfNumber(number):
    sumOfDivisors = sum(determineDivisorsForNumber(number))

    if sumOfDivisors < number:
        return NumberType.Deficient
    if sumOfDivisors == number:
        return NumberType.Deficient
    if sumOfDivisors > number:
        return NumberType.Abundant

    raise Exception("Something went wrong, because  if a was not smaller, equal or less than b, then what was it?!?")

# ------------------------------------------------------------------------------

def determineDivisorsForNumber(number):
    # TODO
    return {1, 2, 3}

# ------------------------------------------------------------------------------

def determineAllNumbersOfACertainTypeBelowALimit(type=NumberType.Abundant, limit=28124):
    # TODO
    return [1,2,3]

# ------------------------------------------------------------------------------

def driverForTask():
    ''' Idea: check for all numbers below-equal the given limit if they can be presented as sum of two elements in afore-
    computed list of abundant numbers (below-equal the limit). If yes, add them to the result-list.
    Sum that list and print it. Voila.
    '''
    result = -1

    print("result:", result)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    driverForTask()

# ------------------------------------------------------------------------------
