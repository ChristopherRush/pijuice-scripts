#!/usr/bin/python3
import json
import os
from pijuice import PiJuice # Import pijuice module

pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print(pijuice.status.GetChargeLevel()['data']) # Read PiJuice status.

charge_level = pijuice.status.GetChargeLevel()['data']

if charge_level <= 10:
        with open("/var/lib/pijuice/pijuice_config.JSON", "r+") as jsonFile:
        data = json.load(jsonFile)

        tmp = data["system_task"]["min_charge"]
        #print (tmp)
        data["system_task"]["min_charge"] = {"threshold": 10, "enabled": False}

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

os.system('sudo systemctl restart pijuice.service')
