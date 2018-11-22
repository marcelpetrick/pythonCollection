# This problem was asked by Two Sigma.
#
# Using a function rand7() that returns an integer from 1 to 7 (inclusive)
# with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

import random

# given
def rand7():
    return random.randint(1, 7)

# to implement: idea: just drop all values bigger than 5.
# todo proof statistically that this is really the case
def rand5():
    result = rand7()
    while result > 5:
        result = rand7()

    return result

# ---------- test -----------------

#for _ in range(10):
#    print(rand7())


for _ in range(100):
    print(rand5())