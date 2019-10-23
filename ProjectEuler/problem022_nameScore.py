# Names scores
#
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

# idea:
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
import time
import unittest
# ------------------------------------------------------------------------------
def prepareInput():

    # open
    file = open('problem022_names.txt', 'r')

    # prepare result container
    listOfCleanedNames = list()

    # read content
    for line in file.readlines():
        splitLine = line.split(",")
        for item in splitLine:
            cleanItem = item.replace("\"", "")
            #print("cleanItem:", cleanItem)
            listOfCleanedNames.append(cleanItem)

    return listOfCleanedNames
# ------------------------------------------------------------------------------
def calcValueOfName(name):

    characterValues = sum([(ord(c) - 64) for c in name])
    return characterValues
#-------------------------------------------------------------------------------
def calcNameScore():
    inputList = prepareInput()
    print("inputList:", inputList)
    inputList.sort();
    print("inputList:", inputList)

    position = 1 # damn Project Euler ... starting to count positions with 1 and not 0!
    fileResultSum = 0
    for name in inputList:
        calculatedValue = calcValueOfName(name)
        finalValue = position * calculatedValue
        print(name, ":", calculatedValue, " * ", position, " => ", finalValue)
        position -=-1

        fileResultSum += finalValue

    return fileResultSum

# ------------------------------------------------------------------------------
class Testcase(unittest.TestCase):
    def test_calcValueOfName(self):
        self.assertEqual(1, calcValueOfName("A"))
        self.assertEqual(53, calcValueOfName("COLIN"))

    def test_finalRun(self):
        print("final score is:", calcNameScore())
        self.assertTrue(1337)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
# last run:
# ..
# ZULMA : 73  *  5162  =>  376826
# final score is: 870873746
#
#
# second try with first position = 1:
# 871198282
#
# Congratulations, the answer you gave to problem 22 is correct.
#
# You are the 124097th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%. 
