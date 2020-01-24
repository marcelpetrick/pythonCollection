# Cubic permutations
#
# Problem 62
# The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

#-------------------
# idea:
# * naively computing for each number (increasingly upwards) the cube. then checking all permutations if they are true
# cubes would take ages, or? is the given hint with three digit cube-bases a lie?
# * wha t about precomputing a LUT with given cubes for all numbers up to a certain limit (number of digits)?
#-------------------
# init step for the LUT
import time
startTime = time.time()
fatCubeDict = dict()
for i in range(0, 10000):
    fatCubeDict[i] = i ** 3
print("creating cube LUT took:", time.time() - startTime, "s")
print("cube LUT:", fatCubeDict)
#-------------------
import itertools
def determineAmountOfFittingPermutations(number):
    amountOfCubes = 0 # start with zero, because input itself will be also checked
    cubes = set()
    for tuple in itertools.permutations(str(number)):
        permutNumberToCheck = "".join(tuple)
        while permutNumberToCheck[0] == "0":
            permutNumberToCheck = permutNumberToCheck[1:]

        if int(permutNumberToCheck) in fatCubeDict.values():
            #print("hit:", permutNumberToCheck)
            amountOfCubes += 1
            cubes.add(int(permutNumberToCheck))

    return cubes
#-------------------
#print("41063625 has", determineAmountOfFittingPermutations(41063625))

#-------------------
import time
numberToCheck = 1
runStartTime = time.time()
while True:
    # the number to check has to be a cube itself, so just count upwards from 0
    # and cube-ify it
    numbercube = numberToCheck ** 3
    startTime = time.time()
    cubes = determineAmountOfFittingPermutations(numbercube)
    endTime = time.time()
    cubesAmount = len(cubes)

    if cubesAmount > 1:
        print(numberToCheck, "->", numbercube, "->", cubesAmount, ":", cubes, "in", endTime - startTime, "s, (whole run:", time.time() - runStartTime, "s)")

        if cubesAmount == 5:
            exit(1337)

    numberToCheck += 1

