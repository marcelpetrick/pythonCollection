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
# loop: 960 --> ninehundredandsixty --> 19
# loop: 961 --> ninehundredandsixtyone --> 22
# loop: 962 --> ninehundredandsixtytwo --> 22
# loop: 963 --> ninehundredandsixtythree --> 24
# loop: 964 --> ninehundredandsixtyfour --> 23
# loop: 965 --> ninehundredandsixtyfive --> 23
# loop: 966 --> ninehundredandsixtysix --> 22
# loop: 967 --> ninehundredandsixtyseven --> 24
# loop: 968 --> ninehundredandsixtyeight --> 24
# loop: 969 --> ninehundredandsixtynine --> 23
# loop: 970 --> ninehundredandseventy --> 21
# loop: 971 --> ninehundredandseventyone --> 24
# loop: 972 --> ninehundredandseventytwo --> 24
# loop: 973 --> ninehundredandseventythree --> 26
# loop: 974 --> ninehundredandseventyfour --> 25
# loop: 975 --> ninehundredandseventyfive --> 25
# loop: 976 --> ninehundredandseventysix --> 24
# loop: 977 --> ninehundredandseventyseven --> 26
# loop: 978 --> ninehundredandseventyeight --> 26
# loop: 979 --> ninehundredandseventynine --> 25
# loop: 980 --> ninehundredandeighty --> 20
# loop: 981 --> ninehundredandeightyone --> 23
# loop: 982 --> ninehundredandeightytwo --> 23
# loop: 983 --> ninehundredandeightythree --> 25
# loop: 984 --> ninehundredandeightyfour --> 24
# loop: 985 --> ninehundredandeightyfive --> 24
# loop: 986 --> ninehundredandeightysix --> 23
# loop: 987 --> ninehundredandeightyseven --> 25
# loop: 988 --> ninehundredandeightyeight --> 25
# loop: 989 --> ninehundredandeightynine --> 24
# loop: 990 --> ninehundredandninety --> 20
# loop: 991 --> ninehundredandninetyone --> 23
# loop: 992 --> ninehundredandninetytwo --> 23
# loop: 993 --> ninehundredandninetythree --> 25
# loop: 994 --> ninehundredandninetyfour --> 24
# loop: 995 --> ninehundredandninetyfive --> 24
# loop: 996 --> ninehundredandninetysix --> 23
# loop: 997 --> ninehundredandninetyseven --> 25
# loop: 998 --> ninehundredandninetyeight --> 25
# loop: 999 --> ninehundredandninetynine --> 24
# loop: 1000 --> onethousand --> 11
# final score is: 21151
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.054s
#
# OK
#
# Process finished with exit code 0
