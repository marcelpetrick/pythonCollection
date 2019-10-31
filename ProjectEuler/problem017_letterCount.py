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
            #(0, "zero"),
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

        self.stringHundredAnd = "hundred and"

    # ------------------------------------------------------------------------------

    def convertNumberToString(self, number):
        if number < 0 or number > 1000:
            raise Exception("Wrong input value.")

        if number == 1000:
            return "one thousand"

        amountOfHundreds = number // 100
        rest = amountOfHundreds % 100

        stringLastTwoDigits = ""
        if rest > 0: # zero has no words ..
            if rest < 20:
                stringLastTwoDigits = self.numberDict[rest]
            else:
                amountOfTens = (rest // 10) * 10
                rest = rest - amountOfTens
                stringLastTwoDigits =  self.numberDict[amountOfTens] + " " + self.numberDict[amountOfTens]

        resultString = self.numberDict[amountOfHundreds] + " " + self.stringHundredAnd + " " + stringLastTwoDigits

        return resultString

    # ------------------------------------------------------------------------------

    def lettersOfNumberAsWord(self, number):
        return len(self.convertNumberToString(number))

    # ------------------------------------------------------------------------------

    def driverMethod(self):
        amountOfCharsNeeded = 0
        for number in range(1, 1000 + 1):
            print("loop:", number, "-->", self.lettersOfNumberAsWord(number))
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
        print("final score is:", instance.driverMethod())
        self.assertTrue(1337)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
