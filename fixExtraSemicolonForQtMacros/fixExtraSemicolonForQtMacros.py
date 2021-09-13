# @author mail@marcelpetrick.it

#---------------------------------------------------------------------------------------------------------
def fixExtraSemicolonForQtMacros():
    # determine given parameter
    import sys

    if len(sys.argv) < 2:
        print("too less args: first param = filename")
        exit(1)
    filename = sys.argv[1]
    if not filename:
        print("filename as input missing")
        exit(1)

    #print("----------------------------- handle now:", filename, "---------------") # remove later

    # replace with new line: " * @file	$filename$"
    # but just use the filename, discard the leading path!
    #newLine = " * @file    " + ntpath.basename(filename) + "\n" # also 4 spaces instead of tab

    # read everything in and store an edited version in buffer
    reading_file = open(filename, "r")
    new_file_content = ""#

    # handle all lines of the file
    for line in reading_file:
        # expand this ...
        hit = False
        givenQtMacros = {"Q_NAMESPACE", "Q_ENUM_NS", "Q_OBJECT", "Q_LOGGING_CATEGORY", "Q_DECLARE_OPERATORS_FOR_FLAGS",
                         "Q_DECLARE_FLAGS", "Q_DECLARE_LOGGING_CATEGORY", "Q_DECLARE_METATYPE", "Q_PROPERTY"}
        for macro in givenQtMacros:
            if macro in line:
                hit = True
                break

        if hit:
            line = line.replace(";", "")

        # append the processed line
        new_file_content += line #+ "\n"

    reading_file.close()

    # write to same file for replacing
    writing_file = open(filename, "w")
    writing_file.write(new_file_content)
    writing_file.close()
#---------------------------------------------------------------------------------------------------------
# this line must exist here to be callable from cmd with parameval
fixExtraSemicolonForQtMacros()
