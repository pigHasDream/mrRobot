#!/usr/bin/python3
import time
from adafruit_motorkit import MotorKit

class MotorCL :
    def __init__(self) :
        self.kit = MotorKit()
        self.kit.motor1.throttle = 0
        self.kit.motor4.throttle = 0
        # max speed needs to be at most 1
        self.initSpeed = 0.5
        self.maxSpeed = 1
        self.incrSpeedStep = 0.2
        tranTime = 0.1
        holdTime = 1

    def getWheelDir(self, mode) :
      if mode == 1 :
        lsign, rsign = 1, 1
      elif mode == 2 :
        lsign, rsign = 1, -1
      elif mode == 3 :
        lsign, rsign = -1, 1
      elif mode == 4 :
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


def gearChange(kit, nextDir, minSpeed, incrSpeedStep, maxSpeed, tranTime, isAcc) :
  print("Speed up...") if isAcc else print("Slow down...")

  leftDir,rightDir = getWheelDir(nextDir)
  kit.motor1.throttle = minSpeed * leftDir
  kit.motor4.throttle = minSpeed * rightDir

  maxCount = int((maxSpeed - minSpeed) / incrSpeedStep) - 1

  for i in range(0, maxCount):
    leftDelta = incrSpeedStep * leftDir
    kit.motor1.throttle = kit.motor1.throttle + leftDelta if isAcc else kit.motor1.throttle - leftDelta
    rightDelta = incrSpeedStep * rightDir
    kit.motor4.throttle = kit.motor4.throttle + rightDelta if isAcc else kit.motor4.throttle - rightDelta
    time.sleep(tranTime)
    print(kit.motor1.throttle, kit.motor4.throttle)

  return kit.motor1.throttle, kit.motor4.throttle

def manCtrlLoop(kit, mode) :

  global initSpeed
  global incrSpeedStep
  global maxSpeed
  global tranTime
  global holdTime

  while True :
    nextDir = int(input("next?"))
    if nextDir == 0 :
      break
    elif nextDir == 99 :
      mode = str(input("reset play mode?"))
      continue

    if mode == "a" :
      gearChange(kit, nextDir, initSpeed, incrSpeedStep, maxSpeed, tranTime, True)
      gearChange(kit, nextDir, initSpeed, incrSpeedStep, maxSpeed, tranTime, False)
    elif mode == "c" :
      stableMove(kit, nextDir, initSpeed, holdTime)
      stableMove(kit, nextDir, 0, holdTime)
    else :
      print("ERROR mode, exiting...")
      break


if __name__ == "__main__" :
  mode = str(input("play mode?"))
  manCtrlLoop(kit, mode)

  
    
