# License file preparator for Yocto-libs
# @see README.md

#------------------------------------------------------------------------------------------------------

def handleFilesRecursively(path, prefix):
    import os

    for dirname, dirnames, filenames in os.walk(path):
        #print("iter:", dirname, dirnames, filenames) # todom remove
        for filename in filenames:
            if filename.startswith(prefix):
                fullPath = os.path.join(dirname, filename)
                print("proper file:", fullPath)

                # copy file with new name
                resultPath = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/licenses"
                #resultPath = "C:\Users\MarcelP\Desktop\MarcelsFolder\coding\pythonCollection\yoctoLicensePrep\licenses"
                copyFile(path, fullPath, resultPath)

#------------------------------------------------------------------------------------------------------
def copyFile(originalPath, file, resultPath):
    print("copyFile:", originalPath, file, resultPath)

    tail = remove_prefix(file, originalPath)
    print("tail:", tail)  # todom remove
    # remove leading "\" and replace the second one with underscore
    finalName = tail[1:].replace("\\", "_")
    print("finalName:", finalName) # todom remove
    

#------------------------------------------------------------------------------------------------------
# no Python 3.9, so <https://stackoverflow.com/a/16892491>
def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]
#------------------------------------------------------------------------------------------------------

# test run
prefix = "generic_"
path = "C:/Users/MarcelP/Desktop/MarcelsFolder/coding/pythonCollection/yoctoLicensePrep/testFolder"
#path = "C:\Users\MarcelP\Desktop\MarcelsFolder\coding\pythonCollection\yoctoLicensePrep\\testFolder"
handleFilesRecursively(path, prefix)
