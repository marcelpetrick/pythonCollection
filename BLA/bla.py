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

extractDir = "extractDir"
unzip("testData.zip", extractDir)
import shutil
shutil.rmtree(extractDir)
