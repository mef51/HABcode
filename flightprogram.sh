#!/bin/bash

echo "Starting video."
raspivid -t 21600000 -vs -w 1640 -h 1232 -fps 30 -b 15000000 -o $(date +"%T")_flight.h264 &

echo "Start GPS Transmitter"
./home/pi/Documents/HABcode/GPS/parseGPS.py &

echo "Starting FTU"
./FTU.py &
echo "Don't forget to restart countdown before launch"

echo "Starting CO2 sensor"
./home/pi/Documents/HABcode/CO2/CO2.py &

echo "Starting Science Log in 5 seconds..."
# sleep to allow us to see errors from the video, GPS, or FTU
sleep 5
echo "Science log started"
./logScience.py
