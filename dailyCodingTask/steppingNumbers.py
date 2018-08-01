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