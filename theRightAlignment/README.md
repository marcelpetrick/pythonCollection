 # How to use?
 
 Invoke on the files of the last commit with parallel processing (note: must have `parallel` installed!)  
 `$  git diff --name-only HEAD~1 HEAD | parallel --bar python theRightAlignment.py`

# Tested
So far no issues in the wild could be observed regarding right-aligning c++ files (macros, etc ..).
For Qt-ui files a special rule for the very first line had to be introduced. don#t align the line with "<?xml version="1.0" encoding="UTF-8"?>", else parsing fails.
