# test using glob

# -------------------------------------------
def md5(filename):
    import hashlib

    # hash blobs of 4096 byte size
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# -------------------------------------------

def sizeof_fmt(num, suffix='B'):
    # human readable version of the file size:
    # taken from: https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

# -------------------------------------------

#import glob
from pathlib import Path

pathToCheck = "C:\LumiSuiteTestData"
#pathToCheck = "C:/" # test your whole root .. lel

# TODO make this a real function with time measurement!
fileList = []
for filename in Path(pathToCheck).rglob('*.lsimg'):
    fileList.append(filename)

import os
import time
# check the output
for elem in fileList:
    currentTime = time.time()
    md5sum = md5(elem)
    print(elem, ":", sizeof_fmt(os.path.getsize(elem)), ":", md5sum, " - ", time.time() - currentTime, "s")
print("amount of found files:", len(fileList))
