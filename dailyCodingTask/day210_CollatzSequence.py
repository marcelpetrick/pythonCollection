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
    pass

# ------------------------------------------------------------------------------

collatz(1)
collatz(2)
collatz(3)