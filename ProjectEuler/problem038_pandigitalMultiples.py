# Pandigital multiples
#
# Problem 38
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
# of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
# with (1,2, ... , n) where n > 1?

# ------------------------------------------------------------------------------
# idea:
# * it is clear that integer 987654321 * {1} is the lower limit, which has to be obeyed (edit: since n should be bigger 1, this is wrong)
# * also the number has to be 9-pandigital with 9 digits
# * brute force would be: count up from 1 to 10 ** 10 (max): then a second loop which goes from 1 to "concatenated result is longer than 9 digits"
# * only check until 10 ** 6, because includes all 1,2,3,4,5 digit-numbers. which can be combined into a 9 digit number
# ** do precheck if length is 9 digits, then check if pandigital
#
# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# taken from euler041:
def isPandigital(number):
    ''' An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. '''
    stringified = str(number)
    length = len(stringified)

    if length > 9:
        return False

    for i in range(1, length + 1):
        # print(i)
        if str(i) not in stringified:
            return False

    return True

# ------------------------------------------------------------------------------

# crude and brute ..
ten10 = 10 ** 10
#ten9 = 10 ** 9
ten8 = 10 ** 8
ten6 = 10 ** 6

def determine_largest9PandigitalNumber_bruteForce():
    biggestResult = 0

    # loop over the possible numbers
    integer = 0
    while integer < ten6:
        integer += 1
        if len(str(integer)) not in [1, 2, 3, 4, 5, 9]:
            continue
        #print(integer)

        # # "progress bar"
        # if integer % ten8 == 0:
        #     print(integer // ten8, "% computed")

        # find the proper multiplicator
        multiplicator = 1
        while True:
            # generate the number
            currentNumber = ""
            for m in range(1, multiplicator+1):
                currentNumber += str(m * integer)
            #print(currentNumber, "generated from", integer, "and", multiplicator)
            # check if length fits
            if len(currentNumber) < 9:
                multiplicator += 1
                continue
            if len(currentNumber) > 9:
                break

            # check if pandigital
            currentNumberInt = int(currentNumber)
            if isPandigital(currentNumberInt):
                print("we have a hit ... now check if this is bigger than the saved one:", currentNumberInt, integer, multiplicator)

                if currentNumberInt > biggestResult:
                    biggestResult = currentNumberInt

            # if it was length of nine, then also break ... won't become better
            break

    print("final result:", biggestResult)

# ------------------------------------------------------------------------------

determine_largest9PandigitalNumber_bruteForce()

# ------------------------------------------------------------------------------

# ..
# we have a hit ... now check if this is bigger than the saved one: 793215864 7932 2
# we have a hit ... now check if this is bigger than the saved one: 926718534 9267 2
# we have a hit ... now check if this is bigger than the saved one: 927318546 9273 2
# we have a hit ... now check if this is bigger than the saved one: 932718654 9327 2
# final result: 932718654

# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 38 is correct.
#
# You are the 58714th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 25%.
