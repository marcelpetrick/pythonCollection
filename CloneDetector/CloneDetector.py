# test using glob
import glob
pathToCheck = "C:\LumiSuiteTestData"
fileList = glob.glob(pathToCheck + "/*", recursive=True)

# test using os.walk
import os
fileList = next(os.walk('..'))[2]
# just 9 files, not recursively

# check the output
for elem in fileList:
    print(elem)
print("found files:", len(fileList))
