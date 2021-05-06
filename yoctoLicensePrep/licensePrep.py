# License file preparator for Yocto-libs
# @see README.md

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
    print("----")
    print("copyFile:", originalPath, file, resultPath)

    tail = remove_prefix(file, originalPath)
    print("tail:", tail)  # todom remove
    # remove leading "\" and replace the second one with underscore
    finalName = tail[1:].replace("\\generic_", "_")
    print("finalName:", finalName) # todom remove

    import shutil
    target = resultPath+"/"+finalName
    print("target:", target)
    shutil.copy(file, target)

#------------------------------------------------------------------------------------------------------
# no Python 3.9 for str.removeprefix, so <https://stackoverflow.com/a/16892491>
def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

#------------------------------------------------------------------------------------------------------
# test run: hardcoded path - no kwargs 😬
inputPath = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/testFolder"
# overwrite with real one
inputPath = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/yocto_license_tree/yocto_license_tree/licenses"
resultPath = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/licenses"
discriminatingPrefix = "generic_"

# call
handleFilesRecursively(inputPath, resultPath, discriminatingPrefix)
