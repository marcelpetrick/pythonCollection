# Prime permutations
#
# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers
# are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

# ------------------------------------------------------------------------------
# idea:
# * hint: "An arithmetic sequence is a sequence of numbers such that the difference of any two successive members
# of the sequence is a constant. Example. 2,4,6,8,10….is an arithmetic sequence with the common difference 2." (google)
# * create all permutations of 4 (digits) (or just 4-tuple?) out of digits from 1..9 (by a generator, not in memory)
# * compute all permuts of this 4-tuple, then check if prime, then store all primes for that: and determine of any
# 3-set the arithm. difference (also called: offset)?

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

#import time

# ------------------------------------------------------------------------------

def createListOfPrimePermutationsOfInputNumber(number):
    # todo maybe make the input a string

    # todo maybe create some dictionary as backup: key will be the sorted digits of the number (normalization)

    pass

# ------------------------------------------------------------------------------

