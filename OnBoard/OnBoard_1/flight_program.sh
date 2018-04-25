#!/bin/bash

echo "Starting video.";
raspivid -t 21600000 -vs -w 1640 -h 1232 -fps 30 -b 15000000 -o $(date +"%T")_flight.h264 &

python GeigerCounter.py &

echo "Entering sensor loop.";
while :
do

	## TODO: GPS SCRIPT THAT TERMINATES BASED ON COORDINATES
		## SCRIPT SHOULD SAVE THE COORDINATES + TRANSMIT THEM

	sleep 1		# the amount of time we wait before taking a reading in seconds.
done
