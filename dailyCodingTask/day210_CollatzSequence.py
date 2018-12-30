# This problem was asked by Apple.
#
# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
#
# if n is even, the next number in the sequence is n / 2
# if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
#
# Bonus: What input n <= 1000000 gives the longest sequence?

# ------------------------------------------------------------------------------

# idea:
# * implement the collatz-sequence
# + improvement: put the computed steps into a dictionary, to save the computation of the "rest" of the steps
# * do it for all values under the given n

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def collatz(n):
    print(n)

    if n < 1:
        return  -1 # should be an error!

    steps = 1 # because it was called once

    if n == 1:
        pass # do nothing, because we found the end result
    elif n % 2 == 0: # even
        steps += collatz(n // 2)
    else: #odd
        steps += collatz(3 * n + 1)

    return steps

# ------------------------------------------------------------------------------

def driver(n):
    print("collatz sequence of n =", n)
    steps = collatz(n)
    print("--> finished after", steps, "steps")
    print("-------------------------------------------")

# ------------------------------------------------------------------------------

driver(0)
driver(1)
driver(2)
driver(3)
driver(33)
