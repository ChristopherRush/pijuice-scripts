#!/usr/bin/python
import json
import os

with open("/var/lib/pijuice/pijuice_config.JSON", "r+") as jsonFile:
    data = json.load(jsonFile)

    tmp = data["system_task"]["min_charge"]
    print (tmp)
    data["system_task"]["min_charge"] = {"threshold": 10, "enabled": True}

    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile)
    jsonFile.truncate()
os.system('sudo systemctl restart pijuice.service')
