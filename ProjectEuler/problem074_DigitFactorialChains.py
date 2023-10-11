# Digit Factorial Chains
#
#
# Problem 74
#
# The number
# is well known for the property that the sum of the factorial of its digits is equal to :
# Perhaps less well known is , in that it produces the longest chain of numbers that link back to
#
# ; it turns out that there are only three such loops that exist:
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
# Starting with
#
# produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

# idea:
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper

# ------------------------------------------------------------------------------

@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# ------------------------------------------------------------------------------
class Testcase(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

def benchmarkFactorial():
    import time
    start_time = time.time()
    for number in range(1, 1500):
        print(number, factorial(number))
    print("whole execution took %s seconds" % (time.time() - start_time)) # 0.1 seconds

#benchmarkFactorial()

# ------------------------------------------------------------------------------
# last run:
# ..
