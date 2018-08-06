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


# test-programm: probability should be around 0.4
cointhrows = 1000000

probability = 0
for x in range(cointhrows):
    if biasedCoin():
        probability += 1

print("biased coin after", cointhrows ,"throws -->", probability / cointhrows)

# ------------------------------------------------------------------------------

def unbiasedCoin():
    coin0, coin1 = biasedCoin(), biasedCoin()
    while coin0 == coin1:
        #print("throw")
        coin0, coin1 = biasedCoin(), biasedCoin()
    return coin0 # just pick one; could be as well the second one

probability = 0
for x in range(cointhrows):
    if unbiasedCoin():
        probability += 1

print("unbiased coin after", cointhrows ,"throws -->", probability / cointhrows)

# a very good explanation why this works can be found at https://jeremykun.com/2014/02/08/simulating-a-fair-coin-with-a-biased-coin/
# (similar: http://yilinmo.github.io/fair-results-from-a-biased-coin)
