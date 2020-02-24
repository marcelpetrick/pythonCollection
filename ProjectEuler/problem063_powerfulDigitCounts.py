# Powerful digit counts
#
# Problem 63
# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
# ------------------------------------------------------------------------------
# idea:
# * just compute straight-forward the n-th power of a digit and then check if the result has the length n
# * brute force could be enough
# * maybe some special cases are n+1 digit numbers as base which are then also n-th powers?
# ------------------------------------------------------------------------------

#import unittest

# # ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     unittest.main()

# ------------------------------------------------------------------------------

def getListOfNthPowers():

    returnValue = []

    for base in range(1, 10):
        for power in range(1, 10):
            result = base ** power

            if len(str(result)) == power:
                print("got one:", base, power, result)
                returnValue.append(result)

    return returnValue

# ------------------------------------------------------------------------------

print("------------------------------------------------------------------------------")
auto = getListOfNthPowers()
print("------------------------------------------------------------------------------")
print("all numbers which fit:", auto)
print("------------------------------------------------------------------------------")
print("how many are that?", len(auto))
