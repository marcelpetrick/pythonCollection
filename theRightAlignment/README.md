 # How to use?
 
 Invoke on the files of the last commit with parallel processing (note: must have `parallel` installed!)  
 `$  git diff --name-only HEAD~1 HEAD | parallel --bar python theRightAlignment.py`

# Open tasks
- test and verify if C++ macros will be broken
- Qt-ui files: don't align the first line with "<?xml version="1.0" encoding="UTF-8"?>", else parsing fails
