# This problem was asked by Facebook.
#
# Given a number in Roman numeral format, convert it to decimal.
#
# The values of Roman numerals are as follows:
#
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
#
# In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
#
# For the input XIV, for instance, you should return 14.

# ------------------------------------------------------------------------------

import unittest
import re # for regular expression checking

# ------------------------------------------------------------------------------

conversionTable = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

# ------------------------------------------------------------------------------

def convertRomanToDecimal(input):
    # first: convert to upp-case
    romanNumber = str(input).upper()
    #print("romanNumber: ", romanNumber)

    # check if it consists only of the allowed letters
    pattern = re.compile("[MDCLXVI]+")
    for elem in romanNumber:
        if not pattern.match(elem):
            print(input, "is not a valid input! Only digits from [MDCLXVI] allowed.")
            return -1

    # convert the given input
    decimalValue = 0
    previousNumber = 1001
    for digit in romanNumber:
        valueForCurrentDigit = conversionTable[digit]
        #print("\t", valueForCurrentDigit)
        decimalValue += valueForCurrentDigit

        if previousNumber < valueForCurrentDigit:
            # remove the previousNumberTwice (because it has to be removed and it was added once too much)
            decimalValue -= 2* previousNumber

        previousNumber = valueForCurrentDigit

    return decimalValue

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_wrongInput(self):
        self.assertEqual(-1, convertRomanToDecimal("A"))
        self.assertEqual(-1, convertRomanToDecimal("IQ"))

    def test_simpleNumbers(self):
        self.assertEqual(1, convertRomanToDecimal("I"))
        self.assertEqual(2, convertRomanToDecimal("II"))
        self.assertEqual(3, convertRomanToDecimal("III"))
        self.assertEqual(1, convertRomanToDecimal("i"))
        self.assertEqual(2, convertRomanToDecimal("ii"))
        self.assertEqual(3, convertRomanToDecimal("iii"))

        self.assertEqual(8, convertRomanToDecimal("viii"))

        self.assertEqual(1666, convertRomanToDecimal("MDCLXVI"))

    def test_subtractionRule(self):
        # see: https://www.roemische-zahlen.net/
            # 1. Regel: I steht nur vor V und X
            # 2. Regel: X steht nur vor L und C
            # 3. Regel: C steht nur vor D und M
        self.assertEqual(9, convertRomanToDecimal("IX"))
        self.assertEqual(1984, convertRomanToDecimal("MCMLXXXIV"))

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
