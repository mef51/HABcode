#!/bin/bash

echo "Starting video."
raspivid -t 21600000 -vs -w 1640 -h 1232 -fps 30 -b 15000000 -o $(date +"%T")_flight.h264 &

echo "Start GPS Transmitter"
./home/pi/Documents/HABcode/GPS/parseGPS.py &

echo "Starting FTU"
# ???

echo "Starting Science Log in 5 seconds..."
# sleep to allow us to see errors from the video, GPS, or FTU
sleep 5
echo "Science logged at " `ls *.csv`
./logScience.py
