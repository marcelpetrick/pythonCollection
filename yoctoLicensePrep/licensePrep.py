# License file preparator for Yocto-libs
# @see README.md

#------------------------------------------------------------------------------------------------------

def handleFilesRecursively(path, prefix):
    print("go")
    import os

    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirname, filename)
            if full_path.startswith(prefix):
                print(full_path)

                # todo continue here
#------------------------------------------------------------------------------------------------------

# test run
prefix = "generic_"
path = "./testFolder"
handleFilesRecursively(path, prefix)
