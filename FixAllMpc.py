import fileinput
import sys
import os

def addVc14ToMpb(filename):
    #print("called addVc14ToMpb:", filename)

    for line in fileinput.input(filename, inplace=True):
        #print("%d: %s" % (fileinput.filelineno(), line))
        if(line.__contains__("vc13") and not line.__contains__("vc14")):
            line = line.replace("vc13", "vc13, vc14", 1) # replace once

        #print(line) # output to file
        sys.stdout.write(line) # prints without additional newline (on windows)

# find all mpb/mpc files
path = "ADD HERE YOUR PATH"

for dirname, dirnames, filenames in os.walk(path):
    for filename in filenames:
        fullPath = os.path.join(dirname, filename)
        if(fullPath.endswith("mpb")): # or fullPath.endswith("mpc")):
            print(fullPath)
            addVc14ToMpb(fullPath)

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.svn' in dirnames:
        dirnames.remove('.svn')
    if '.git' in dirnames:
        dirnames.remove('.git')

quit(0) # stop here

#------------------------------------------

class FixAllMpc:
    '''
    Insert a certain given string into all mpc-files which are found in the directories below the current path.
    '''

    def __init__(self, givenPath, givenString):
        self.givenPath = givenPath
        self.givenString = givenString

    def __repr__(self):
        return "FixAllMpc: path=#%s# string=#%s#" % (self.givenPath, self.givenString)

# ------------------------------------------


    # find all files recursively which end with given suffix
    def findAllFiles(self, suffix):
        print("findAllFiles:", suffix)
        pass



#------------------------------------------

foo = FixAllMpc(".", "klaus")
print(foo)
foo.findAllFiles("mpc")
