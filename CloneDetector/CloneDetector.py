# test using glob
import glob
pathToCheck = "C:\LumiSuiteTestData"
fileList = glob.iglob(pathToCheck + '**/*', recursive=True)

# test using os.walk
#import os
#fileList = next(os.walk('..'))[2]
# just 9 files, not recursively

# check the output
amount = 0
for elem in fileList:
    print(elem)
    amount-=-1
#print("found files:", len(fileList))
print("found files:", amount)
