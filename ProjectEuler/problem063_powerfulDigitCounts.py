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
        for power in range(1, 100): # first idea limited this to the range of powers with 9 ... but 99 is more fitting
            # (even though 21 is the highest base on the seen result)
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

# ------------------------------------------------------------------------------

# ..
# got one: 9 18 150094635296999121
# got one: 9 19 1350851717672992089
# got one: 9 20 12157665459056928801
# got one: 9 21 109418989131512359209
# ------------------------------------------------------------------------------
# all numbers which fit: [1, 2, 3, 4, 16, 5, 25, 125, 6, 36, 216, 1296, 7, 49, 343, 2401, 16807, 117649, 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, 1073741824, 9, 81, 729, 6561, 59049, 531441, 4782969, 43046721, 387420489, 3486784401, 31381059609, 282429536481, 2541865828329, 22876792454961, 205891132094649, 1853020188851841, 16677181699666569, 150094635296999121, 1350851717672992089, 12157665459056928801, 109418989131512359209]
# ------------------------------------------------------------------------------
# how many are that? 49
#
# Process finished with exit code 0

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 63 is correct.
#
# You are the 40260th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 25%.
#
# Return to Problems page.