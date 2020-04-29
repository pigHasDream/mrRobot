#!/usr/bin/python3
import time
from module.dist import DistCL
from adafruit_motorkit import MotorKit
import random

kit = MotorKit()
kit.motor1.throttle = 0
kit.motor4.throttle = 0

initSpeed = 0.8
holdTime = 0.4
turnDist = 30

def getWheelDir(n) :
  if n == 1 :
    lsign, rsign = 1, 1
  elif n == 2 :
    lsign, rsign = 1, -1
  elif n == 3 :
    lsign, rsign = -1, 1
  elif n == 4 :
    lsign, rsign = -1, -1
  else :
    lsign, rsign = 0, 0

  return lsign, rsign


def stableMove(kit, nextDir, speed, holdTime) :
  print("Move stably...") 

  leftDir,rightDir = getWheelDir(nextDir)
  kit.motor1.throttle = speed * leftDir
  kit.motor4.throttle = speed * rightDir
  print(kit.motor1.throttle, kit.motor4.throttle)
  time.sleep(holdTime)

  return kit.motor1.throttle, kit.motor4.throttle


def goUntilHitLoop(kit) :

  distObj = DistCL()
  nextDir = 1

  try:
    while True :
      dist = distObj.getDist()

      if dist < turnDist :
        #nextDir = random.randint(2,3)
        nextDir = 2
        stableMove(kit, nextDir, initSpeed, holdTime)
        stableMove(kit, nextDir, 0, holdTime)

      stableMove(kit, 1, initSpeed, holdTime)

  except KeyboardInterrupt :
     stableMove(kit, nextDir, 0, holdTime/2)

if __name__ == "__main__" :
  input("To start hit anything")
  goUntilHitLoop(kit)

  
    
