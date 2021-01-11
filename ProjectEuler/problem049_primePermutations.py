# Prime permutations
#
# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers
# are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

# ------------------------------------------------------------------------------
# idea:
# * hint: "An arithmetic sequence is a sequence of numbers such that the difference of any two successive members
# of the sequence is a constant. Example. 2,4,6,8,10….is an arithmetic sequence with the common difference 2." (google)
# * create all permutations of 4 (digits) (or just 4-tuple?) out of digits from 1..9 (by a generator, not in memory)
# * compute all permuts of this 4-tuple, then check if prime, then store all primes for that: and determine of any
# 3-set the arithm. difference (also called: offset)?
#
# alternative approach: create all primes below 10.000 (four digits), then condense them into a map of ordered digits: key is the ascending order; values is then a list of the primes.
# for each elem of the list, check then for difference ... first: just lists with at least two items (or three? i find the description ambiguous)

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# reuse code from previous solution: will require the existing numpy!
# TODO maybe consider to use a prime-generator, which is proven and tested; see problem041
def getPrimesUntilLimit(limit):
    from ProjectEuler.problem668_numpy import sieveEras  # works, but just after commenting lots of code inside that file
    primes = sieveEras(limit, False) # this is also a mistake in the second parameter
    #print(len(primes), ":", primes)  # 78,498 for 10 ** 6 - which is correct
    return primes

# ------------------------------------------------------------------------------

def createAscendingOrderedDigitString(number):
    ''' Take input number, convert to string, sort ascending, return combined string. '''
    charList = ''.join(sorted(str(number)))
    return charList

# ------------------------------------------------------------------------------

def mapAllPrimesWithNormalizedStringAsKey(limit):
    allPrimes = getPrimesUntilLimit(limit)

    mappingDict = dict()
    for prime in allPrimes:
        normForm = createAscendingOrderedDigitString(prime)

        # check first if a list has to be created
        if normForm not in mappingDict:
            mappingDict[normForm] = []

        formerValue = mappingDict[normForm]
        formerValue.append(prime)
        mappingDict[normForm] = formerValue

    return mappingDict

# test run
def theProgram():
    limit = 10000
    mapped = mapAllPrimesWithNormalizedStringAsKey(limit)
    print("mapped:", mapped)
    filtered = {k: v for k, v in mapped.items() if len(v) > 1 and len(k) == 4} # list comprehension for a map, OMG!
    print("filtered:", filtered)
    # lacks sorting: https://stackoverflow.com/questions/1479649/readably-print-out-a-python-dict-sorted-by-key
    for key, value in sorted(filtered.items(), key=lambda x: x[0]):
        print("{} : {}".format(key, value))

# ------------------------------------------------------------------------------
def findCandidates(input):
    # todo implement until the new unit-test works!
    return []
# ------------------------------------------------------------------------------

import unittest
class Testcase(unittest.TestCase):
    def test_createAscendingOrderedDigitString(self):
        self.assertEqual("1337", createAscendingOrderedDigitString(1337))
        self.assertEqual("1337", createAscendingOrderedDigitString(7331))
        self.assertEqual("1337", createAscendingOrderedDigitString(1733))

    def test_findCandidates(self):
        # quote: "The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,"
        input = [1487, 1847, 4817, 4871, 7481, 7841, 8147, 8741]
        result = [1487, 4817, 8147]
        self.assertEqual(findCandidates(input), result)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
# ------------------------------------------------------------------------------
