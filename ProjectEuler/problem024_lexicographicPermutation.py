# Lexicographic permutations
#
# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# ------------------------------------------------------------------------------

# idea: brute force; just count upwards, check if the number would be a valid permutation ..
#
# since the first idea did not really work and was inefficient
# 0. generate all permutations of 0123.456.789. since they should be lexicographic, the first digits wont have changed.
# means: how many of the last digits have to be permutated to achieve the millionth permutation?

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

##############
# dead code! #
##############

# print(1*2*3*4*5*6*7*8*9*10)
#
# def generatePermut(inputString):
#     if len(inputString) == 0:
#         return []
#
#     if len(inputString) == 1:
#         return [inputString]
#
#     # take the first elem, permut the rest, apply the first to all of th rest
#     head = inputString[:1]
#     rest = inputString[1:]
#     print(inputString, ":", head, " - ", rest)
#     permuts = generatePermut(rest)
#     print("permuts:", permuts)
#
#     # put now the first elem to all possible positions of the permuts
#     results = []
#     # TODO
#     #for i in range(0, len)
#
#     return results
#
# generatePermut("abc")
#
# # early exit
# exit(0)
#
# # init
# comparisonList = []
# for i in range(0,10):
#     comparisonList.append(str(i))
#
# def isValidPermutation(number):
#     asListOfChars = [x for x in str(number)]
#     asListOfChars.sort()
#     #print("as char:", asListOfChars)
#     return asListOfChars == comparisonList
#
# #print(comparisonList)
# #print("1234567890:", isValidPermutation(1234567890))
# #print("1234567810:", isValidPermutation(1234567810))
#
# # the function
# currentNumber = 1023456789
# numberOfValidPermutations = 0 # is the x-th permutation in lexicographic order
# while True:
#     if isValidPermutation(currentNumber):
#         numberOfValidPermutations += 1
#         print(numberOfValidPermutations, ":", currentNumber)
#
#         if numberOfValidPermutations == 1000000:
#             break
#
#     currentNumber += 1
#
# # ------------------------------------------------------------------------------
# # 999993 : 3782914506
# # 999994 : 3782914560
# # 999995 : 3782914605
# # 999996 : 3782914650
# # 999997 : 3782915046
# # 999998 : 3782915064
# # 999999 : 3782915406
# # 1000000 : 3782915460
#
# # Sorry, but the answer you gave appears to be incorrect.
#
# # ------------------------------------------------------------------------------

import itertools as EiTeh
import time as Taim
startTime = Taim.time()
listOfAllPermuts = list(EiTeh.permutations([0,1,2,3,4,5,6,7,8,9]))
print("permut creation took:", Taim.time() - startTime, "s")
#exit(0)
print("all permutations:")
print(listOfAllPermuts[0])
print(listOfAllPermuts[1])
print(listOfAllPermuts[2])
print(listOfAllPermuts[1000000 - 1]) # indexing issue!

asString = ""
for elem in listOfAllPermuts[1000000 - 1]:
    asString += str(elem)
print("result:", asString)

# permut creation took: 0.5242722034454346 s
# all permutations:
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# (0, 1, 2, 3, 4, 5, 6, 7, 9, 8)
# (0, 1, 2, 3, 4, 5, 6, 8, 7, 9)
# (2, 7, 8, 3, 9, 1, 5, 4, 6, 0)
# result: 2783915460
