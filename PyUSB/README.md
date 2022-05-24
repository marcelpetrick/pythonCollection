# Powercycling script

* power outlet is `Energenie EG-PM2` (see: https://energenie.com/item.aspx?id=7556&lang=de)
* python support with this lib?
  https://github.com/marcelpetrick/pysispm
* workflow: turn on socket (1), wait for boot, login via ssh, check if i2c appears: if yes, then reboot; else wait


* requirements:
```
> pip install pyusb
Defaulting to user installation because normal site-packages is not writeable
Collecting pyusb
  Downloading pyusb-1.2.1-py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 2.7 MB/s
Installing collected packages: pyusb
Successfully installed pyusb-1.2.1
WARNING: You are using pip version 20.2.1; however, version 22.1.1 is available.
You should consider upgrading via the 'c:\program files\python38\python.exe -m pip install --upgrade pip' command.
PS C:\Users\MarcelP\Desktop\MarcelsFolder\coding\pythonCollection\yoctoLicensePrep> 

```

as well:
> pip install pysispm

https://github.com/marcelpetrick/pysispm/blob/master/examples/printenv.py

as well: pyserial!


Check for devices:
lsusb

Bus 001 Device 003: ID 04b4:fd15 Cypress Semiconductor Corp. Energenie EG-PMS2
----------------

ps@ps-kub:~/Documents/pythonCollection/PyUSB$ sudo python3 powerCycle.py 
sispm.getid(d): 01:01:60:d0:e9
found device with fitting id
line 44: end of powerCycle()
ps@ps-kub:~/Documents/pythonCollection/PyUSB$ 

----------------

Question: what is the tty-device?

-------------

see: https://github.com/xypron/pysispm/blob/master/examples/sispmctl.py
```
ps@ps-kub:~/Documents/pythonCollection/PyUSB$ sudo ./sispmctl.py -o 1
device 0, 01:01:60:d0:e9
        status[1] = 1
        status[2] = 0
        status[3] = 0
        status[4] = 0
ps@ps-kub:~/Documents/pythonCollection/PyUSB$ 
```


----------------
Output looks like this:

```
$ sudo ./powerCycle.sh --cont
* turn off before first cycle *
device 0, 01:01:60:d0:e9
        status[1] = 0
        status[2] = 0
        status[3] = 0
        status[4] = 0
---------- run 1 / 0 freezes yet / Di 24. Mai 14:18:16 CEST 2022 / continuous=false ----------
* turn on *
device 0, 01:01:60:d0:e9
        status[1] = 1
        status[2] = 0
        status[3] = 0
        status[4] = 0
^C
ps@ps-kub:~/Documents/pythonCollection/PyUSB$ sudo ./powerCycle.sh -cont
continuous mode enabled!
* turn off before first cycle *
device 0, 01:01:60:d0:e9
        status[1] = 0
        status[2] = 0
        status[3] = 0
        status[4] = 0
---------- run 1 / 0 freezes yet / Di 24. Mai 14:18:20 CEST 2022 / continuous=true ----------
* turn on *
device 0, 01:01:60:d0:e9
        status[1] = 1
        status[2] = 0
        status[3] = 0
        status[4] = 0
* ssh now *
SSHRESULT=0600.0000.b7cc.aa0a
10.25.0d.00.01
03.04
5a.80:AP
found version; driver works
* turn off *
device 0, 01:01:60:d0:e9
        status[1] = 0
        status[2] = 0
        status[3] = 0
        status[4] = 0
* wait one more second *
---------- run 2 / 0 freezes yet / Di 24. Mai 14:18:42 CEST 2022 / continuous=true ----------
* turn on *
device 0, 01:01:60:d0:e9
        status[1] = 1
        status[2] = 0
        status[3] = 0
        status[4] = 0
* ssh now *
SSHRESULT=0600.0000.b7cc.aa0a
10.25.0d.00.01
03.04
5a.80:AP
found version; driver works
* turn off *
device 0, 01:01:60:d0:e9
        status[1] = 0
        status[2] = 0
        status[3] = 0
        status[4] = 0
* wait one more second *
---------- run 3 / 0 freezes yet / Di 24. Mai 14:19:05 CEST 2022 / continuous=true ----------
* turn on *
device 0, 01:01:60:d0:e9
        status[1] = 1
        status[2] = 0
        status[3] = 0
        status[4] = 0

```
