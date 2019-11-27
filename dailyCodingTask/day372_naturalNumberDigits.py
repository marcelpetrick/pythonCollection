# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Write a function that takes a natural number as input and returns the number of digits the input has.
#
# Constraint: don't use any loops.

# ------------------------------------------------------------------------------
# idea: Not sure if this is a joke?!?
# Stringification would be possible and the just call len(..).
# Or mathematical: log10 of the number, then rounded up.

# ------------------------------------------------------------------------------

def digitsOfInput(number):
    import math

    if number < 0:
        raise ValueError("Just natural numbers please.")

    return math.ceil(math.log10(number + 1))

def driverForTask():
    result = digitsOfInput(0)
    print("result:", result)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    driverForTask()
