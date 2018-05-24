#!/usr/bin/python3

from __future__ import print_function
from datetime import datetime
from pytz import timezone
import serial, io

tz = timezone('Canada/Eastern')

addr = '/dev/ttyUSB0'
baud = 9600
fname = 'GeigerCounter.txt'
fmode = 'a'

def getGeigerData():
	"""
	Removes commas from the output of the counter to preserve the csv log
	"""
	with serial.Serial(addr,baudrate = 9600,  timeout = 1) as pt, open(fname,fmode) as outf:
		spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
			encoding = 'ascii', errors = 'ignore', newline = '\n', line_buffering = False)
		data = spb.readline().strip()
		data = data.replace(',', '')
		return data

if __name__ == '__main__':
	with serial.Serial(addr, baudrate = 9600, timeout = 1) as pt, open(fname,fmode) as outf:
		spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
			encoding = 'ascii', errors = 'ignore', newline = '\n', line_buffering = True)
		spb.readline()
		while (1):
			outf.write('{0}, {1} \n'.format(datetime.now(tz), spb.readline().strip()))
			outf.flush()
