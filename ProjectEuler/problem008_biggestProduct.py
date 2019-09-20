# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

# ------------------------------------------------------------------------------

# idea:
# * convert the input to a list with 1000 entries (simple) [done]
# either check for all 13-tuples the product, then print the final one [done]
# speed-up: shifting window: div by the front-number; multiply by the new follow-up-number [note done]
# another trick: if one of the factors is zero, then just "skip" [not done]

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def prepareInput():
    inputString = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )

    # convert all characters to integer-digits for the list
    listOfDigits = [int(character) for character in inputString]

    # print("elem in listOfDigits:", len(listOfDigits))

    return listOfDigits

#-------------------------------

def checkAllPossibleTupleProducts():
    ''' Simple and straightforward and with no padding of neutral elements of both ends of the list:
        create sliding window of 13 digits; compute the product; compare against the saved maximum
    '''

    # for the product of sub-lists
    from functools import reduce
    import operator

    # init the comparing values
    biggestTuple = []
    biggestTupleProduct = 0

    # get the list
    listOfDigits = prepareInput()

    # go over the whole list:
    tupleRange = 13
    for startIndex in range(0, 1000 -tupleRange):
        selectedTuple = listOfDigits[startIndex:(startIndex + tupleRange)]
        # print("selection:", selectedTuple)

        currentProduct = reduce(operator.mul, selectedTuple, 1)
        # print(currentProduct)

        if currentProduct > biggestTupleProduct:
            biggestTupleProduct = currentProduct
            biggestTuple = selectedTuple.copy()
            print("Bäm, update:", biggestTupleProduct)

    print("final state:", biggestTupleProduct,"with", biggestTuple)

#-------------------------------

# call the functionality
# print(prepareInput())
checkAllPossibleTupleProducts()

# result? needs to be checked against the euler-page
# final state: 23514624000 with [5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5]

# Result fom Euler-Homepage with 23514624000:
# Congratulations, the answer you gave to problem 8 is correct.
#
# You are the 323831st person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%.
