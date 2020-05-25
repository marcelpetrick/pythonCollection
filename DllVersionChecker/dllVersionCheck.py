# task: take a given filename
# get the information of GetFileVersionInfo - maybe return as string (filename + version)

# ----------------------------------------------------------------------------------------------------------------

def getVersionString(filename):
    # inspiration taken from: http://timgolden.me.uk/python/win32_how_do_i/get_dll_version.html
    from win32api import GetFileVersionInfo, LOWORD, HIWORD

    try:
        info = GetFileVersionInfo(str(filename), "\\")
    except:
        return "---" # f'failed for {filename}'

    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    versionAsList = [HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)]
    versionStr = ".".join([str(i) for i in versionAsList])

    return versionStr

# ----------------------------------------------------------------------------------------------------------------

def getVersionStringWithFilename(filename):
    returnValue = str(filename) + " ; " + getVersionString(filename)

    return returnValue

# ----------------------------------------------------------------------------------------------------------------

#print("getVersionStringWithFilename:", getVersionStringWithFilename("C:\Windows\\twain_32.dll")) # the need for doubled backslashes is not good
# will print: "getVersionStringWithFilename: C:\Windows\twain_32.dll ; 1.7.1.3" - which fits :)

# ----------------------------------------------------------------------------------------------------------------

# todo Add function to give a directory; parse its file-contents and then print the list of: name + versionStr
def printDllVersionContentToStdOut(pathToCheck):
    from pathlib import Path

    # get all DLL-files
    for filename in Path(pathToCheck).rglob('*.dll'):
        # run the printer on them
        print(getVersionStringWithFilename(filename))

# ----------------------------------------------------------------------------------------------------------------

pathToCheck = "C:/Program Files/Instrument Systems/LumiSuite SDK"
printDllVersionContentToStdOut(pathToCheck)

# todos:
# make it a class
# add unit-test-suite: check against twain32.dll (is and must be windows)
# add ui: just a button, where you pick with qfiledialog a path, then run the stuff
# for the ui-start: add start with param --gui
# maybe show the results as sortable table (with: remove those with version)
# move to dedicated repo

# ----------------------------------------------------------------------------------------------------------------

class DllVersionProcessor:

    def __init__(self, pathToCheck, suffixForFiltering):
        self.__pathToCheck = pathToCheck
        self.__suffixForFiltering = suffixForFiltering

    def getDictionaryOfFileVersions(self):

        resultValue = dict()

        return resultValue

    def __createListOfFilesWithGivenSuffix(self):

        pass

    # todo question: how to unit-test private functions?

# ----------------------------------------------------------------------------------------------------------------

# todo unit tests
import unittest

# proper unit-test
class Testcase(unittest.TestCase):
    def test_DllVersionProcessor(self):
        processor = DllVersionProcessor(".", "*.dll")

        resultDict = processor.getDictionaryOfFileVersions()

        self.assertEqual(len(resultDict), 0)

# ----------------------------------------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
# ----------------------------------------------------------------------------------------------------------------
