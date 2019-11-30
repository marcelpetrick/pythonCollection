# copied from https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/
from machine import Pin
from time import sleep

# this LED exists on every ESP8266
led = Pin(2, Pin.OUT)

# the "main"
while True:
    led.value(not led.value())
    sleep(0.05)  # discoooo! flashes with a frequency of 10 Hz (on-off-cycle takes 2*0.05s -> 10 Hz)
