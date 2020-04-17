#!/usr/bin/python3

from picamera import PiCamera
from time import sleep

timer = 20

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
sleep(timer)
camera.stop_preview()
