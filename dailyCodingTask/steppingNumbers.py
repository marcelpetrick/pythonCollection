# Stepping Numbers
# Given two integers ‘n’ and ‘m’, find all the stepping numbers in range [n, m].
# A number is called stepping number if all adjacent digits have an absolute difference of 1.
# 321 is a Stepping Number while 421 is not.
#
# Examples :
# Input : n = 0, m = 21
# Output : 0 1 2 3 4 5 6 7 8 9 10 12 21
#
# Input : n = 10, m = 15
# Output : 10, 12

# ------------------------------------------------------------------------------

def printSteppingNumbersInRange(m, n):
    '''
    @param: m begin (inclusive)
    @param: n end (inclusive)
    '''

    results = []

    for number in range(m, n + 1): # n should be inclusive, therefore +1
        if isSteppingNumber(number):
            results.append(number)

    return results

# ------------------------------------------------------------------------------

def isSteppingNumber(number):
    numberOfDigits = str(number).__len__()
    if (numberOfDigits == 1):
        returnValue = True
    else:
        current = 0
        next = number % 10
        number //= 10
        returnValue = True
        for position in range(0, numberOfDigits - 1):
            # use div and mod to acquire the digits and check them
            current = next
            next = number % 10
            if(abs(next - current) != 1):
                #print("current and next differ by more than one:", current, next)
                returnValue = False
                break
            number //= 10

    #print("isSteppingNumber:", originalNumber, "returns", returnValue)
    #print("###################")
    return returnValue

# ------------------------------------------------------------------------------

print("-----------------------------------------------------------------------------")
print("range(10,15):", printSteppingNumbersInRange(10, 15))
print("range(0,100):", printSteppingNumbersInRange(0, 100))
