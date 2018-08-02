# Stepping Numbers
# Given two integers ‘n’ and ‘m’, find all the stepping numbers in range [n, m].
# A number is called stepping number if all adjacent digits have an absolute difference of 1. 321 is a Stepping Number while 421 is not.
#
# Examples :
# Input : n = 0, m = 21
# Output : 0 1 2 3 4 5 6 7 8 9 10 12 21
#
# Input : n = 10, m = 15
# Output : 10, 12

def printSteppingNumbersInRange(m, n):
    '''
    @param: m begin (inclusive)
    @param: n end (inclusive)
    '''

    results = []

    for number in range(m, n + 1): # n should be inclusive, therefore +1
        print(number)
        if isSteppingNumber(number):
            results.append(number)

    return results

def isSteppingNumber(number):
    returnValue = False

    if (str(number).__len__() == 1):
        returnValue = True
    else:
        pass #todo

    return returnValue

print(printSteppingNumbersInRange(0, 3))