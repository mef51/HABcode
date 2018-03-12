#!/usr/bin/python3

###
# Connect to the GPS and parse the messages, pulling out the info we want to transmit.
#
###
import serial
import pynmea2
port = '/dev/ttyS0'
baud = 9600 # pulse rate of port

def handleGPSmsg(GGAmsg, RMCmsg):
	"""
	GGAmsg is a pynmea2 parsed GGA string (http://www.gpsinformation.org/dale/nmea.htm#GGA)
	To see what fields are available see the pynmea2 docs (https://github.com/Knio/pynmea2)
	
	To get latitude in degrees for example you can do msg.latitude
	"""
	speed = RMCmsg.spd_over_grnd # speed in knots
	speed *= 0.514444 # speed in meters/sec
	
	msg = GGAmsg
	altitude = msg.altitude
	time = msg.timestamp
	
	longitude = '%02d°%02d′%07.4f″' % (msg.longitude, msg.longitude_minutes, msg.longitude_seconds)
	latitude = '%02d°%02d′%07.4f″' % (msg.latitude, msg.latitude_minutes, msg.latitude_seconds)
	
	print(str(time)+" UTC:", latitude, longitude, 'alt:', altitude, 'meters spd:', '{:.3f}'.format(speed), "m/s")
	

if __name__ == '__main__':
	ser = serial.Serial(port, baud)
	GGAmsg = None # location info
	RMCmsg = None # speed info
	try:
		while True:
			line = ser.readline()
			line = line.strip()
			line = line.decode('utf-8')
			try:
				msg = pynmea2.parse(line, check=False)
				if isinstance(msg, pynmea2.types.talker.GGA):
					GGAmsg = msg
				elif isinstance(msg, pynmea2.types.talker.RMC):
					RMCmsg = msg
			except pynmea2.nmea.ChecksumError:
				print('ignoring checksum error')
			except pynmea2.nmea.ParseError:
				print('ignoring parse error')
				
			if GGAmsg and RMCmsg:
				handleGPSmsg(GGAmsg, RMCmsg)
				GGAmsg = None; RMCmsg = None
			
	finally:
		ser.close()
