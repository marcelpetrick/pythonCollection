# Pentagon numbers
#
# Problem 44
#
# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj|
# is minimised; what is the value of D?
# ------------------------------------------------------------------------------
# idea:
# * let's simplify the needed equation: n(3n-1)/2 - m(3m-1)/2 = d(3d-1)/2 .. so save the division for all of them
# * put the intermediate results into a map, so that they can be reused (or better a dict?)
# * one loop which computes the next pentagonal number, then checks if this number minus one of the previous
# ones is contained in the container as value?

# ------------------------------------------------------------------------------

def makeDoublePentagonalNumber(n):
    return n*(3*n-1)//2


penNums = dict()

def findPenPairs(limit):
    minimalDiffSoFar = 666

    n = 1
    while True:
        # look it up, if possible, else compute. See the sum-check below for the reason why n/nP can already exist in the dictionary
        if n in penNums:
            nP = penNums[n]
        else:
            nP = makeDoublePentagonalNumber(n)
            penNums[n] = nP

        for m in range(n-1, 0, -1): # one less than the start, then down to 1
            #print("n, m", n, m) # todom remove
            mP = penNums[m]

            diff = nP - mP
            if diff in penNums.values():
                #print("diff hit:", n, nP, m, mP, "-->", diff)

                sum = nP + mP

                # prepare the dict while counting up
                fakeN = n
                while True:
                    fakeNP = makeDoublePentagonalNumber(fakeN)
                    penNums[fakeN] = fakeNP
                    if fakeNP >= sum:
                        #print("  sum not pentagonal")
                        break
                    fakeN += 1

                # check now if the sum was also pentagonal
                if sum in penNums.values():
                    print("diff hit:", n, nP, m, mP, "-->", diff)
                    print("  sum is also pentagonal!", fakeN, fakeNP)
                    if diff < minimalDiffSoFar:
                        print("-------------------------------> D:", diff)
                        minimalDiffSoFar = diff

        n += 1
        if n == limit:
            break

# ------------------------------------------------------------------------------

findPenPairs(100**10)

# ------------------------------------------------------------------------------
# C:\Users\MarcelP\Desktop\MarcelsFolder\coding\pythonCollection\venv\Scripts\python.exe C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/ProjectEuler/problem044_pentagonNumbers.py
# diff hit: 2167 7042750 1020 1560090 --> 5482660 (last number is answer; just quit the computation, since there can't be smaller solutions for the difference
#   sum is also pentagonal! 2395 8602840
# ------------------------------------------------------------------------------
# Congratulations, the answer you gave to problem 44 is correct.
#
# You are the 57500th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 25%. #
# ------------------------------------------------------------------------------
