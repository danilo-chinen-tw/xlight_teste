#!/bin/bash
sudo echo
sudo ./tftp.py &
./xdata.py
pkill tftp.py
