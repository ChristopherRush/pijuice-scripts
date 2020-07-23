#!/usr/bin/python3
import os
from gpiozero import LED
from time import sleep

from pijuice import PiJuice

red_pin = LED(18)
yellow_pin = LED(22)
green_pin = LED(24)

pijuice = PiJuice(1, 0x14)

while True:
    #print(pijuice.status.GetChargeLevel()['data'])
    charge_level = pijuice.status.GetChargeLevel()['data']
    if charge_level <= 25:
        red_pin.on()
        yellow_pin.off()
        green_pin.off()
    elif charge_level > 25 and charge_level <= 75:
        red_pin.off()
        yellow_pin.on()
        green_pin.off()
    else:
        red_pin.off()
        yellow_pin.off()
        green_pin.on()
    sleep(30)
