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
    # no checks for odd-ness included, because the inputs are already filtered
    # saves a check here, saves time for one function-call, or?

    # reverting a string in python: ten thousands of ways
    # https://www.journaldev.com/23647/python-reverse-string#python-reverse-string-using-slicing

    # check first if number itself is palindrome
    stringifiedDec = str(number)
    if stringifiedDec != stringifiedDec[::-1]:
        return False

    # do then the same check for the binary version
    stringifiedBin = str(bin(number))
    if stringifiedDec != stringifiedDec[::-1]:
        return False

    return True

# ------------------------------------------------------------------------------

# todo add unittest

# ------------------------------------------------------------------------------
# simple driver

print(5, palindromeCheck(5))
print(17, palindromeCheck(17))
print(585, palindromeCheck(585))

def driver(number):
    isPalindromic = palindromeCheck(number)
    if isPalindromic:
        print(number, "->", bin(number))

import time
startTime = time.time()

limit = 10 ** 6
for number in range(1, limit, 2): # step width 2 decresed runtime for 10 ** 6 (with output) from 0.44s to 0.22s
    driver(number)

print("computation took", time.time() - startTime, "s")