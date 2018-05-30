# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#-------------------------------------------------------------------
###########################################################################
# naive implementation: no optimization, runtime O(n^2) du to "contains") #
###########################################################################

def firstNaiveApproach(inputList, expectedSum):
    #print("firstNaiveApproach:", inputList, expectedSum)

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
###########################################################################
# naive implementation: no optimization, runtime O(n^2) du to "contains") #
###########################################################################

def mappedFunction(inputList, expectedSum):
    found = False
    dictionary = {}
    for elem in inputList:
        #print("processing:", elem)
        # put the current value into the dictionary
        if elem in dictionary:
            dictionary[elem] += 1
        else:
            dictionary[elem] = 1

        remainder = expectedSum - elem #todo: check that not negative; todo check that remainder != elem
        if remainder in dictionary:
            #print("found the entry:", remainder)
            found = True
            break
        #else:
            #print("remainder not found :(", remainder)

    return found

#-------------------------------------------------------------------
#############
# execution #
#############

inputList = [10, 5, 3, 7, 12]
k = 17
print("For k = %i the list %s yields %s" % (k, inputList, firstNaiveApproach(inputList, k)))
k = 16
print("For k = %i the list %s yields %s" % (k, inputList, firstNaiveApproach(inputList, k)))
print("#####################################")
k = 17
print("For k = %i the list %s yields %s" % (k, inputList, mappedFunction(inputList, k)))
k = 16
print("For k = %i the list %s yields %s" % (k, inputList, mappedFunction(inputList, k)))
