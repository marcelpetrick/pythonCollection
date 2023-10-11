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

@memoize
def sumOfFactorialOfDigits(n):
    return sum([factorial(int(digit)) for digit in str(n)])

@memoize
def calculateChain(n):
    chain = [n]
    while True:
        n = sumOfFactorialOfDigits(n)
        if n in chain:
            #print("repeat!")
            break
        chain.append(n)
    #print(chain)
    return chain

def calculateChainsUpTo(limit, wantedLength):
    results = list()

    for i in range(1, limit+1):
        chain = calculateChain(i)
        currentLen = len(chain)
        if currentLen == wantedLength:
            #print(f"found chain of length {wantedLength} for {i}: {chain}")
            results.append(i)
    return results

def solveProblem():
    import time
    start_time = time.time()
    upperLimit = 10**6
    wantedLength = 60
    possibleChains = calculateChainsUpTo(upperLimit, wantedLength)
    print(f"found {len(possibleChains)} chains of length {wantedLength} up to {upperLimit}: {possibleChains}")
    print("whole execution took %s seconds" % (time.time() - start_time)) # 0.1 seconds

solveProblem()

# ------------------------------------------------------------------------------
class Testcase(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_sumOfFactorialOfDigits(self):
        self.assertEqual(sumOfFactorialOfDigits(145), 145)
        self.assertEqual(sumOfFactorialOfDigits(169), 363601)
        self.assertEqual(sumOfFactorialOfDigits(871), 45361)
        self.assertEqual(sumOfFactorialOfDigits(540), 145)

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
#
# found 402 chains of length 60 up to 1000000: [1479, 1497, 1749, 1794, 1947, 1974, 4079, 4097, 4179, 4197, 4709, 4719, 4790, 4791, 4907, 4917, 4970, 4971, 7049, 7094, 7149, 7194, 7409, 7419, 7490, 7491, 7904, 7914, 7940, 7941, 9047, 9074, 9147, 9174, 9407, 9417, 9470, 9471, 9704, 9714, 9740, 9741, 223479, 223497, 223749, 223794, 223947, 223974, 224379, 224397, 224739, 224793, 224937, 224973, 227349, 227394, 227439, 227493, 227934, 227943, 229347, 229374, 229437, 229473, 229734, 229743, 232479, 232497, 232749, 232794, 232947, 232974, 234279, 234297, 234729, 234792, 234927, 234972, 237249, 237294, 237429, 237492, 237924, 237942, 239247, 239274, 239427, 239472, 239724, 239742, 242379, 242397, 242739, 242793, 242937, 242973, 243279, 243297, 243729, 243792, 243927, 243972, 247239, 247293, 247329, 247392, 247923, 247932, 249237, 249273, 249327, 249372, 249723, 249732, 272349, 272394, 272439, 272493, 272934, 272943, 273249, 273294, 273429, 273492, 273924, 273942, 274239, 274293, 274329, 274392, 274923, 274932, 279234, 279243, 279324, 279342, 279423, 279432, 292347, 292374, 292437, 292473, 292734, 292743, 293247, 293274, 293427, 293472, 293724, 293742, 294237, 294273, 294327, 294372, 294723, 294732, 297234, 297243, 297324, 297342, 297423, 297432, 322479, 322497, 322749, 322794, 322947, 322974, 324279, 324297, 324729, 324792, 324927, 324972, 327249, 327294, 327429, 327492, 327924, 327942, 329247, 329274, 329427, 329472, 329724, 329742, 342279, 342297, 342729, 342792, 342927, 342972, 347229, 347292, 347922, 349227, 349272, 349722, 372249, 372294, 372429, 372492, 372924, 372942, 374229, 374292, 374922, 379224, 379242, 379422, 392247, 392274, 392427, 392472, 392724, 392742, 394227, 394272, 394722, 397224, 397242, 397422, 422379, 422397, 422739, 422793, 422937, 422973, 423279, 423297, 423729, 423792, 423927, 423972, 427239, 427293, 427329, 427392, 427923, 427932, 429237, 429273, 429327, 429372, 429723, 429732, 432279, 432297, 432729, 432792, 432927, 432972, 437229, 437292, 437922, 439227, 439272, 439722, 472239, 472293, 472329, 472392, 472923, 472932, 473229, 473292, 473922, 479223, 479232, 479322, 492237, 492273, 492327, 492372, 492723, 492732, 493227, 493272, 493722, 497223, 497232, 497322, 722349, 722394, 722439, 722493, 722934, 722943, 723249, 723294, 723429, 723492, 723924, 723942, 724239, 724293, 724329, 724392, 724923, 724932, 729234, 729243, 729324, 729342, 729423, 729432, 732249, 732294, 732429, 732492, 732924, 732942, 734229, 734292, 734922, 739224, 739242, 739422, 742239, 742293, 742329, 742392, 742923, 742932, 743229, 743292, 743922, 749223, 749232, 749322, 792234, 792243, 792324, 792342, 792423, 792432, 793224, 793242, 793422, 794223, 794232, 794322, 922347, 922374, 922437, 922473, 922734, 922743, 923247, 923274, 923427, 923472, 923724, 923742, 924237, 924273, 924327, 924372, 924723, 924732, 927234, 927243, 927324, 927342, 927423, 927432, 932247, 932274, 932427, 932472, 932724, 932742, 934227, 934272, 934722, 937224, 937242, 937422, 942237, 942273, 942327, 942372, 942723, 942732, 943227, 943272, 943722, 947223, 947232, 947322, 972234, 972243, 972324, 972342, 972423, 972432, 973224, 973242, 973422, 974223, 974232, 974322]
# whole execution took 9.652567148208618 seconds
