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

cache = {}

def collatz(n):
    #print(n)

    if n < 1:
        return  -1 # should be an error!

    # check if in cache
    if n in cache:
        #print("cache hit! :)")
        return cache[n]

    # looks like we have to compute ourselves
    steps = 1 # because it was called once
    if n == 1:
        pass # do nothing, because we found the end result
    elif n % 2 == 0: # even
        steps += collatz(n // 2)
    else: #odd
        steps += collatz(3 * n + 1)

    # put into the cache
    cache[n] = steps

    return steps

# ------------------------------------------------------------------------------

def driver(n):
    print("collatz sequence of n =", n)
    steps = collatz(n)
    print("--> finished after", steps, "steps")
    print("-------------------------------------------")

# ------------------------------------------------------------------------------

def findlongestSequenceForNumbersBelow(n):
    mostSteps = -1
    bestCandidate = -1

    for elem in range(1, n): # because last should not be included
        steps = collatz(elem)
        #print(elem, "->", steps)
        if steps > mostSteps:
            bestCandidate = elem
            mostSteps = steps

    return (bestCandidate, mostSteps)

# ------------------------------------------------------------------------------

driver(0)
driver(1)
driver(2)
driver(3)
driver(33)

#print(findlongestSequenceForNumbersBelow(100)) # result is (97, 119)
#print(findlongestSequenceForNumbersBelow(10000000)) # result is: (837799, 525)

for digits in range(0,10):
    #print("digits:",digits)
    number = 10 ** digits
    #print("number:", number)

    print("for range up to ", number, "the result is", findlongestSequenceForNumbersBelow(number))

# for range up to  1 the result is (-1, -1)
# for range up to  10 the result is (9, 20)
# for range up to  100 the result is (97, 119)
# for range up to  1000 the result is (871, 179)
# for range up to  10000 the result is (6171, 262)
# for range up to  100000 the result is (77031, 351)
# for range up to  1000000 the result is (837799, 525)
# for range up to  10000000 the result is (8400511, 686)


