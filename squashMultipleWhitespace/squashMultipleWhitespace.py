import sys

lastLine = ""
currentLine = ""

for line in sys.stdin:
    currentLine = line
    if(len(currentLine) != 0 or len(lastLine) != 0):
        sys.stdout.write(lastLine)

    lastLine = currentLine

# print the last buffered line
sys.stdout.write(currentLine)
