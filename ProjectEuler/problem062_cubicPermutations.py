# Cubic permutations
#
# Problem 62
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

#-------------------
# idea:
# * naively computing for each number (increasingly upwards) the cube. then checking all permutations if they are true
# cubes would take ages, or? is the given hint with three digit cube-bases a lie?
# * wha t about precomputing a LUT with given cubes for all numbers up to a certain limit (number of digits)?
#-------------------
#-------------------
#-------------------
