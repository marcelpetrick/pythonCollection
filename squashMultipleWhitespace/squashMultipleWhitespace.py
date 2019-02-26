import sys

# idea:
# shifting window of two lines over the whole file. if both lines are emtpy, then discard it by not printing. else print "last line".

lastLine = ""
currentLine = ""

for line in sys.stdin:
    print("-----------------------------")
    currentLine = line
    print("lastLine:", lastLine) # todom remove
    print("currentLine:", currentLine)  # todom remove

    if(len(currentLine) != 0 or len(lastLine) != 0):
        sys.stdout.write(lastLine)

    lastLine = currentLine

# print the last buffered line
sys.stdout.write(currentLine)
