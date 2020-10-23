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
        print("numC200:" + str(numC200))
        s200 = numC200 * 200 # + 0
        for numC100 in range(amount // 100 + 1):
            print("numC100:" + str(numC100))
            s100 = numC100 * 100 + s200
            for numC50 in range(amount // 50 + 1):
                s50 = numC50 * 50 + s100
                for numC20 in range(amount // 20 + 1):
                    s20 = numC20 * 20 + s50
                    for numC10 in range(amount // 10 + 1):
                        s10 = numC10 * 10 + s20
                        for numC5 in range(amount // 5 + 1):
                            s5 = numC5 * 5 + s10
                            for numC2 in range(amount // 2 + 1):
                                s2 = numC2 * 2 + s5
                                for numC1 in range(amount // 1 + 1):
                                    s1 = numC1 + s2
                                    #currentSum = 200 * numC200 + 100 * numC100 + 50 * numC50 + 20 * numC20 + 10 * numC10 + 5 * numC5 + 2 * numC2 + 1 * numC1
                                    if s1 == amount:
                                        #print("hit:" + numC5 * "5" + numC2 * "2" + numC1 * "1")
                                        possibleWays -=- 1

    print(f"amount = {amount} --> possible ways: {possibleWays}")

# ------------------------------------------------------------------------------

def timedCall(amount):
    import time
    startTime = time.time()
    computeNumberBruteForce(amount)
    duration = time.time() - startTime
    print(f"    computation tooK {duration} s")

# ------------------------------------------------------------------------------

timedCall(5) # --> 4 ways
timedCall(50) # --> 451
timedCall(100) # --> 4563

# without temporary sums:
# amount = 100 --> possible ways: 4563
#     computation tooK 8.966492652893066 s

# with temp sums:
# amount = 100 --> possible ways: 4563
#     computation tooK 2.025925874710083 s

timedCall(200) # --> ... not computed yet

# ------------------------------------------------------------------------------
# see as well: https://en.wikipedia.org/wiki/Subset_sum_problem
# ------------------------------------------------------------------------------

# amount = 5 --> possible ways: 4
#     computation tooK 0.0 s
# amount = 50 --> possible ways: 451
#     computation tooK 0.02383899688720703 s
# amount = 100 --> possible ways: 4563
#     computation tooK 2.025925874710083 s
# amount = 200 --> possible ways: 73682
#     computation tooK 310.35107588768005 s
# ------------------------------------------------------------------------------

# Answer was correct!
# Completed on Fri, 23 Oct 2020, 13:55
#
# marcelpetrick
# Level 2
# Solved 50 out of 730 problems