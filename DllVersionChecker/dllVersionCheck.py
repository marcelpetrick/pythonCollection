# task: take a given filename
# get the information of GetFileVersionInfo - maybe return as string (filename + version)

# taken from: http://timgolden.me.uk/python/win32_how_do_i/get_dll_version.html
from win32api import GetFileVersionInfo, LOWORD, HIWORD

def get_version_number (filename):
  info = GetFileVersionInfo (filename, "\\")
  ms = info['FileVersionMS']
  ls = info['FileVersionLS']
  return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)

def getVersionString(filename):
  import os
  filename = os.environ["COMSPEC"]
  versionStr = ".".join ([str (i) for i in get_version_number (filename)])
  return versionStr


getVersionString()