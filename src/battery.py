#!/usr/bin/python

# https://www.raspberrypiwiki.com/index.php/How_to_read_the_battery_capacity_via_I2C_on_X750%26725

import struct
import smbus
import sys
import time

def readVoltage(bus):
  address = 0x36
  read = bus.read_word_data(address, 2)
  swapped = struct.unpack("<H", struct.pack(">H", read))[0]
  voltage = swapped * 1.25 /1000/16
  return voltage


def readCapacity(bus):
  address = 0x36
  read = bus.read_word_data(address, 4)
  swapped = struct.unpack("<H", struct.pack(">H", read))[0]
  capacity = swapped/256
  return capacity


# 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
bus = smbus.SMBus(1) 

def getBatteryStat() :
  print "=================="

  print "Voltage:%5.2fV" % readVoltage(bus)
  print "Battery:%5i%%" % readCapacity(bus)

  if readCapacity(bus) == 100:
    print "Battery FULL"

  if readCapacity(bus) < 20:
    print "Battery LOW"

  print "=================="

if __name__ == "__main__" :
  getBatteryStat()
