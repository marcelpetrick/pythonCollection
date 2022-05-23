# @author mail@marcelpetrick.it

#-------------------------------
# @brief Discover device and try to switch it on/off.
# Follows https://github.com/marcelpetrick/pysispm/blob/master/examples/printenv.py
# Run with `sudo python3 powerCycle.py`- has to be sudo!
def powerCycle():
    import serial
    import sispm
    import time
    
    # defines
    id = '01:01:60:d0:e9' # checked with the enumeration below
    port = 1
    tty = '/dev/ttyUSB0'

    #print(sispm.get_num_devices())
    
    # Find Enermax devices.
    devices = sispm.connect()

    # Were they found?
    if len(devices) == 0:
        print('No device found')
        quit()

    # Find the device with the correct id
    dev = None
    for d in devices:
        print("sispm.getid(d):", sispm.getid(d))
        # sispm.getid(d): 01:01:60:d0:e9
        
        if sispm.getid(d) == id:
            dev = d
            print("found device with fitting id")
            break
    
    # report discovery-failure
    if dev is None:
        print("dev is None")
        print('Device ' + id + ' not found')
        quit()
        
    print("line 44: end of powerCycle()")

#-------------------------------

powerCycle()
