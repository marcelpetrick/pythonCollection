import time

#------------------------------------------------------------------------

class PrimeClass:
    ''' Precompute all primes up to a certain limit and store them for quicker access. '''

    def __init__(self, upperLimit):
        if upperLimit >= 2:
            self.upperLimit = upperLimit
        else:
            raise Exception("weird upper range - you get nothing!")

        # contains (in as ascending order) all found primes
        self.primeList = [2]

    # ------------------------------------------------------------------------

    def runInitialization(self):
        ''' Just compute all the primes up to the given limit. '''

        # two is initially already included, if the limit is just two, the 'nothing' happens here
        # stride length is two to avoid checks against "div 2" ..
        for primeCandidate in range(3, self.upperLimit + 1, 2):
            # assume it is prime until proven wrong
            isPrime = True

            for dividend in range (3, int(primeCandidate ** 0.5) + 1, 2):
                if primeCandidate % dividend == 0:
                    isPrime = False
                    break

            if isPrime:
                self.primeList.append(primeCandidate)

        return "to implement"

    #------------------------------------------------------------------------

    def getList(self):
        ''' attention: as copy! '''

        return self.primeList.copy()

#------------------------------------------------------------------------

pc = PrimeClass(100000) # 1000 000 : 78498 is correct; 1000:168 --> fits with: https://primes.utm.edu/howmany.html
startTime = time.time()
pc.runInitialization()
print(f"\t computation time: {time.time() - startTime} s" )
result = pc.getList() # acquire once, use multiple times
print("primes:", result)
print("amount:", len(result))

# precompute: 1 mio -> 3 s
# precompute 100000 (is sqrt(10 000 000 000)) -> computation time: 0.14261794090270996 s

# print the last five primes .. and they are correct: 99929 99961 99971 99989 99991 [100003]
print(result[-5:])