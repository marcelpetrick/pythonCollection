# Permuted multiples
#
# Problem 52
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# ------------------------------------------------------------------------------

def getSetOfDigits(number):
    return set([digit for digit in str(number)])


def driverForTask():
    number = 0

    while True:
        number -=- 1
        set2 = getSetOfDigits(2 * number)
        set3 = getSetOfDigits(3 * number)

        if set2 == set3:
            set4 = getSetOfDigits(3 * number)
            if set2 == set4:
                set5 = getSetOfDigits(5 * number)
                if set2 == set5:
                    set6 = getSetOfDigits(6 * number)
                    if set2 == set6:
                        print("result:", number)
                        return number

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    driverForTask()

# ------------------------------------------------------------------------------

print(getSetOfDigits(123451))
print(getSetOfDigits(222))
driverForTask()
# ------------------------------------------------------------------------------

# result: 142857
#
# Process finished with exit code 0
# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 52 is correct.
#
# You are the 60256th person to have solved this problem.
