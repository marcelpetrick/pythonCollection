# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# ------------------------------------------------------------------------------

def sumSquareDifference(number):

    listList = list(range(1, number+1))
    sumOfSquares = sum([elem ** 2 for elem in listList])
    squareOfSum = sum(listList) ** 2
    #print(sumOfSquares)
    #print(squareOfSum)
    print("result:", squareOfSum - sumOfSquares)

# ------------------------------------------------------------------------------

sumSquareDifference(10)
sumSquareDifference(100)

# ------------------------------------------------------------------------------

# result: 2640
# result: 25164150

# Sorry, no unit-testing for this. Not sure why it was a "problem" at all!

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 6 is correct.
#
# You are the 406105th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.