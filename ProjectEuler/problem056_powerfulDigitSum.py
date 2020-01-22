# Powerful digit sum
#
# Problem 56
# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large:
# one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

#----------

def computeDigitSum(a,b):
    # do it naively ... compute the power and then sum it
    power = a ** b
    result = sum([int(elem) for elem in str(power)])
    return result

#----------

limit = 100
currentMax = -1
maxA, maxB = 0, 0
for a in range(0, limit):
    for b in range(0, limit):
        digitSum = computeDigitSum(a, b)
        if digitSum > currentMax:
            print(a, b, "with", digitSum)
            currentMax = digitSum
            maxA, maxB = a, b

print("chonkiest", maxA, maxB, "with", computeDigitSum(maxA, maxB))

#----------
# ..
# 79 99 with 955
# 94 98 with 970
# 99 95 with 972
# chonkiest 99 95 with 972
#----------

#----------
#----------
