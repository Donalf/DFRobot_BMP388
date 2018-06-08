# Connect bmp388 and esp32 via I2C/SPI.
#
# Warning:
#   This demo only supports python3.
#   Run this demo: python3 ReadForINT.py.
#
# connect: 
#   raspberry       bmp388
#   13              INT
#(I2C)
#   3.3v(1)         VCC
#   GND(6)          GND
#   SCL(5)          SCL
#   SDA(3)          SDA
#
#(SPI)
#   raspberry       bmp388
#   CS  (15)        CSB
#   3.3v(17)        VCC
#   MOSI(19)        SDI
#   MISO(21)        SDO
#   SCLK(23)        SCK
#   GND (25)        GND
# 
import bmp388
import time

# If 1, connect BMP388 to SPI interface of esp32, else connect I2C interface
if 0:
  # Create a bmp388 object to communicate with I2C.
  bmp388 = bmp388.DFRobot_BMP388_I2C()
  
else:
  # Define chip selection pins
  cs = 22

  # Create a bmp388 object to communicate with SPI.
  bmp388 = bmp388.DFRobot_BMP388_SPI(cs)

INT = 27 
# Read pressure and print it.
while 1:
  if(bmp388.INTReadPin(INT)):
    temp = bmp388.readTemperature()
    print("Temperature : %s C" %temp)
    pres = bmp388.readPressure()
    print("Pressure : %s Pa" %pres)
  time.sleep(0.5)