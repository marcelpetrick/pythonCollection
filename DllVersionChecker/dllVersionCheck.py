# task: take a given filename
# get the information of GetFileVersionInfo - maybe return as string (filename + version)

# ----------------------------------------------------------------------------------------------------------------

# todo Add function to give a directory; parse its file-contents and then print the list of: name + versionStr
def printDllVersionContentToStdOut(pathToCheck):
    from pathlib import Path

    # get all DLL-files
    for filename in Path(pathToCheck).rglob('*.dll'):
        # run the printer on them
        print(DllVersionProcessor.getVersionStringWithFilename(filename))

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

    # --------------------

    def getDictionaryOfFileVersions(self):

        resultValue = dict()

        return resultValue

    # --------------------

    def __createListOfFilesWithGivenSuffix(self):

        pass

    # todo question: how to unit-test private functions?

    # --------------------

    @staticmethod
    def getVersionString(fileName):
        # inspiration taken from: http://timgolden.me.uk/python/win32_how_do_i/get_dll_version.html
        from win32api import GetFileVersionInfo, LOWORD, HIWORD

        try:
            info = GetFileVersionInfo(str(fileName), "\\")
        except:
            return "---"  # f'failed for {filename}'

        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        versionAsList = [HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)]
        versionStr = ".".join([str(i) for i in versionAsList])

        return versionStr

    # --------------------

    @staticmethod
    def getVersionStringWithFilename(fileName):
        returnValue = str(fileName) + " ; " + DllVersionProcessor.getVersionString(fileName)

        return returnValue

# ----------------------------------------------------------------------------------------------------------------

# unit tests for the class
import unittest

# proper unit-test
class Testcase(unittest.TestCase):
    def test_DllVersionProcessor(self):
        processor = DllVersionProcessor(".", "*.dll")

        resultDict = processor.getDictionaryOfFileVersions()

        self.assertEqual(len(resultDict), 0)

    def test_getVersionString(self):
        result = DllVersionProcessor.getVersionString("C:\Windows\\twain_32.dll")
        self.assertEqual(result, "1.7.1.3") # yeah, maybe I should not do this - different Win-version, different result ;)

    def test_getVersionStringWithFilename(self):
        result = DllVersionProcessor.getVersionStringWithFilename("C:\Windows\\twain_32.dll")
        self.assertEqual(result, "C:\Windows\\twain_32.dll ; 1.7.1.3") # yeah, maybe I should not do this - different Win-version, different result ;)
        # deploying a custom-made DLL for testing would mitigate this

# ----------------------------------------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
# ----------------------------------------------------------------------------------------------------------------
