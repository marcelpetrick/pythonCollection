# idea: create files with random binary content (written to disk) - see how much throughput is possible

# todo:
# * gui (see mockup)
# * give option to write until disk full or "leave 100 MiB free"?; repeat option? one file or several files (uuid based?)

#-----------------------------

def groundSpace():

    #print("before writing")
    #listOfItems = [123, 124, 64, 98, 12]
    listOfItems = [0] * (2 ** 20)
    byteArray = bytearray(listOfItems)
    with open('temporaryFile.tmp', 'ba') as tempFile: # refer to this for the second param: https://docs.python.org/3/library/functions.html#open
        for a in range(2 ** 10):
            tempFile.write(byteArray)
        print("one GB written")

    #print("done writing")

#-----------------------------

# I am impressed: writes 8 GiB in some seconds ... can be maybe improved
# Benchmarks over several seconds on Win10; checked via TaskManager
# Samsung SSD 960 EVO 500GB achieves just 300 MB/s continuous
# sk hynix BC501 256 GB: 160 MB/s
while True:
    groundSpace()

#-----------------------------

# failure is reported like this
# ..
# one GB written
# one GB written
# Traceback (most recent call last):
#   File "C:/Users/husband-boy/Desktop/coding/pythonCollection/GroundSpace/groundSpace.py", line 23, in <module>
#     while True:
#   File "C:/Users/husband-boy/Desktop/coding/pythonCollection/GroundSpace/groundSpace.py", line 13, in groundSpace
#     tempFile.write(byteArray)
# OSError: [Errno 28] No space left on device
#
# Process finished with exit code 1
