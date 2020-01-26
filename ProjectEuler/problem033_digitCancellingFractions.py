# Digit cancelling fractions
#
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# ------------------------------------------------------------------------------

def isFakeRoundable(numA, numB):
    strA = str(numA)
    strB = str(numB)

# still wrong, I guess the key is that the result after the "naive" cancelling would be equal to the real result
    if strA[1] == strB[0] or strA[0] == strB[1]:
        return True
    #
    # for digit in strA:
    #     if digit in strB and digit != "0":
    #         #print("found cancellable digit:", digit)
    #         return True

    return False

# ------------------------------------------------------------------------------
print(isFakeRoundable(21, 13))
# ------------------------------------------------------------------------------

results = []
for denominator in range(10, 100): # since the resulting number shall be below 1
    for numerator in range(10, denominator+1):
        print("check now:", denominator, numerator)
        if isFakeRoundable(numerator, denominator):
            results.append([numerator, denominator])

print("results:", results)
