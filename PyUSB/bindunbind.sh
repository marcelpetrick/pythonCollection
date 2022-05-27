#!/bin/sh

# print some info about the device first
echo "installed bundle: $(cat /etc/os-version)"
echo "firmware information:"
cat /sys/devices/platform/soc@0/30800000.bus/30a30000.i2c/i2c-1/1-0041/{{firmware,kernel,protocol}_version,mode} 
echo "---------------"
# cycles
echo "Will do the unbind/bind-cycles now. Check with \"dmesg -w\" the output.\n"
CYCLES=0
while true ; do
	CYCLES=$((CYCLES+1))
        echo 1-0041 > /sys/bus/i2c/drivers/ili210x_i2c/unbind
        sleep 1
        echo 1-0041 > /sys/bus/i2c/drivers/ili210x_i2c/bind 
        sleep 1
        test -e /dev/input/touchscreen0 || break
        echo "ok: $CYCLES - $(date)"
done
