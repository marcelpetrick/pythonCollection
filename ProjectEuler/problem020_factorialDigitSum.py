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

    return 1

# ------------------------------------------------------------------------------

number = 100
print("Fcatorial digit sum of", number, "is:", factorialDigitSum(number))
