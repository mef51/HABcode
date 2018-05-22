#!/bin/bash

echo "Starting video.";
raspivid -t 21600000 -vs -w 1640 -h 1232 -fps 30 -b 15000000 -o $(date +"%T")_flight.h264 &

echo "Running parseBME.py"
./HABcode/PressTempHum/parseBME.py &

echo "Running UV.py"
./HABcode/UVSensor/uv.py &

echo "Entering sensor loop.";
while :
do
	./HABcode/ControlEverything_Methane_Ozone/ozone_methane.py &
	
	sleep 1		# the amount of time we wait before taking a reading in seconds.
done
