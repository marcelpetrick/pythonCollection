#!/bin/sh

# print some info about the device first
echo "---------------"
echo "installed bundle: $(cat /etc/os-version)"
echo "---------------"
echo "used HMI: $(cat /logging/p118/log.log | grep FD | tail -1)"
echo "---------------"
echo "firmware alternative: $(cat /sys/bus/i2c/devices/1-0041/*version)"
echo "---------------"
echo "md5 of firmware file: $(md5sum /lib/firmware/ilitek/ili251x.bin)"
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
echo "failed; check dmesg .."
echo "---------------"
