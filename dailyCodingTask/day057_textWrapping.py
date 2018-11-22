# This problem was asked by Amazon.
#
# Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less.
# You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.
#
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
#
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
# ["the quick", "brown fox", "jumps over", "the lazy", "dog"].No string in the list has a length of more than 10.
##########################################################

import unittest

# ------------------------------------------------------------------------------

def lazybuttWrapText(s, k):
    '''
    :param s - input string
    :param k - length in integer of desired substrings'''
    print("lazybuttWrapText called with: ", s, " and length ", k)
    returnValue = []

    splitString = s.split(" ")

    # lazybutt-wrap: check if each element is a fitting substring and then just return this!
    allElementsOfValidLength = True
    for elem in splitString:
        if elem.__len__() > k:
            allElementsOfValidLength = False
            break
        print("check now:", elem) # todo remove: to see if break works

    if allElementsOfValidLength:
        print("yes, fits!")
        returnValue = splitString
    # end of lazybutt-version

    return returnValue

# ------------------------------------------------------------------------------

def wrapText(s, k):
    '''
    :param s - input string
    :param k - length in integer of desired substrings'''
    print("wrapText called with: ", s, " and length ", k)

    # my idea:
    # - split the whole text into substrings
    #- their length should be then used to "try" out all possible permutation-sums with a length less-equal the given length
    # would be: 3, 5, 5, 3, 5, 4, 3, 4, 3
    #- but when computing the length of concatenated words, then don't forget the space between as +1!
    splitString = s.split(" ")
    print("splitString", splitString)

    returnValue = wrapTextHelper(splitString, k)
    return returnValue

def wrapTextHelper(inputList, k):
    ''' Same like the real function, just with list of split words instead of the string. '''
    print("#############################################################")
    print("wrapText called with: ", inputList, " and length ", k)
    returnValue = []

    # find first what would be the maximum lookahead with the given splits
    greedyLookAhead = greedyMatch(inputList, k)
    print("greedyMatch:", greedyLookAhead)

    # todo try from max to 1 if the rest would return fitting stuff; in case the rest is at least one element big
    for max in range(greedyLookAhead, 0, -1):
        print("max:", max)
        # prepare the remaining list
        remainingList = inputList.copy()
        for amountOfPops in range(0, max, 1):
            #print("pop")
            remainingList.pop(0)
        print("remainingList:", remainingList)

        # todo test if the remaining list is at least one element big
        if remainingList.__len__() == 0:
            print("len == 0")
            # then we have a valid splitting! :)
            returnValue.append(listOfFirstXItemsToString(inputList, max))

            print("valid wrapping found - no remainder left: will return now:", returnValue)
            break
        else:
            print("len != 0")
            resultFromWrappingTheRest = wrapTextHelper(remainingList, k)
            print("resultFromWrappingTheRest:", resultFromWrappingTheRest) # just for checking
            if resultFromWrappingTheRest.__len__() > 0: # not empty means success!
                # todo result is list of (concatenated) substrings
                print("got valid result from the call on remaining elements:", resultFromWrappingTheRest)
                returnValue.append(listOfFirstXItemsToString(inputList, max))

                for elem in resultFromWrappingTheRest:
                    returnValue.append(elem)
                print("will return therefore:", returnValue)
                break

    return returnValue

# ------------------------------------------------------------------------------

def listOfFirstXItemsToString(list, amount):
    print("listOfFirstXItemsToString: with", list, "and", amount)

    firstItems = list[0:amount]  # slice it # todo improve, because this part comes twice!
    concatenatedString = ""
    for elem in firstItems:
        concatenatedString += elem + " "
    concatenatedString = concatenatedString.rstrip(" ")  # just to prevent the trailing space ;) #todo improve

    print(" ->returnValue:", concatenatedString)

    return concatenatedString

# ------------------------------------------------------------------------------

def greedyMatch(list, k):
    ''' Find the amount of items which would be smaller-equal the given k. '''
    returnValue = 0
    currentLength = 0

    for elem in list:
        if (currentLength + elem.__len__()) <= k:
            returnValue += 1 # add the current element
            currentLength += elem.__len__() + 1 # add it to the current length; plus one because of the needed space between the words
        else:
            #print("stop!")
            break

    return returnValue

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    ''' Tests for day56_textWrapping.py '''

    def test0(self):
        s = "the quick brown fox jumps over the lazy dog"
        k = 10
        expectedResult = ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
        output = wrapText(s, k)
        self.assertEqual(output, expectedResult)
        print(" --> input", s, " with length ", k, "yielded result:", output, ":)")

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

print("############################################################")
print("should not work:", lazybuttWrapText("klaushaus", 2))
print("should work:", lazybuttWrapText("klaushaus", 20))
print("############################################################")

# real version
s = "the quick brown fox jumps over the lazy dog"
k = 10
output = wrapText(s, k)
print(" --> input", s, " with length ", k, "yielded result:", output, ":)")