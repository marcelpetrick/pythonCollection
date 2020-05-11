# task: take a given filename
# get the information of GetFileVersionInfo - maybe return as string (filename + version)

# ----------------------------------------------------------------------------------------------------------------

def getVersionString(filename):
    # inspiration taken from: http://timgolden.me.uk/python/win32_how_do_i/get_dll_version.html
    from win32api import GetFileVersionInfo, LOWORD, HIWORD

    info = GetFileVersionInfo(filename, "\\")
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

print("getVersionStringWithFilename:", getVersionStringWithFilename("C:\Windows\\twain_32.dll")) # the need for doubled backslashes is not good
# will print: "getVersionStringWithFilename: C:\Windows\twain_32.dll ; 1.7.1.3" - which fits :)

# todo Add function to give a directory; parse its file-contents and then print the list of: name + versionStr

# ----------------------------------------------------------------------------------------------------------------

def printDllVersionContentToStdOut(filepath):
    # todo check if this exists

    # todo get list of all files: rglob?

    # todo run and print for each file: getVersionStringWithFilename(..)

    pass

# ----------------------------------------------------------------------------------------------------------------
