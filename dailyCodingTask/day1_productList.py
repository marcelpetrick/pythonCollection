# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would
# be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

# todo: implement the task
# write some unit-test


# idea:
# 0. create outputList with same size as given inputList; initialized with 1
# 1. iterate once over the inputList; multiply this element-wise to the outputList except at current position
def produceProductList(inputList):


#---------------------------------------------

innputList0 = [1, 2, 3, 4, 5]
innputList0 = [3, 2, 1]
