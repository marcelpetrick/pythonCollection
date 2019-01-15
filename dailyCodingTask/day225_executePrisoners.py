# This problem was asked by Bloomberg.
#
# There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with
# the kth person, and removing every successive kth person going clockwise until there is no one left.
#
# Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
#
# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
#
# Bonus: Find an O(log N) solution if k = 2.

# ------------------------------------------------------------------------------
# idea:
# * todo

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

class SpecialArray(object):

    def __init__(self, n, k):
        #print("Stack: ctor :)")
        self.__n__ = n
        self.__k__ = k
        # init the array
        self.__array__ = ["alive"] * self.__n__
        self.__position__ = -1

    # ------------------------------------------------

    def getNumberOfPeopleAlive(self):
        amount = 0
        for elem in self.__array__:
            if elem == "alive":
                amount += 1

        return amount

    #------------------------------------------------

    # attention: can run into infinite looping! check before if getNUmberOfPeopleAlive >= 1!
    def executeNext(self):
        #print("executeNext:")
        #print("self.__k__:", self.__k__)
        #print("range(self.__k__):", range(self.__k__))

        length = len(self.__array__)

        for step in range(self.__k__):
            #print("\t", step)
            self.__position__ = (self.__position__ + 1) % length

            # continue to move if the current one is already dead
            while self.__array__[self.__position__] == "dead":
                self.__position__ = (self.__position__ + 1) %  length

            #print("\tfound one at", self.__position__)

        # execute him
        self.__array__[self.__position__] = "dead"

        #print("-- end of executeNext --")

    # ------------------------------------------------

    def getCurrentPosition(self):
        return 1 + self.__position__

    # ------------------------------------------------

    def getNextManStandingPosition(self):
        length = len(self.__array__)
        position = self.__position__
        while self.__array__[position] == "dead":
            position = (position + 1) % length

        return position

    # ------------------------------------------------

    # representation: empty Stack -> ""; else "elem0;elem1;elem2;.."
    def __repr__(self):
        result = ""

        for elem in self.__array__:
            result += elem + ";"

        return result


# ------------------------------------------------------------------------------

# attention: k-th Person, so [1,2,3,4,5]. Not starting with 0!
def bestStandingPosition(n, k):
    ''' Will return -1 for "error". '''

    # add some checks for valid n and k
    if n <= 0:
        return -1

    if k <= 0:
        return -1

    # prepare an array
    array = SpecialArray(n, k)

    #print("array:", array, array.getNumberOfPeopleAlive())
    #array.executeNext()
    #print("array:", array, array.getNumberOfPeopleAlive())

    while array.getNumberOfPeopleAlive() > 1:
        array.executeNext()
        print("array:", array, "|| people left:", array.getNumberOfPeopleAlive(), "|| killed:", array.getCurrentPosition())

    #print("--->")
    #print("array:", array, array.getCurrentPosition())

    return array.getNextManStandingPosition() + 1 # plus one to have proper "index"

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenChallengeExample(self):
        n, k  = 5, 2
        expectedOutput = 3
        computedOutput = bestStandingPosition(n, k)
        self.assertEqual(expectedOutput, computedOutput)
