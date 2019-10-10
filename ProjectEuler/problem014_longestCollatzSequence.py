# Longest Collatz sequence
#
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

# for some approaches: also: https://euler.stephan-brumme.com/612/
# for the Collatz conjecture and the generalized form (circles in the graph): https://en.wikipedia.org/wiki/Collatz_conjecture

# ------------------------------------------------------------------------------

# idea:
# first naively implement the conjecture, then support it with a dictionary
# process all start-values from 1..10^6; then find the biggest one

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def collatzStepsUntil1(input):
    # todo: write unit-test against the first 30 entries of https://oeis.org/A006577

    # check input for proper range
    if input <= 0:
        raise Exception("Values below 1 not supported. Just positive integers (in this case).")

    # no more steps needed
    if input == 1:
        return 0

    # check and apply the Collatz-rule
    if input % 2 == 0:
        return 1 + collatzStepsUntil1(input // 2)
    else:
        return 1 + collatzStepsUntil1(3 * input + 1)

# --- test run ---
for i in range(1, 28):
    print(i, " -> ", collatzStepsUntil1(i))
