#Created by Chris Rush @ Pi-Supply

#!/usr/bin/python3
import logging
import datetime
import time
from pijuice import PiJuice # Import pijuice module
pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object

while True:
        temp =  pijuice.status.GetBatteryTemperature()
        temp = temp['data'] if temp['error'] == 'NO_ERROR' else temp['error']
        vbat = pijuice.status.GetBatteryVoltage()
        vbat = vbat['data'] if vbat['error'] == 'NO_ERROR' else vbat['error']
        ibat = pijuice.status.GetBatteryCurrent()
        ibat = ibat['data'] if ibat['error'] == 'NO_ERROR' else ibat['error']
        vio =  pijuice.status.GetIoVoltage()
        vio = vio['data'] if vio['error'] == 'NO_ERROR' else vio['error']
        iio = pijuice.status.GetIoCurrent()
        iio = iio['data'] if iio['error'] == 'NO_ERROR' else iio['error']

        data = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),"T=", temp, "Vbat=", vbat, "Ibat=", ibat, "Vio=",vio," Iio$
        logging.basicConfig(filename='pijuice.log',level=logging.DEBUG)
        logging.debug(data)

        print (data)
        time.sleep(1)
