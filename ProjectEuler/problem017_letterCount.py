# Number letter counts
#
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# ------------------------------------------------------------------------------
# idea:

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

class NumbersToWords:
    def __init__(self):

        # how to make this "static"?
        # create a list of tuples, which is then converted to a dictionary
        self.numberDict = dict([
            (0, ""),
            (1, "one"),
            (2, "two"),
            (3, "three"),
            (4, "four"),
            (5, "five"),
            (6, "six"),
            (7, "seven"),
            (8, "eight"),
            (9, "nine"),
            (10, "ten"),
            (11, "eleven"),
            (12, "twelve"),
            (13, "thirteen"),
            (14, "fourteen"),
            (15, "fifteen"),
            (16, "sixteen"),
            (17, "seventeen"),
            (18, "eighteen"),
            (19, "nineteen"),
            (20, "twenty"),
            (30, "thirty"),
            (40, "forty"),
            (50, "fifty"),
            (60, "sixty"),
            (70, "seventy"),
            (80, "eighty"),
            (90, "ninety")
            # values more than hundred are determined by calculation
        ])
        #print("numberDict:", self.numberDict)

        self.stringHundred = "hundred"

        self.stringAnd = "and"

    # ------------------------------------------------------------------------------

    def convertNumberToString(self, number):
        if number < 0 or number > 1000:
            raise Exception("Wrong input value.")

        if number == 1000:
            return "onethousand" # no space

        amountOfHundreds = number // 100
        rest = number % 100

        stringLastTwoDigits = ""
        if rest > 0: # zero has no words ..

            # add an "and" in case there were hundreds
            if amountOfHundreds > 0:
                stringLastTwoDigits += self.stringAnd

            if rest < 20:
                stringLastTwoDigits += self.numberDict[rest]
            else:
                #print("incoming remainder is:", rest)
                amountOfOnes = rest % 10
                amountOfTens = rest - amountOfOnes
                #print("amountOfTens:", amountOfTens, "amountOfOnes:", amountOfOnes)
                stringLastTwoDigits += self.numberDict[amountOfTens] + " " + self.numberDict[amountOfOnes]

        # constructing the result: first the hundreds ..
        resultString = ""
        if amountOfHundreds > 0:
            resultString += self.numberDict[amountOfHundreds] + " " + self.stringHundred + " "
        # .. then the last two digits
        resultString += stringLastTwoDigits

        # almost forgot to omit counting the spaces!
        resultString = resultString.replace(" ", "")
        print(number, "-->", resultString)

        return resultString

    # ------------------------------------------------------------------------------

    def lettersOfNumberAsWord(self, number):
        return len(self.convertNumberToString(number))

    # ------------------------------------------------------------------------------

    def driverMethod(self):
        amountOfCharsNeeded = 0
        for number in range(1, 1000 + 1):
            #print("loop:", number, "-->", self.convertNumberToString(number), "-->", self.lettersOfNumberAsWord(number))
            amountOfCharsNeeded += self.lettersOfNumberAsWord(number)
        return amountOfCharsNeeded

    # ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_calcValueOfName(self):
        instance = NumbersToWords()
        self.assertEqual(23, instance.lettersOfNumberAsWord(342))
        self.assertEqual(20, instance.lettersOfNumberAsWord(115))

    def test_finalRun(self):
        instance = NumbersToWords()
        print("-----------------")
        print("final score is:", instance.driverMethod())
        self.assertTrue(1337)

# # ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

#instance = NumbersToWords()
#print("final score is:", instance.driverMethod())

# ------------------------------------------------------------------
# ..
# 995 --> ninehundredandninetyfive
# 996 --> ninehundredandninetysix
# 997 --> ninehundredandninetyseven
# 998 --> ninehundredandninetyeight
# 999 --> ninehundredandninetynine
# final score is: 21124
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.022s

# ------------------------------------------------------------------

# Congratulations, the answer you gave to problem 17 is correct.
#
# You are the 140179th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%

