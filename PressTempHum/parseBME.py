#!/usr/bin/python3
import Adafruit_BME280 as bme
import time, datetime

sensor = bme.BME280(t_mode=bme.BME280_OSAMPLE_8,
					p_mode=bme.BME280_OSAMPLE_8,
					h_mode=bme.BME280_OSAMPLE_8)

def getData():
	try:
			temp = sensor.read_temperature()
			pascals = sensor.read_pressure()
			press = pascals / 1000
			humidity = sensor.read_humidity()
			return (temp, press, humidity)
	except Exception as e:
			print(e)

if __name__ == '__main__':
	sampleTime = 1 # seconds between samples
	while True:
		try:
			degrees = sensor.read_temperature()
			pascals = sensor.read_pressure()
			kPa = pascals / 1000
			humidity = sensor.read_humidity()

			timestmp = ((str(datetime.datetime.utcnow())).split(' ')[1]).split('.')[0]

			#print('Temp      = {0:0.3f} C'.format(degrees))
			#print('Pressure  = {0:0.4f} kPa'.format(kPa))
			#print('Humidity  = {0:0.2f} %'.format(humidity))
			print(timestmp, 'UTC', 'T: {0:0.3f} C'.format(degrees), 'P: {0:0.4f} kPa'.format(kPa), 'Hum {0:0.2f} %'.format(humidity))
		except Exception as e:
			print(e)
		time.sleep(sampleTime)

