# This problem was asked by Square.
#
# Assume you have access to a function toss_biased() which returns0 or 1 with a probability that's not
# 50-50 (but also not 0-100 or 100-0).You do not know the bias of the coin.
#
# Write a function to simulate an unbiased coin toss.

# ------------------------------------------------------------------------------

# Idea is to throw to coins until they show different results and then pick one as result.

# ------------------------------------------------------------------------------

import random

def biasedCoin():
    ''' Return in 60% of the cases TRUE else FALSE. Not 50/50! '''
    value = random.randint(1, 101)
    return (value >= 60)


cointhrows = 1000000

probability = 0
for x in range(cointhrows):
    if biasedCoin():
        probability += 1

print(probability / cointhrows)

