# -- Task --
#
# Provide means to retrieve for a given filename or path the version-information of the DLL.
# (See WinAPI GetFileVersionInfo).

# ----------------------------------------------------------------------------------------------------------------

#  -- TODO --
# ✓ make it a class
# ✓ add unit-test-suite: check against twain32.dll (is and must be windows)
# add ui: just a button, where you pick with qfiledialog a path, then run the stuff
# for the ui-start: add start with param --gui
# maybe show the results as sortable table (with: remove those with version)
# move to dedicated repo

# ----------------------------------------------------------------------------------------------------------------

class DllVersionProcessor:

    def __init__(self, pathToCheck, suffixForFiltering):
        self.__pathToCheck = pathToCheck

        # todo check if the given suffix fits the format; e.g. '*.dll'
        self.__suffixForFiltering = suffixForFiltering

    # --------------------

    def getDictionaryOfFileVersions(self):

        resultValue = dict()

        for filename in self.__createListOfFilesWithGivenSuffix():
            resultValue[filename] = self.getVersionString(filename)

        return resultValue

    # --------------------

    def __createListOfFilesWithGivenSuffix(self):
        from pathlib import Path

        resultValue = []

        for filename in Path(self.__pathToCheck).rglob(self.__suffixForFiltering):
            resultValue.append(filename)

        return resultValue

    # --------------------

    # todo question: how to unit-test private functions?

    # --------------------

    @staticmethod
    def getVersionString(filename):
        # inspiration taken from: http://timgolden.me.uk/python/win32_how_do_i/get_dll_version.html
        from win32api import GetFileVersionInfo, LOWORD, HIWORD

        try:
            info = GetFileVersionInfo(str(filename), "\\")
        except:
            return "---"  # f'failed for {filename}'

        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        versionAsList = [HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)]
        versionStr = ".".join([str(i) for i in versionAsList])

        return versionStr

    # --------------------

    @staticmethod
    def getVersionStringWithFilename(filename):
        returnValue = str(filename) + " ; " + DllVersionProcessor.getVersionString(filename)

        return returnValue

# ----------------------------------------------------------------------------------------------------------------

# unit tests for the class
import unittest

# proper unit-test
class Testcase(unittest.TestCase):
    def test_DllVersionProcessor_dirWithNoDll(self):
        processor = DllVersionProcessor(".", "*.dll")
        resultDict = processor.getDictionaryOfFileVersions()
        self.assertEqual(len(resultDict), 0)

    def test_DllVersionProcessor_sdkDir(self):
        processor = DllVersionProcessor("C:/Program Files/Instrument Systems/LumiSuite SDK (Internal)", "*.dll")
        resultDict = processor.getDictionaryOfFileVersions()
        print("result for the SDK-directory:")
        [print(key, ":", value) for key, value in resultDict.items()] # print line by line
        self.assertTrue(1 == 1) # nothing to do here ..

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
