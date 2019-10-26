# Coded triangle numbers
#
# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
# we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
# number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?

# ------------------------------------------------------------------------------

# idea:
# 0. read the file, split the line, compute for each word the value and while going through the list, find the maximum.
# 1. Then generate triangle numbers until you are bigger than that maximum. store the triangle numbers in a dictionary.
# 2. check for each word-value if triangle number: if yes, then +1
# 3. return the result -- profit
# ------------------------------------------------------------------------------

def prepareInput():

    # open
    file = open('problem042_words.txt', 'r')

    # prepare result container
    listOfCleanedNames = list()

    # read content
    for line in file.readlines():
        splitLine = line.split(",")
        for item in splitLine:
            cleanItem = item.replace("\"", "")
            #print("cleanItem:", cleanItem)
            listOfCleanedNames.append(cleanItem)

    return listOfCleanedNames
# ------------------------------------------------------------------------------
def calcValueOfName(name):

    characterValues = sum([(ord(c) - 64) for c in name])
    return characterValues
#-------------------------------------------------------------------------------

resultDict = dict()
for word in prepareInput():
    resultDict[word] = calcValueOfName(word)

print(resultDict)
maximum = max(resultDict, key=resultDict.get)
print(resultDict[maximum]) # 192

# triangle numbers up to 200 ... because of (n(n+1)/2 .. 20 at least

triangles = []
for i in range(1, 21):
    triangles.append(int(i * (i + 1) / 2))

print("triangles:", triangles)
print("names in list:", prepareInput().__len__())

print("triangle words in list", sum([calcValueOfName(word) in triangles for word in prepareInput()]))

# triangles: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
# names in list: 1786
# triangle words in list 162

# -------------------------
# Congratulations, the answer you gave to problem 42 is correct.
#
# You are the 68601st person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%. 
