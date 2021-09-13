# @author mail@marcelpetrick.it

#---------------------------------------------------------------------------------------------------------
def fixExtraSemicolonForQtMacros():
    # determine given parameter
    import sys
    #import ntpath

    if len(sys.argv) < 2:
        print("too less args: first param = filename")
        exit(1)
    filename = sys.argv[1]
    if not filename:
        print("filename as input missing")
        exit(1)

    print("----------------------------- handle now:", filename, "---------------") # remove later

    # replace with new line: " * @file	$filename$"
    # but just use the filename, discard the leading path!
    #newLine = " * @file    " + ntpath.basename(filename) + "\n" # also 4 spaces instead of tab

    # read everything in and store an edited version in buffer
    reading_file = open(filename, "r")
    new_file_content = ""#

    # handle all lines of the file
    for line in reading_file:
        print(line)
        # expand this ...
        if "Q_OBJECT" in line:
            line = line.replace(";", "")

        # append the processed line
        new_file_content += line #+ "\n"

    reading_file.close()

    # write to same file for replacing
    writing_file = open(filename, "w")
    writing_file.write(new_file_content)
    writing_file.close()
#---------------------------------------------------------------------------------------------------------

# just for testing
# python fixExtraSemicolonForQtMacros.py "testInputFile.cpp"
