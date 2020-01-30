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

def isFakeCancellable(numA, numB):
    strA = str(numA)
    strB = str(numB)

    realResult = numA / numB

    if strA[1] == strB[0]:
        print("one cancellable: a")
        if int(strB[1]) == 0:
            print("would be DIV 0!")
            return False
        failCancel = int(strA[0]) / int(strB[1])
        if failCancel == realResult:
            print("fake cancel is equal to real result!", failCancel, "==", realResult)
            return True

    if strA[0] == strB[1]:
        print("one cancellable: b")
        failCancel = int(strA[1]) / int(strB[0])
        if failCancel == realResult:
            print("fake cancel is equal to real result!", failCancel, "==", realResult)
            return True

    return False

# ------------------------------------------------------------------------------
print("21/13:", isFakeCancellable(21, 13))
print("49/98:", isFakeCancellable(49, 98))
# ------------------------------------------------------------------------------

results = []
for denominator in range(10, 100): # since the resulting number shall be below 1
    for numerator in range(10, denominator+1):
        print("check now:", denominator, numerator)
        if isFakeCancellable(numerator, denominator):
            if numerator != denominator:
                results.append([numerator, denominator])

print("results:", results)
# ------------------------------------------------------------------------------

# ..
# one cancellable: b
# check now: 99 99
# one cancellable: a
# fake cancel is equal to real result! 1.0 == 1.0
# results: [[16, 64], [26, 65], [19, 95], [49, 98]]
# ------------------------------------------------------------------------------

# See: "If the product of these four fractions is given in its lowest common terms, find the value of the denominator."
from fractions import Fraction
fractionProduc = Fraction(1,1) # identity
for elem in results:
    fractionProduc *= Fraction(elem[0], elem[1])
print("final product:", fractionProduc, "==>", fractionProduc.denominator)
# ------------------------------------------------------------------------------
# ..
# results: [[16, 64], [26, 65], [19, 95], [49, 98]]
# final product: 1/100 ==> 100
# ------------------------------------------------------------------------------
# Congratulations, the answer you gave to problem 33 is correct.
#
# You are the 67196th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 25%.
# ------------------------------------------------------------------------------
