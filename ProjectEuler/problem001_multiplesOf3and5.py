# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

#----------------------------------------------------------------------------------------

def sumOfMultiplesOf3And5Below(limit):
    print(limit)
    allNumbers = list(range(1, limit + 1))
    print(allNumbers)
    allMultiples = [x for x in allNumbers if (x % 3 == 0 or x % 5 == 0)]
    print(allMultiples)
    return sum(allMultiples)

#----------------------------------------------------------------------------------------

# limit=10; expect: 23
print(sumOfMultiplesOf3And5Below(10))

# limit 1000: result?
print(sumOfMultiplesOf3And5Below(1000))