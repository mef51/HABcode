#!/usr/bin/python

import serial
import time
ser = serial.Serial("/dev/ttyUSB1", baudrate = 9600, timeout = 1)
ser.flushInput()
time.sleep(1)

from datetime import datetime

while (1):
	ser.flushInput()
	ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
	time.sleep(.5)
	resp = ser.read(7)
	if resp != "":
		high = ord(resp[3])
		low = ord(resp[4])
		co2 = (high * 256) + low
		msg = "%s, %s \n" %(datetime.now(), co2)
		with open ("/home/pi/Desktop/CO2log.txt", "a") as log:
			log.write(msg)
		print " CO2 = " +str(co2)
	time.sleep(1)
