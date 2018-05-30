# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#-------------------------------------------------------------------

def firstNaiveApproach(inputList, expectedSum):
    #print("firstNaiveApproach:", inputList)

    found = False
    for elem in inputList:
        missing = expectedSum - elem
        #contained = inputList.__contains__(missing)
        #print("\tmissing ", missing, " is contained?", contained)
        if inputList.__contains__(missing):
            found = True
            break

    return found

#-------------------------------------------------------------------

inputList = [10, 5, 3, 7]
k = 17
result = firstNaiveApproach(inputList, k)
resultString = "For k = %i the list %s yields %s" % (k, inputList, result)
print(resultString)
