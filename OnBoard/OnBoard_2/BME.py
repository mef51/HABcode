#!/usr/bin/python3
import Adafruit_BME280 as bme
import time, datetime


sensor = bme.BME280(t_mode=bme.BME280_OSAMPLE_8, 
					p_mode=bme.BME280_OSAMPLE_8, 
					h_mode=bme.BME280_OSAMPLE_8)
					
degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
kPa = pascals / 1000
humidity = sensor.read_humidity()

timestmp = ((str(datetime.datetime.utcnow())).split(' ')[1]).split('.')[0]

print('Temp      = {0:0.3f} C'.format(degrees))
print('Pressure  = {0:0.4f} kPa'.format(kPa))
print('Humidity  = {0:0.2f} %'.format(humidity))

# Write to csv
with open("bme.csv", "a") as output_file:
	cur_time = str(datetime.datetime.now()).split()
	output_file.write("%s,%s,%.3f,%.4f, %.2f\n" % (cur_time[0], cur_time[1], degrees, kPa, humidity))
	
