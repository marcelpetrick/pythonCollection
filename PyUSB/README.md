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

