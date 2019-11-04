# test using glob
import glob
from pathlib import Path

pathToCheck = "C:\LumiSuiteTestData"
fileList = []
for filename in Path(pathToCheck).rglob('*.*'):
    fileList.append(filename)

# check the output
for elem in fileList:
    print(elem)
print("amount of found files:", len(fileList))
