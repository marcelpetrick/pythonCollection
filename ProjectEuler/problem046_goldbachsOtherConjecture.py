# Goldbach's other conjecture
#
# Problem 46
#
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime
# and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# ------------------------------------------------------------------------------
# idea: (naive)
# * composite numbers are the "non-prime" numbers
# * in this case even just the odd ones ..
# * generate a list (or generator) of those by pre-computing the primes until a certain limit, then taking the
#   "inverse", then filtering by oddness?
#
# * goldbach-check: create the difference of "number to test" and "loop up to the prime below number to check":
# ** then divide the difference by two: and the resulting number shall be a square.
# ** at least once this shall be true then -> then the conjecture would be true
#
# * go upwards to find the first number, which does not fulfill it
# ------------------------------------------------------------------------------
