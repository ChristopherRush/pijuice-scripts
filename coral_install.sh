#!/bin/bash
sudo apt update -y
sudo apt upgrade -y

echo "deb https://packages.cloud.google.com/apt coral-cloud-stable main" | sudo tee /etc/apt/sources.list.d/coral-cloud.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt update -y

sudo apt install python3-coral-enviro -y

sudo sed -i "$ a dtparam=spi=on" /boot/config.txt
sudo sed -i "$ a dtparam=i2c_arm=on" /boot/config.txt

sudo reboot
