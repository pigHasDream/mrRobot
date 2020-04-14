#!/usr/bin/python3
import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

kit.motor1.throttle = 0
kit.motor4.throttle = 0

maxSpeed = 20
initSpeed = 0.5
step = 0.01
interval = 0.01
lsign = -1
rsign = 1

nextAct = int(input("next?"))

def getNext(n) :
  global lsign 
  global rsign 

  if n == 1 :
    lsign = 1
    rsign = 1
  elif n == 2 :
    lsign = 1
    rsign = -1
  elif n == 3 :
    lsign = -1
    rsign = 1
  elif n == 4 :
    lsign = -1
    rsign = -1
  else :
    lsign = 1
    rsign = 1

getNext(nextAct)

while nextAct > 0:
  print("Forward!")
  kit.motor1.throttle = initSpeed * lsign
  kit.motor4.throttle = initSpeed * rsign
  time.sleep(1)

  print("Speed up...")
  for i in range(0, maxSpeed+1):
    speed = i * step
    kit.motor1.throttle = speed * lsign
    kit.motor4.throttle = speed * rsign
    time.sleep(interval)

  print("Slow down...")
  for i in range(maxSpeed, -1, -1):
    speed = i * step
    kit.motor1.throttle = speed * lsign
    kit.motor4.throttle = speed * rsign
    time.sleep(interval)

  print("Stop!")
  kit.motor1.throttle = 0
  kit.motor4.throttle = 0
  time.sleep(1)

  nextAct = int(input("next?"))
  getNext(nextAct)
  
    
