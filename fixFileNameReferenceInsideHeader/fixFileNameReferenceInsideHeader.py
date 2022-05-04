# Small script to insert the filename as string to the header of the qml/h/cpp-file. Sometimes they were missing despite @file.
#
# @author mail@marcelpetrick.it

# -----------------------------------------------------------
def insertFilenameIntoHeader():
    # determine given parameter
    import sys
    import ntpath

    if len(sys.argv) < 2:
        print("too less args: first param = filename")
        exit(1)
    filename = sys.argv[1]
    if not filename:
        print("filename as input missing")
        exit(1)

    print("----------------------------- handling:", filename, "---------------") # remove later

    # replace with new line: " * @file	$filename$"
    # but just use the filename, discard the leading path!
    newLine = " * @file    " + ntpath.basename(filename) + "\n" # also 4 spaces instead of tab

    # read everything in and store an edited version in buffer
    reading_file = open(filename, "r")
    new_file_content = ""

    for line in reading_file:
        if ("@file") in line:
            print(line, " --> ", newLine)
            line = newLine

        new_file_content += line #+ "\n"

    reading_file.close()

    # write to same file for replacing
    writing_file = open(filename, "w")
    writing_file.write(new_file_content)
    writing_file.close()
# -----------------------------------------------------------
def removeSuperflousStructuringLines():
    # determine given parameter
    import sys
    import ntpath

    if len(sys.argv) < 2:
        print("too less args: first param = filename")
        exit(1)
    filename = sys.argv[1]
    if not filename:
        print("filename as input missing")
        exit(1)

    print("----------------------------- handling:", filename, "---------------") # remove later

    # read everything in and store an edited version in buffer
    reading_file = open(filename, "r")
    new_file_content = ""
    stuffToRemove = {
        "Private methods",
        "Public methods"
        "Protected methods",
        "SOF",
        "EOF"
    }
    outputLine = True

    for line in reading_file:
        for waste in stuffToRemove:
            if line.__contains__(waste)
        if waste.lower() in line.lower():
            print("waste found")
            outputLine = False

        if outputLine:
            new_file_content += line #+ "\n"

    reading_file.close()

    # write to same file for replacing
    writing_file = open(filename, "w")
    writing_file.write(new_file_content)
    writing_file.close()
# -----------------------------------------------------------

# first fix the headers
insertFilenameIntoHeader()
# then remove the crap
removeSuperflousStructuringLines()
