# Double-base palindromes
#
# Problem 36
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# ------------------------------------------------------------------------------

# idea:
# * loop over all numbers up to a certain limit (maybe parallelized - this would be actually the big bang for that task!)
# * create a function which tests a single number for palindromic (int and binary)
# * if true, then add to the result list
# * sum that result-list

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
