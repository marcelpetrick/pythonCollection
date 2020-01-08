# Pandigital prime
#
# Problem 41
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# ------------------------------------------------------------------------------
# idea:
# * it is clear that a number with 9 digits is the biggest pandigital number,
# * searching from 10**9 -1 downwards inside all primes, check if it is n-pandigital
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
