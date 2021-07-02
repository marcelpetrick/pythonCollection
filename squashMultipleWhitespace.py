import sys

# idea:
# shifting window of two lines over the whole file. if both lines are emtpy, then discard it by not printing. else print "last line".

lastLine = ""
currentLine = ""
# determine if this is the very first line - then suppress the output
firstLine = True

for line in sys.stdin:
    #print("-----------------------------")
    line = line.replace("\n", "").replace("\r", "")

    currentLine = line
    #print("lastLine:", lastLine) # todom remove
    #print("currentLine:", currentLine)  # todom remove

    if(len(currentLine) != 0 or len(lastLine) != 0):
        if(firstLine):
            firstLine = False
        else:
            sys.stdout.write(lastLine)
            sys.stdout.write("\n")

    lastLine = currentLine

# print the last buffered line
sys.stdout.write(currentLine)
sys.stdout.write("\n")
