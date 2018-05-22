#!/bin/bash

echo "Starting video.";
raspivid -t 21600000 -vs -w 1640 -h 1232 -fps 30 -b 15000000 -o flight.h264 &

echo "Entering sensor loop.";

COUNTER=14400
while [ $COUNTER -ge 0 ]
do
	python ozone_methane.py
	(( COUNTER-- ))
	sleep 1		# the amount of time we wait before taking a reading in seconds.
done

