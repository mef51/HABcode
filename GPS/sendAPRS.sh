#!/bin/bash

echo "Enabling audio"
sudo modprobe snd-bcm2835

echo "Redirecting audio to GPIO pins"
gpio mode 1 alt 5

echo "Setting audio volume"
amixer set PCM -- 400

echo "Preparing transmitter PTT"
gpio mode 4 out
gpio write 4 0

if [ -e packet.wav ]; then
	echo Activating transmitter PTT
	gpio write 4 1

	echo Playing audio
	aplay packet.wav

	echo Done playing audio. Removing packet and turning of transmitter
	rm packet.wav
	gpio write 4 0
fi
	

