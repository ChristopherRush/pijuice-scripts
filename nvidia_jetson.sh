#!/bin/bash

sudo apt update
sudo apt install -y python3-smbus python3-pip python3-stdeb dh-systemd debhelper fakeroot python3-all
sudo pip3 install stem stdeb3

sudo git clone https://github.com/PiSupply/PiJuice.git

cd $HOME/PiJuice/Software/Source/Setuid-Wrapper
sudo ./build-setuid-progs.sh
sudo cp p* $HOME/PiJuice/Software/Source/bin

cd $HOME/PiJuice/Software/Source/
sudo ./pckg-pijuice.sh

sudo cp $HOME/PiJuice/Software/Source/deb_dist_base/pi*.deb $HOME
sudo cp $HOME/PiJuice/Software/Source/deb_dist_gui/pi*.deb $HOME

sudo rm -rf PiJuice

sudo apt install -y python3-urwid lua5.3
