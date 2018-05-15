#!/usr/bin/python

import time
import os
import RPi.GPIO as GPIO
from datetime import datetime

now = datetime.now()

GPIO.setmode(GPIO.BCM)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)

        adcout >>= 1       # first bit is 'null' so drop it
        return adcout


try:
        uvLog = open("/home/pi/Desktop/UV-data.log","a")
        uvLog.write("\n=================================================\n")
        uvLog.write("  UV Data Log\n")
        uvLog.write("  Start time: ")
        uvLog.write(now.strftime("%d-%m-%Y %H:%M:%S"))
        uvLog.write("\n=================================================")
        uvLog.write("\n")
        uvLog.close()

        SPICLK = 26 #yellow
        SPIMISO = 19 #orange
        SPIMOSI = 13 #maroon
        SPICS = 6 #gray

        # set up the SPI interface pins
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)

        # uv sensor connected to adc #0
        uvSens_adc = 0;

        while True:
                # read the analog pin
                uv_value = readadc(uvSens_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
                localtime = time.asctime( time.localtime(time.time()) )

                uvLog = open("./UV-data.log","a")
                uvLog.write(localtime + ", "+ str(int(uv_value)) + "\n")
                uvLog.close()

                print uv_value

                time.sleep(1)


##cleanup pins on CTRL+C
except KeyboardInterrupt:
        GPIO.cleanup()
