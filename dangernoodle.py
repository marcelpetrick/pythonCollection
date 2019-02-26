import sys

for line in sys.stdin:
	stringi = line + " --> " + str(len(line))
	stringi = stringi.replace("\n", "")
	stringi = stringi.replace("\r", "")
	stringi += "\n"
	sys.stdout.write(stringi)

	
# invoke with:

#$ cd /c/Repos && cat buildStats_LumiSuite.txt | cut -c 1-8 | uniq -c | python dangernoodle.py
#      7 20181017-->17
#     23 20181018-->17
#     38 20181019-->17
#     ...
