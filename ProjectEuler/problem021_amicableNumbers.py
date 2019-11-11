# Amicable numbers
#
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

# idea:
# * do for all numbers in the range: find all divisors (list) and compute sum
# * then sort them into buckets where the sum is the key
# * if one bucket has more than one entry, then that
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
#import time
#import unitttest

def sumOfProperDivisors(number):
    return sum(computeProperDivisors(number))

def computeProperDivisors(number):
    if number <= 0:
        raise ValueError("Only positive integers bigger than zero are allowed.")

    properDivisors = set()
    for divisor in range(1, number):
        dividend, modulo = divmod(number, divisor)

        if modulo == 0:
            properDivisors.add(divisor)
            properDivisors.add(dividend) # save one call

    return properDivisors

# --- test call ---
def driver(number):
    print(number, "-->", computeProperDivisors(number), "-->", sumOfProperDivisors(number))

driver(220)
driver(1024)
