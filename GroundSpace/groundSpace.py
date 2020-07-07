# idea: create files with random binary content (written to disk) - see how much throughput is possible

#-----------------------------

def groundSpace():

    #print("before writing")
    #listOfItems = [123, 124, 64, 98, 12]
    listOfItems = [0] * (2 ** 20)
    byteArray = bytearray(listOfItems)
    with open('temporaryFile.tmp', 'ba') as tempFile: # refer to this for the second param: https://docs.python.org/3/library/functions.html#open
        for a in range(2 ** 30):
            tempFile.write(byteArray)
            print("one loop-block done")

    #print("done writing")

#-----------------------------

# I am impressed: writes 8 GiB in some seconds ... can be maybe improved
# Samsung SSD 960 EVO 500GB achieves just 300 MB/s continuous
while True:
    groundSpace()
