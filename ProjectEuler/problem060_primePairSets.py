# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
# the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
# primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def isPrime(input):
    upperLimit = input // 2 + 1
    for x in range(2, upperLimit):
        if input % x == 0:
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

def createAllPairs(inputList, unique, sorted): # todo add default params
    ''' Create all 2-tuples for the given @param inputList.
    @param sorted is boolean and determines if the resulting list shall be sorted before return.
    @param unique determines if (a,b) AND (b,a) shall be part of the result-list.
    '''

    resultList = []
    #todo implement this ...

    # todo: redo this ... not working. maybe recursive is easier here (or use "itertools" ..)
    count = 0
    for elem in inputList:
        restList = inputList.copy()
        for a in range(0, count+1):
            restList.pop(0)
        print(elem, restList)
        for elemRest in restList:
            resultList.append((elem, elemRest))
            print((elem, elemRest))

    return resultList

# ------------------------------------------------------------------------------

def findLowestSumForNPrimePairSets(n):
    # todo: idea:
    # the set of n primes can be sorted; the biggest number will always be the "upper limit" -> so do some upward expanding loop?
    # done: reuse the isPrime-function
    # todo: needs a function which does all pair-shuffles for elements of a set (of primes)
    # todo check all possible pairs (front and back concatenation) if prime: exit early if not!
    # hint: 2 can't be in the set, else it would end up as pair-combination xyz2 - which is always multiple of 2, so not prime (optimization)

    return 792 # just for testing the unit-test
    #pass

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

    def test_findLowestSumForNPrimePairSets(self):
        self.assertEqual(792, findLowestSumForNPrimePairSets(4)) # given example

    def test_createAllPairs(self):
        # not enough input
        inputList = []
        expectedOutput = []
        self.assertEqual(expectedOutput, createAllPairs(inputList, True, False))
        # not enough input
        inputList = [1]
        expectedOutput = []
        self.assertEqual(expectedOutput, createAllPairs(inputList, True, False))
        # unique pairs
        inputList = [1, 2]
        expectedOutput = [(1,2)]
        self.assertEqual(expectedOutput, createAllPairs(inputList, True, True))
        # not unique pairs
        inputList = [1, 2]
        expectedOutput = [(1,2), (2,1)]
        self.assertEqual(expectedOutput, createAllPairs(inputList, False, True))

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

# this is the function which would yield the result
print("findLowestSumForNPrimePairSets(5):", findLowestSumForNPrimePairSets(5))
