# Factorial digit sum
#
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# ------------------------------------------------------------------------------

def factorialDigitSum(number):
    if number < 1:
        raise ValueError("Input must be greater 0")

    # self implemented factorial
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1

    # convert to string, then sum all digits
    return sum([int(elem) for elem in str(factorial)])

# ------------------------------------------------------------------------------

number = 100
print("Factorial digit sum of", number, "is:", factorialDigitSum(number))

# ------------------------------------------------------------------------------
# Fcatorial digit sum of 100 is: 648
#
# Process finished with exit code 0
# ------------------------------------------------------------------------------
# Congratulations, the answer you gave to problem 20 is correct.
#
# You are the 185298th person to have solved this problem.

# simpler:
import math
print("Factorial digit sum of", number, "is:", sum([int(elem) for elem in str(math.factorial(number))]))
