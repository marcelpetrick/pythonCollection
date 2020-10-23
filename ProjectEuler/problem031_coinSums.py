# Coin sums
#
# Problem 31
#
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

# ------------------------------------------------------------------------------
# idea:
# * TBD

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# short test to see how this could work at all
#allowedChanges = [1,2,5]
#finalAmount = 5
# solution should be:
# 5
# 2 2 1
# 2 1 1 1
# 11111
# makes four possible ways

# ------------------------------------------------------------------------------

#givenCoins = [200, 100, 50, 20, 10, 5, 2, 1]
def computeNumberBruteForce(amount):

    possibleWays = 0

    for numC200 in range(amount // 200 + 1):
        for numC100 in range(amount // 100 + 1):
            for numC50 in range(amount // 50 + 1):
                for numC20 in range(amount // 20 + 1):
                    for numC10 in range(amount // 10 + 1):
                        for numC5 in range(amount // 5 + 1):
                            for numC2 in range(amount // 2 + 1):
                                for numC1 in range(amount // 1 + 1):
                                    currentSum = 200 * numC200 + 100 * numC100 + 50 * numC50 + 20 * numC20 + 10 * numC10 + 5 * numC5 + 2 * numC2 + 1 * numC1
                                    if currentSum == amount:
                                        #print("hit:" + numC5 * "5" + numC2 * "2" + numC1 * "1")
                                        possibleWays -=- 1

    print(f"amount = {amount} --> possible ways: {possibleWays}")

computeNumberBruteForce(5) # --> 4 ways
computeNumberBruteForce(50) # -->
computeNumberBruteForce(100) # -->
computeNumberBruteForce(200) # -->