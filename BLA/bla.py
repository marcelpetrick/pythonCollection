# extract zip archive to self-chosen directory
# parse its content for "warning:"
# get for each warning the cause as equivalence-class
# remove the unzipped directory
# print final statistics

def unzip(zipFilePath, unzipPath):
    from zipfile import ZipFile

    with ZipFile(zipFilePath, 'r') as zipObject:
        zipObject.extractall(unzipPath)

    pass

#--------------------

class BuildLogAnalyzer:

    def __init__(self):
        self.extractDir = "extractDir"
        self.zipFilePath = "testData.zip"

        # nothing so far
        pass

    # --------------------

    def unzip(self):
        from zipfile import ZipFile

        with ZipFile(self.zipFilePath, 'r') as zipObject:
            zipObject.extractall(self.extractDir)

        # todo some check for the content if it is not empty? or check for errors?
        # todo. determine the content; the filenames; and store them for later usage ..

    # --------------------

    def cleanup(self):
        import shutil
        shutil.rmtree(self.extractDir)

#--------------------

objectUnderTest = BuildLogAnalyzer()
objectUnderTest.unzip()
objectUnderTest.cleanup()

# todo add unit test before anything else!
