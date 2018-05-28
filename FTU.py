#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, 0)

sleep(9000)
GPIO.output(37, 1)
sleep(600)
GPIO.output(37, 0)
