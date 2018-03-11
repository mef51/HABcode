#!/usr/bin/python3

###
# Connect to the GPS and parse the messages, pulling out the info we want to transmit.
#
###
port = '/dev/ttyS0'
baud = 9600 # pulse rate of port

if __name__ == '__main__':
	ser = serial.Serial(port, baud)
	print(ser)
