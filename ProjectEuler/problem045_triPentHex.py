# Triangular, pentagonal, and hexagonal
#
# Problem 45
#
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...
#
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

# ------------------------------------------------------------------------------
# idea:
# * just borrow from the dove-tailing approach from problem044:
# ** compute first the next hexagonal number, then compute triangle and pentagonal numbers up to this point and
#   put them into respective dicts; then check the given hexagonal number if it is inside the dicts
# * if two hits are found, abort mission .. should be easy as pie; maybe computationally intensive,
#   but should be doable until midnight

# ------------------------------------------------------------------------------

def makeTriangleNumber(n):
    return n * (n + 1) // 2

def makePentagonalNumber(n):
    return n*(3 * n - 1) // 2

def makeHexagonalNumber(n):
    return n*(2 * n - 1)

# ------------------------------------------------------------------------------

triNums = dict()
pentNums = dict()
hexNums = dict()

# init
triNums[1] = 1 # needed for the way how for the maximum key in the dict is searched
pentNums[1] = 1

def findHits(maxAmount):

    n = 1
    while True:
        # compute the current hexagonal number
        if n in hexNums:
            nH = makeHexagonalNumber[n]
        else:
            nH = makeHexagonalNumber(n)
            hexNums[n] = nH

        #print("hex: handle now", n, "-->", nH) # todom remove

        # fill the dicts of the tria and pent numbers
        while True:
            currentMax = max(triNums, key=lambda x: triNums[x])
            if triNums[currentMax] < nH:
                nextKey = currentMax+ + 1
                triNums[nextKey] = makeTriangleNumber(nextKey)
                #print("    tri:", nextKey, triNums[nextKey]) # todom remove
            else:
                break

        # do the same for pentagonal number dict
        while True:
            currentMax = max(pentNums, key=lambda x: pentNums[x])
            if pentNums[currentMax] < nH:
                nextKey = currentMax+ + 1
                pentNums[nextKey] = makePentagonalNumber(nextKey)
                #print("    pent:", nextKey, pentNums[nextKey]) # todom remove
            else:
                break

        # check now if the current hex number is also tri and pent
        if nH in pentNums.values():
            print("-----------------------------------------------------------------")
            if nH in triNums.values():
                print("found a good hit! nH:", nH, "for n=", n)
                print("tri:", triNums)
                print("pen:", pentNums)
                print("hex:", hexNums)


                if nH > 40755:
                    print("this shall be the wanted result:", nH, "for n=", n)
                    break

        n += 1

# ------------------------------------------------------------------------------

findHits(10)

# ------------------------------------------------------------------------------

# output:

# ------------------------------------------------------------------------------
