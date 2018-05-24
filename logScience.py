#!/usr/bin/python3
"""
Log all science data to a single file. Format is csv:

time(est),altitude,lat,lng,temp,pressure,hum,O3_ppm,CH4_ppm,CO2_ppm,uv,geiger_cps,camera_check(maybe?)

"""
import csv
from datetime import datetime
import time

# try importing sensors
try:
	from PressTempHum import parseBME
except:
	print("failed BME import")
try:
	from ControlEverything_Methane_Ozone.Methane import ADC121C_MQ4
except:
	print("Failed Methane import")
try:
	from ControlEverything_Methane_Ozone.Ozone import ADC121C_MQ131
except:
	print("Failed Ozone import")
#try:
#	from CO2 import CO2
#except:
#	print("failed co2 import")
#try:
#	from UVSensor import uv
#except:
#	print("failed UV import")
try:
	from GeigerCounter import GeigerCounter
except:
	print("failed geiger import")
#try:
#	from GPS import parseGPS
#except:
#	print("failed gps import")

def getTimeAndDate():
	date = datetime.now()
	timestr = '{}:{}:{:02d}EDT'.format(date.hour, date.minute, date.second)
	datestr = '{}-{:02d}-{:02d}'.format(date.year, date.month, date.day)
	return (timestr, datestr)

if __name__ == '__main__':
	sampleTime = 1 # second
	logfile = 'flightlog_{}.csv'.format(getTimeAndDate()[1])
	fieldnames = ['time',
					'alt',
					'lat',
					'lng',
					'temp(C)',
					'press(kpa)',
					'hum(%)',
					'O3_ppm',
					'CH4_ppm',
					'CO2',
					'uv',
					'geiger']

	bufsize = 1 # write one line at a time
	with open(logfile, 'a', bufsize) as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		while True:
			row = {}
			sensorFailures = [False, False, False, False, False, False, False]
			sensors = ['GPS', 'BME', 'CH4', 'O3', 'CO2', 'UV', 'Geiger']

			# get time

			try:
				# get GPS
				alt, lat, lng = parseGPS.getGPSLogData()
				print(alt, lat, lng)
				row['alt'] = alt
				row['lat'] = lat
				row['lng'] = lng
				sensorFailures[0] = False
			except Exception:
				sensorFailures[0] = True

			try:
				# get BME data (pressure, temp, humidity)
				temp, press, humidity = parseBME.getData()
				row['temp(C)'] = '{0:0.3f}'.format(temp)
				row['press(kpa)'] = '{0:0.4f}'.format(press)
				row['hum(%)'] = '{0:0.2f}'.format(humidity)
				sensorFailures[1] = False
			except Exception:
				sensorFailures[1] = True

			try:
				# get CH4 data
				CH4 = ADC121C_MQ4.getMethaneData()
				row['CH4_ppm'] = '{:.2f}'.format(CH4)
				sensorFailures[2] = False
			except Exception:
				sensorFailures[2] = True

			try:
				# get O3 data
				O3  = ADC121C_MQ131.getOzoneData()
				row['O3_ppm']  = '{:.2f}'.format(O3)
				sensorFailures[3] = False
			except Exception:
				sensorFailures[3] = True

			try:
				# get CO2. Note getCO2Data() sleeps for 0.5 seconds
				CO2_ppm = CO2.getCO2Data()
				row['CO2'] = str(CO2_ppm)
				sensorFailures[4] = False
			except Exception:
				sensorFailures[4] = True

			try:
				# get UV
				uvdata = uv.getUVData()
				row['uv'] = str(uvdata)
				sensorFailures[5] = False
			except Exception:
				sensorFailures[5] = True

			try:
				# get geiger
				geigerdata = GeigerCounter.getGeigerData()
				row['geiger'] = geigerdata
				sensorFailures[6] = False
			except Exception:
				sensorFailures[6] = True

			timestr = getTimeAndDate()[0]
			row['time'] = timestr

			if True in sensorFailures:
				failedSensors = ''
				for sensor, status in zip(sensors, sensorFailures):
					if status:
						failedSensors += sensor + ' '
				print(timestr, 'failed data fetch:', failedSensors)

			writer.writerow(row)
			time.sleep(sampleTime)

