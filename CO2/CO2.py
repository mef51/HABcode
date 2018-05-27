#!/usr/bin/python

import serial
import time
ser = serial.Serial("/dev/ttyUSB1", baudrate = 9600, timeout = 1)
ser.flushInput()
time.sleep(1)

from datetime import datetime

def getCO2Data():
	ser.flushInput()
	ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
	time.sleep(.5)
	resp = ser.read(7)
	if resp != "":
		high = ord(resp[3])
		low = ord(resp[4])
		co2 = (high * 256) + low
		return co2
	else:
		return ''

if __name__ == '__main__':
	date = datetime.now()
	logfile = "CO2log_%04d-%02d-%02d.csv" % (date.year, date.month, date.day)
	with open (logfile, "a") as log:
		log.write('time,co2\n')
	while (1):
		ser.flushInput()
		string = '\xFE\x44\x00\x08\x02\x9F\x25'
		ser.write(string)
		time.sleep(.5)
		resp = ser.read(7)
		try:
			high = ord(resp[3])
			low = ord(resp[4])
			co2 = (high * 256) + low
			msg = "%s,%s\n" %(datetime.now(), co2)
			with open (logfile, "a") as log:
				log.write(msg)
				# print(" CO2 = " +str(co2))
		except:
			print("Please work")
		time.sleep(2)
