# @brief License file preparator for Yocto-libs
# @see README.md
# @author: mail@marcelpetrick.it
# @spdx: GPL-3.0-or-later

#------------------------------------------------------------------------------------------------------
# open tasks:
# * add proper description
# * add a check if the target-directory exists -> else create one
# * add unit test
# * class-ify
# * won't do: maybe filter double licenses by check via hash, but: how to reference to the fitting license?
#   (maybe create a map of "license type -> libs")

#------------------------------------------------------------------------------------------------------
def handleFilesRecursively(inputPath, resultPath, prefix):
    import os

    for dirname, dirnames, filenames in os.walk(inputPath):
        #print("iter:", dirname, dirnames, filenames) # todom remove
        for filename in filenames:
            if filename.startswith(prefix):
                fullPath = os.path.join(dirname, filename)
                # print("proper file:", fullPath)
                # copy file with new name
                copyFile(inputPath, fullPath, resultPath)

#------------------------------------------------------------------------------------------------------
def copyFile(originalPath, file, resultPath):
    import shutil
    #print("----")
    #print("copyFile:", originalPath, file, resultPath)

    # name mangling
    tail = removePrefix(file, originalPath)
    #print("tail:", tail)  # todom remove
    # remove leading "\" and replace the second one with underscore
    # this is not working for *nix: because of the path-separator ('/') -> make it generic (or do it with OS-flags ..)
    finalName = tail[1:].replace("\\generic_", "_")
    #print("finalName:", finalName) # todom remove

    target = resultPath+"/"+finalName
    print("target:", target)
    shutil.copy(file, target)

#------------------------------------------------------------------------------------------------------
# no Python 3.9 for str.removeprefix ..
def removePrefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# call
def startPrep(inputPath, resultPath):
    import time

    # test run: hardcoded path - no kwargs 😬
    #inputPath = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/testFolder"
    # overwrite with real one
    if not inputPath:
        inputPath = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/yocto_license_tree/yocto_license_tree/licenses"
    if not resultPath:
        #resultPath = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/licenses"
        resultPath = "licenses"

    discriminatingPrefix = "generic_"

    startTime = time.time()
    handleFilesRecursively(inputPath, resultPath, discriminatingPrefix)
    print("preparation took", time.time()-startTime, "seconds") # preparation took 9.707338094711304 seconds

#------------------------------------------------------------------------------------------------------
# arg parsing for input
import argparse
import sys
import os

def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(description = 'Helper to collect and copy the license files')
    parser.add_argument('inputDirectory', help = 'Path to the input directory.')
    parser.add_argument('--outputDirectory', help = 'Path to the output that contains the license files.')
    return parser
#------------

if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    startPrep(parsed_args.inputDirectory, parsed_args.outputDirectory)
