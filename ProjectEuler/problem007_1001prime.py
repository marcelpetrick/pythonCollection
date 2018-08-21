# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def isPrime(input):
    upperLimit = input // 2 + 1
    #print(list(range(2, upperLimit)))
    for x in range(2, upperLimit): # is -1
        #print("input:", input, "test:", x)
        if input % x == 0:
            #print("is dividing!")
            return False
    # else we have a prime if we reached this
    return True

# ------------------------------------------------------------------------------

def getPrime():
    currentNumber = 1
    while True:
        currentNumber += 1
        if isPrime(currentNumber):
            yield currentNumber

# ------------------------------------------------------------------------------

def getPrimeNumber(number):
    primes = getPrime()
    for i in range(1, number):
        primes.__next__()
    return primes.__next__()

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(True, isPrime(2))
        self.assertEqual(True, isPrime(3))
        self.assertEqual(False, isPrime(6))
        self.assertEqual(True, isPrime(7))
        self.assertEqual(False, isPrime(16))
        self.assertEqual(False, isPrime(25))
        self.assertEqual(True, isPrime(29))
        self.assertEqual(False, isPrime(87))
        self.assertEqual(True, isPrime(89))

    def test_getPrimeNumber(self):
        self.assertEqual(2, getPrimeNumber(1))
        self.assertEqual(7, getPrimeNumber(4)) # shuffled order
        self.assertEqual(3, getPrimeNumber(2))
        self.assertEqual(13, getPrimeNumber(6))

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

isPrime(6)

primes = getPrime()
for i in range(0,10):
    print(primes.__next__())

# ------------------------------------------------------------------------------

print("getPrimeNumber(10001):", getPrimeNumber(10001))