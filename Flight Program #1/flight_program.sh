#!/bin/bash

echo "Starting video."
raspivid -t 21600000 -vs -w 1640 -h 1232 -fps 30 -b 15000000 -o $(date +"%T")_flight.h264 &

echo "Running  parseGPS.py"
./Documents/HABcode/GPS/parseGPS.py

echo "Running CO2 sensor"
./Documents/HABcode/CO2/CO2.py

echo "Running Geiger Counter"
./Documents/HABcode/Geiger\ Counter/GeigerCounter.py