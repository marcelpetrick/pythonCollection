# Digit factorials
#
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# ------------------------------------------------------------------------------
# idea:
# * a function to compute the factorial (maybe with dictionary for caching) - not really needed, because just 0 to 9
# * if one of the factorials is bigger than the wanted sum, then it can be skipped immediately, or?
# * what is the boundary? how to know to stop?
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

class FactorialChecker:

    # class attribute
    factDict = {}

    def __init__(self):

        # prepare the factorial dictionary
        currentFact = 1
        for elem in range(1, 10):
            # compute the next fact
            currentFact *= elem
            # insert into dict
            self.factDict[elem] = currentFact

        print("current dictionary:", self.factDict) # todom remove

    # ----------------------------

    def computeResultsForRange(self, lowerLimit, upperLimit):
        ''' Used to run the check given by the task:
        is the sum of the factorial of the digits equal to the number itself?'''

        for number in range(lowerLimit, upperLimit + 1):
            if self.isDigitFactorialNumber(number):
                print("hit:", number)

        print("... done ...")

    # ----------------------------

    def isDigitFactorialNumber(self, number):
        # convert to digits
        digits = [int(digit) for digit in str(number)]
        # compute the sum of the factorials of the digits
        summed = sum([self.factDict[digit] for digit in digits])
        # are the equal?
        return summed == number

# ------------------------------------------------------------------------------

foo = FactorialChecker()

print("145?", foo.isDigitFactorialNumber(145))
print("123?", foo.isDigitFactorialNumber(123))

foo.computeResultsForRange(0, 1000)