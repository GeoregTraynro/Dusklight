#!/usr/bin env python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def light_level(pin):
	level = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.2)
	GPIO.setup(pin, GPIO.IN)
	while (GPIO.input(pin) == GPIO.LOW):
		level += 1
	return level

while True:
	print light_level(3)
        if light_level(3) > 60:
                GPIO.output(7 , True)
        else:
                GPIO.output(7 , False)
