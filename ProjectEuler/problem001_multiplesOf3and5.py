# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

#----------------------------------------------------------------------------------------

def sumOfMultiplesOf3And5Below(limit):
    print("\nsumOfMultiplesOf3And5Below with limit", limit, "yields:")
    allNumbers = list(range(1, limit))
    print(allNumbers)
    allMultiples = [x for x in allNumbers if (x % 3 == 0 or x % 5 == 0)]
    print(allMultiples)
    return sum(allMultiples)

#----------------------------------------------------------------------------------------

# limit=10; expect: 23
print("->", sumOfMultiplesOf3And5Below(10))

# limit 1000: result?
print("->", sumOfMultiplesOf3And5Below(1000))
# 233168 - is proven correct

#----------------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 1 is correct.
#
# You are the 773168th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you had previously solved was 0%.
# This is a new record. Well done!