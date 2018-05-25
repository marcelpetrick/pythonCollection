import fileinput
import sys
import os

#------------------------------------------
def addMacroToFile(filename, newStatement):
    #print("called addMacroToFile:", filename, determinePositionOfLastBrace(filename))

    returnValue = "fail"
    posLastBrace = determinePositionOfLastBrace(filename)
    posCurrentLine = 1
    for line in fileinput.input(filename, inplace=True):
        # add additional line in case of matching last brace
        if posCurrentLine == posLastBrace:
            sys.stdout.write(newStatement)
            sys.stdout.write("\n") # newline, else it would be put just before the brace
            returnValue = "success"

        sys.stdout.write(line) # prints without additional newline (on windows)
        posCurrentLine += 1

    return returnValue

#------------------------------------------
# return the position of the last brace.
# possible improvement: in case of some malformed mpc: skip ..
def determinePositionOfLastBrace(filename):
    lastPos = -1
    position = 1
    with open(filename, "r") as file: #has implicit close - which is nice
        for line in file:
            if line.__contains__("}"):
                lastPos = position
            position += 1

    return lastPos

# ------------------------------------------
# find all mpb/mpc files
def fixAllFilesRecursively(path, suffix, newStatement):
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirname, filename)
            if full_path.endswith(suffix):
                print(full_path)
                wasSuccessful = addMacroToFile(full_path, newStatement)
                if wasSuccessful == "success":
                    print("  modified :)")

        # prevent recursion into those subdirs with meta-data
        if '.svn' in dirnames:
            dirnames.remove('.svn')
        if '.git' in dirnames:
            dirnames.remove('.git')

#------------------------------------------
#------------------------------------------

path = "D:\Repo_INS_RADARNX"
suffix = "mpc"
newStatement = "	macros += QT_MESSAGELOGCONTEXT"
# TODO possible improvement: prevent double application of the added macro ..
fixAllFilesRecursively(path, suffix, newStatement)
