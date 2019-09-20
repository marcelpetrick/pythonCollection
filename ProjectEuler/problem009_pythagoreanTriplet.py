# Special Pythagorean triplet
#
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# ------------------------------------------------------------------------------

# idea:
# how to generate them efficiently?
#
# from en.wikipedia.org: "Euclid's formula[3] is a fundamental formula for generating Pythagorean triples given an
# arbitrary pair of integers m and n with m > n > 0. The formula states that the integers#
#     a = m 2 − n 2 ,   b = 2 m n ,   c = m 2 + n 2
#     {\displaystyle a=m^{2}-n^{2},\ \,b=2mn,\ \,c=m^{2}+n^{2}} a=m^{2}-n^{2},\ \,b=2mn,\ \,c=m^{2}+n^{2}
# form a Pythagorean triple."
#
# assumption: since c with highest value of 1000 (itself) is the upper limit, just search for values up to 1k.
# c is the sum of m^2 and n^2, where m is bigger n. So it could be topped by m <= 1000 too.
#
# plan: generate two loops: m from 1000 to 0; n from m-1 to 0: then generate a, b and c. check if pyth; if yes, then check if sum is 1k.
# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# def isPythagoreanTriplet(a, b, c):
#     leftSide = a * a + b * b
#     rightSide = c * c
#     isPythagoreanTriplet = (leftSide == rightSide)
#     return isPythagoreanTriplet

# --------------------

def generateABC(m, n):
    mSquare = m * m
    nSquare = n * n

    a = mSquare - nSquare
    b = 2 * m * n
    c = mSquare + nSquare

    return a,b,c

# --------------------

def isSum1000(a,b,c):
    return (a + b + c == 1000)

# --------------------

def __main__():
    upperLimit = 100

    for m in range(upperLimit, -1, -1):
        for n in range(m, -1, -1):
            a,b,c = generateABC(m, n)

            foundProperTriplet = isSum1000(a,b,c)

            print("m, n:", m, n, "a,b,c:", a,b,c, "is Hit:", foundProperTriplet, a+b+c)

            # hard exit, IDC
            if foundProperTriplet:
                print("product for the solution is:", a*b*c)
                exit(0)

# --------------------

# run it
__main__()

# gives:
# m, n: 20 12 a,b,c: 256 480 544 is Hit: False 1280
# m, n: 20 11 a,b,c: 279 440 521 is Hit: False 1240
# m, n: 20 10 a,b,c: 300 400 500 is Hit: False 1200
# m, n: 20 9 a,b,c: 319 360 481 is Hit: False 1160
# m, n: 20 8 a,b,c: 336 320 464 is Hit: False 1120
# m, n: 20 7 a,b,c: 351 280 449 is Hit: False 1080
# m, n: 20 6 a,b,c: 364 240 436 is Hit: False 1040
# m, n: 20 5 a,b,c: 375 200 425 is Hit: True 1000
# product for the solution is: 31875000

# Congratulations, the answer you gave to problem 9 is correct.
#
# You are the 329039th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%.