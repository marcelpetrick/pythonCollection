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
# * it is clear that integer 987654321 * {1} is the lower limit, which has to be obeyed
# * also the number has to be 9-pandigital with 9 digits
# * brute force would be: count up from 1 to 10 ** 10 (max): then a second loop which goes from 1 to "concatenated result is longer than 9 digits"
# ** do precheck if length is 9 digits, then check if pandigital
#
# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
