#!/usr/bin/env python3
import time
import os

from pijuice import PiJuice
from enviroplus import gas
from bme280 import BME280
from smbus import SMBus
from cayennelpp import LppFrame
from rak811 import Mode, Rak811

pijuice = PiJuice(1, 0x14)
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
cmd = "sudo hwclock --hctosys"

def initialise():
    os.system(cmd)
    while not os.path.exists('/dev/i2c-1'):
        time.sleep(0.1)

    date = time.strftime("%H:%M %d/%m/%Y")

def setRTC():
    d_wake = dict()
    d_wake['year'] = 'EVERY_YEAR'
    d_wake['month'] = 'EVERY_MONTH'
    d_wake['day'] = 'EVERY_DAY'
    d_wake['hour'] = 'EVERY_HOUR'
    d_wake['minute'] = 0
    d_wake['second'] = 0

    status = pj.rtcAlarm.SetAlarm(d_wake)
    if status['error'] != 'NO_ERROR':
        print('Cannot set alarm\n')
        sys.exit()
    else:
        print('Alarm set for ' + str(pj.rtcAlarm.GetAlarm()))

    pj.rtcAlarm.SetWakeupEnabled(True)
    time.sleep(0.4)

def shutdown():
    # PiJuice shuts down power to Rpi after 20 sec from now
    # This leaves sufficient time to execute the shutdown sequence
    time.sleep(60)
    pj.power.SetPowerOff(20)
    subprocess.call(["sudo", "poweroff"])

def getData():
    raw_temp = bme280.get_temperature()
    humidity = bme280.get_humidity()
    pressure = bme280.get_pressure()
    gas = gas.read_all()
    charge_level = pijuice.status.GetChargeLevel()[data]
    #print(raw_temp)

def sendData():
    frame = LppFrame()
    frame.add_temperature(0, raw_temp)
    frame.add_humitidy(6, humidity)
    frame.add_pressure(1, pressure)

    buffer = frame.bytes()

    #print(buffer)

    lora = Rak811()
    lora.hard_reset()
    lora.mode = Mode.LoRaWan
    lora.band = 'EU868'
    lora.set_config(app_eui='70B3D57ED001C921',
                app_key='55B77F583763DCFE02AC75DB77CDD4B1')
    lora.join_otaa()
    lora.dr = 5
    lora.send(bytes(buffer))
    lora.close()

initialise()
#setRTC()
getData()
sendData()
#shutdown()
