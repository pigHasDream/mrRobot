#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

try :
  GPIO.setmode(GPIO.BOARD)

  PIN_TRIGGER = 29
  PIN_ECHO = 31
  cmPerSec = 17150

  GPIO.setup(PIN_TRIGGER, GPIO.OUT)
  GPIO.setup(PIN_ECHO, GPIO.IN)

  GPIO.output(PIN_TRIGGER, GPIO.LOW)

  print("Waiting for sensor to settle")

  time.sleep(0.01)

  print("Calculating distance")

  GPIO.output(PIN_TRIGGER, GPIO.HIGH)

  time.sleep(0.00001)

  GPIO.output(PIN_TRIGGER, GPIO.LOW)

  while GPIO.input(PIN_ECHO)==0:
     pulse_start_time = time.time()
  while GPIO.input(PIN_ECHO)==1:
     pulse_end_time = time.time()

  pulse_duration = pulse_end_time - pulse_start_time
  distance = round(pulse_duration * cmPerSec, 2)

  print(distance)

finally:
  GPIO.cleanup()
