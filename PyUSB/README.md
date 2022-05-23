# Powercycling script

* power outlet is `Energenie EG-PM2`
* python support with this lib?
  https://github.com/marcelpetrick/pysispm
* workflow: turn on socket (1), wait for boot, login via ssh, check if i2c appears: if yes, then reboot; else wait
