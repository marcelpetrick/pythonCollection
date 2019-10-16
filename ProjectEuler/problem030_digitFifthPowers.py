# Digit fifth powers
#
# Problem 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# ------------------------------------------------------------------------------

# idea:
# * implement a generalized function
# * is it a lucky hit that all aforementioned numbers are four-digit numbers? what about bigger numbers?
#       else generating and checking just the range of 10**n to 10**(n+1) woulds be enough
# * for digit in digits: compute the n-th power; add and check if the sum is the digit
# * maybe pre-calc a rainbow-table of all digit-powers and just make a look up
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
import time

# --- first the naive implementation ---
def numberIsDigitFourthPower(number, power):
    if power <= 1:
        raise ValueError("power too small, at least 1 expected!")

    # split into digits
    digits = [int(d) for d in str(number)]

    # power them up
    poweredDigits = [x ** power for x in digits]

    return sum(poweredDigits) == number

def generateDigitFourthPowers(power, rangeExponent):
    if rangeExponent < 1:
        raise ValueError("exponent too small, at least 2 expected!")

    resultList = []
    for number in range(10, 10 ** rangeExponent):
        if(numberIsDigitFourthPower(number, power)):
            print("is digit", power, "th power:", number)
            resultList.append(number)

    return sum(resultList)

# --- test call ---
startTime = time.time()
powerSum = generateDigitFourthPowers(5, 6)
print("computation took", time.time() - startTime, "s: powerSum = ", powerSum)

# is digit fourth power 1634
# is digit fourth power 8208
# is digit fourth power 9474
# computation took 5.894561290740967 s: powerSum =  19316

# ---------------------
# is digit 5 th power: 4150
# is digit 5 th power: 4151
# is digit 5 th power: 54748
# is digit 5 th power: 92727
# is digit 5 th power: 93084
# is digit 5 th power: 194979
# computation took 5.940189361572266 s: powerSum =  443839
# ---------------------
# Congratulations, the answer you gave to problem 30 is correct.
#
# You are the 101338th person to have solved this problem.
