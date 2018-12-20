# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:10:13 2018

@author: Film
"""

# Original from William Henning
# http://www.mikronauts.com/raspberry-pi/raspberry-pi-4x4-keypad-i2c-MCP23017-howto/

import smbus
import time

class keypad_module:

  I2CADDR    = 0x20   	# valid range is 0x20 - 0x27

  PULUPA = 0x0F		# PullUp enable register base address
  PULUPB = 0xF0		# PullUp enable register base address
  
  # Keypad Keycode matrix
  KEYCODE  = [['1','4','7','*'], # KEYCOL0
              ['2','5','8','0'], # KEYCOL1
              ['3','6','9','#'], # KEYCOL2
              ['A','B','C','D']] # KEYCOL3

  # Decide the row
  DECODE = [0,0,0,0,0,0,0,3,0,0,0,2,0,1,0,0]

  # initialize I2C comm, 1 = rev2 Pi, 0 for Rev1 Pi
  i2c = smbus.SMBus(1) 

  # get a keystroke from the keypad
  def getch(self):
    while 1:
        time.sleep(0.01)
        self.i2c.write_byte(self.I2CADDR, self.PULUPA)
        row = self.i2c.read_byte(self.I2CADDR)
        if (row) != 0b1111:
            self.i2c.write_byte(self.I2CADDR, self.PULUPB)
            col = self.i2c.read_byte(self.I2CADDR) >> 4
            row = self.DECODE[row]
            col = self.DECODE[col]
            return self.KEYCODE[row][col]

  # initialize the keypad class
  def __init__(self,addr):
    self.I2CADDR = addr

# test code
def main(): 
  keypad = keypad_module(0x20)  
  while 1:
    ch = keypad.getch()
    print(ch)

    if ch == 'D':
      exit()

# don't runt test code if we are imported
if __name__ == '__main__':
  main()
