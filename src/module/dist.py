#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

class DistCL : 
    def __init__(self) :
        GPIO.setmode(GPIO.BOARD)

        self.PIN_TRIGGER = 29
        self.PIN_ECHO = 31
        self.cmPerSec = 17150

        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

    def getDist(self) :
        print("Waiting for sensor to settle")
        time.sleep(0.01)

        print("Calculating distance")
        GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(self.PIN_ECHO) == 0 :
            pulse_start_time = time.time()
        while GPIO.input(self.PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * self.cmPerSec, 2)
        print(distance)

        return distance

if __name__ == "__main__" :
    distObj = DistCL()

    for _ in range(6) :
        time.sleep(2)
        distObj.getDist()

    GPIO.cleanup()
  



