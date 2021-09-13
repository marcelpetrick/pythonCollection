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
            if (hit):
                #print("hit:", hit.group(1))
                results.add(hit.group(1))

    reading_file.close()

    return results

#---------------------------------------------------------------------------------------------------------

results = scanFileForQ("C:/vmSharedFolder/pedantic_output.txt")
print("results:")
for elem in results:
    print(elem)
