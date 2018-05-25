import fileinput
import sys
import os

#------------------------------------------
def addVc14ToMpb(filename):
    #print("called addVc14ToMpb:", filename)

    for line in fileinput.input(filename, inplace=True):
        if line.__contains__("vc13") and not line.__contains__("vc14"):
            line = line.replace("vc13", "vc13, vc14", 1) # replace once

        sys.stdout.write(line) # prints without additional newline (on windows)

# ------------------------------------------
# find all mpb/mpc files
def fixAllFilesRecursively(path, suffix):
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirname, filename)
            if full_path.endswith(suffix):
                print(full_path)
                addVc14ToMpb(full_path)

        # prevent recursion into those subdirs with meta-data
        if '.svn' in dirnames:
            dirnames.remove('.svn')
        if '.git' in dirnames:
            dirnames.remove('.git')

#------------------------------------------
#------------------------------------------

path = "D:\Dependencies_VS2013_Win32\synapsis\E03.14fake"
suffix = "mpb"
fixAllFilesRecursively(path, suffix)
