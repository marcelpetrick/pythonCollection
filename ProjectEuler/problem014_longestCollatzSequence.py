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
# implementation
# ------------------------------------------------------------------------------
import time

collatzDic = dict()
def collatzStepsUntil1(input):
    # todo: write unit-test against the first 30 entries of https://oeis.org/A006577

    # check input for proper range
    if input <= 0:
        raise Exception("Values below 1 not supported. Just positive integers (in this case).")

    # no more steps needed
    if input == 1:
        return 0

    # check the dictionary for previous results (for 1 mio items: with memo: 1.2s; without 27s!)
    if input in collatzDic:
        return collatzDic[input]

    # check and apply the Collatz-rule
    result = -1
    if input % 2 == 0:
        result = 1 + collatzStepsUntil1(input // 2)
    else:
        result = 1 + collatzStepsUntil1(3 * input + 1)

    collatzDic[input] = result

    return result

# --- test run ---
startTime = time.time()
number, steps = -1, -1
maxLimit = 1000000
for i in range(1, maxLimit):
    result = collatzStepsUntil1(i)
    # print(i, " -> ", result)

    if result > steps:
        steps = result
        number = i

print("took", time.time() - startTime, "s")
print("number %d has %d steps, which is the biggest amount of steps for numbers below %d" % (number, steps, maxLimit))

# took 1.3609158992767334 s
# number 837799 has 524 steps, which is the biggest amount of steps for numbers below 1000000

# ---- euler page ---
# Congratulations, the answer you gave to problem 14 is correct.
#
# You are the 209206th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%.
