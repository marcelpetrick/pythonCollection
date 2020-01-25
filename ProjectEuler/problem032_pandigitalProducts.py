# Pandigital products
#
# Problem 32
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
# 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# ------------------------------------------------------------------------------
# idea:
# * brute force, naive: two stacked loops from 1 to 10 ** 9: abort inner loop if length of the result would be bigger
# than (9 - multiLength - multipliLength), which should be quite early
# * then compute the result and check if the whole stringified addition would be pandigital: maybe check even first if
# one of the digits in the second number ps art of the first (then abort)
#
# other way: draw digits from a sack: so if the first multiplicator takes those, then the second can just draw from the
# remaining: and then the result could just consist of the other ones ..

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
