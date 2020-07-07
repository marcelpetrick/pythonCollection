# idea: create files with random binary content (written to disk) - see how much throughput is possible

#-----------------------------

def groundSpace():

    #print("before writing")
    #listOfItems = [123, 124, 64, 98, 12]
    listOfItems = [0] * 1024
    byteArray = bytearray(listOfItems)
    with open('temporaryFile.tmp', 'ba') as tempFile: # refer to this for the second param: https://docs.python.org/3/library/functions.html#open
        for a in range(2 ** 10):
            tempFile.write(byteArray)

    #print("done writing")

#-----------------------------

# I am impressed: writes 8 GiB in some seconds ... can be maybe improved
while True:
    groundSpace()
