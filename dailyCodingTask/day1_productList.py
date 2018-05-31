# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would
# be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

# done: implement the task
# todo: write some unit-test


# idea:
# 0. create outputList with same size as given inputList; initialized with 1
# 1. iterate once over the inputList; multiply this element-wise to the outputList except at current position
def produceProductList(inputList):
    # save the length, because needed three times
    listLength = len(inputList)

    # prepare an initialized list (value 1) of the given input-length
    returnValue = [1] * listLength

    # do the multiplication
    for indexInput in range(listLength):
        currentMultiplier = inputList[indexInput]
        # inner loop
        #print(range(len(returnValue))) #todom remove
        for indexOutput in range(len(returnValue)):
            if indexInput != indexOutput:
                #print("indexOutput: ", indexOutput) #todom remove
                returnValue[indexOutput] *= currentMultiplier

    return returnValue

#---------------------------------------------

innputList0 = [1, 2, 3, 4, 5]
innputList1 = [3, 2, 1]

#todo write a decorator for that
print(innputList0, "->", produceProductList(innputList0))
print(innputList1, "->", produceProductList(innputList1))

