# idea: create files with random binary content (written to disk) - see how much throughput is possible

#-----------------------------

def groundSpace():

    print("before writing")
    listOfItems = [123, 124, 64, 98, 12]
    byteArray = bytearray(listOfItems)
    with open('temporaryFile.tmp', 'w+b') as tempFile:
        tempFile.write(byteArray)

    print("done writing")

#-----------------------------

groundSpace()
