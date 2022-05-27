#!/bin/sh
CYCLES=0
while true ; do
		CYCLES=$((CYCLES+1))
        echo 1-0041 > /sys/bus/i2c/drivers/ili210x_i2c/unbind
        sleep 1
        echo 1-0041 > /sys/bus/i2c/drivers/ili210x_i2c/bind 
        sleep 1
        test -e /dev/input/touchscreen0 || break
        echo "ok: $(CYCLES) - $(date)"
done 
