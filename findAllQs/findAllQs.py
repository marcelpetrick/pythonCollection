# @author mail@marcelpetrick.it
# @see: README.md

#---------------------------------------------------------------------------------------------------------
def scanFileForQ(filename):
    import re

    results = set()

    reading_file = open(filename, "r")
    for line in reading_file:
        normalized = line.strip()
        #print("normalized:", normalized)

        if "Q_" in normalized and normalized.endswith(";"):
            #print(line)

            # todo put all cropped substrings into a set
            hit = re.search('Q_(.+?)\(', normalized) # search for substring between Q_ and the opening bracket
            # todo error: Q_NAMESPACE; is missing
            if (hit):
                #print("hit:", hit.group(1))
                results.add("Q_" + hit.group(1)) # prefix this again
            else:
                hit = re.search('Q_(.+?);', normalized) # between Q_ and ; - to find those mistakes like "Q_OBJECT;"
                if (hit):
                    results.add("Q_" + hit.group(1)) # prefix this again

    reading_file.close()

    return results

#---------------------------------------------------------------------------------------------------------

results = scanFileForQ("C:/vmSharedFolder/pedantic_output.txt")
print("results:")
print("---------------")
for elem in results:
    print(elem)
print("---------------")
#---------------------------------------------------------------------------------------------------------
# results:
# ---------------
# Q_NAMESPACE
# Q_ENUM_NS
# Q_OBJECT
# Q_LOGGING_CATEGORY
# Q_DECLARE_OPERATORS_FOR_FLAGS
# Q_DECLARE_FLAGS
# Q_DECLARE_LOGGING_CATEGORY
# Q_DECLARE_METATYPE
# Q_PROPERTY
# ---------------
#
# Process finished with exit code 0
