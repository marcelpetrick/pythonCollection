#!/bin/bash    

# author: mail@marcelpetrick.it
# date: 20220524
# version: 4

# Info: Script to run automated on/off-tests with a programmable power-outlet.
#       Does a cycle of "turn on, wait until booted, check if the touchcontroller-firmware-version is readable.
#       If yes, turn off outlet. Else just break and wait.
#
# Requires: sispmctl.py from https://github.com/xypron/pysispm/blob/master/examples/sispmctl.py
#           and the device put to outlet 1 (and configured wifi-access..)

echo "* turn off before first cycle *"
sudo ./sispmctl.py -f 1
sleep 1s

CYCLES=0

# cycle
while true; do
    # increment
    CYCLES=$((CYCLES+1))
    echo "-------------------- run $CYCLES / $(date) --------------------"
    
    # turn outlet 1 on
    echo "* turn on *"
    sudo ./sispmctl.py -o 1

    # wait for 20 s until the X BO booted
    sleep 20s

    # check the result of i2c bus

    echo "* ssh now *"
    # $ ssh root@192.168.100.21 cat /sys/devices/platform/soc@0/30800000.bus/30a30000.i2c/i2c-1/1-0041/{{firmware,kernel,protocol}_version,mode}
    # 0600.0000.b7cc.aa0a
    # 10.25.0d.00.01
    # 03.04
    # 5a.80:AP
    SSHRESULT=$(ssh root@192.168.100.21 cat /sys/devices/platform/soc@0/30800000.bus/30a30000.i2c/i2c-1/1-0041/{{firmware,kernel,protocol}_version,mode});
    echo "SSHRESULT=$SSHRESULT"
    
    # check the result; compare against first line "0600.0000.b7cc.aa0a"
    if [[ $SSHRESULT = *"0600.0000.b7cc.aa0a"* ]]; then
        echo "found version; driver works"
    else
        echo "version not found -> break!"
        date # timestamp
        break
    fi
    
    # wait
    sleep 1s

    # turn outlet 1 off
    echo "* turn off *"
    sudo ./sispmctl.py -f 1

    echo "* wait one more second *"
    sleep 1s

done # end of the while loop
