#!/usr/bin/python

from __future__ import print_function
from datetime import datetime
from pytz import timezone
import serial, io

tz = timezone('Canada/Eastern')

addr = '/dev/ttyUSB0'
baud = 9600
fname = 'GeigerCounter.txt'
fmode = 'a'

with serial.Serial(addr,9600) as pt, open(fname,fmode) as outf:
	spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
		encoding = 'ascii', errors = 'ignore', newline = '\r', line_buffering = False)
	spb.readline()
	while (1):
		outf.write('{0}, {1} \n'.format(datetime.now(tz), spb.readline().strip()))
		outf.flush()