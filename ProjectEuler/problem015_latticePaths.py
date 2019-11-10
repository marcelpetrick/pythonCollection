# Lattice paths
#
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

# ------------------------------------------------------------------------------

# idea:
# first idea was to use some recursive backtracking to determine all routes. then i realized the following ..
# * there are just two alternatives at each node: right or down (short r and d). In a 2x2 lattice, there are six paths:
# this is also the amount of all (unique) permutations of "ddrr".
# So instead of determining the paths for 20x20 and then counting them, just get the size of the list of all
# permutations from 20 times d and 20 times r! :)

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
