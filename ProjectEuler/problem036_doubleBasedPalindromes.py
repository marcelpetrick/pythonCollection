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

# hints:
# * to do th palindrome check, just revert the stringified version and check against the original
# * just odd numbers (dec) can be fitting, because even numbers converted to binary would have a 0 as last digit. and
# for the first digit no numbers with 0 are allowed in the task (same applies for numbers divisible by ten in decimal, but
# mod 10 == 0 is already included in mod 2 == 0)

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def palindromeCheck(number):

    return false


# todo add unittest
