import sys
import serial
import time
#
# This script displays Arduino data received on the Serial port /dev/ttyACM0
# If a parameter is added on the command line, it is interpreted as the
# sensor to display on the Arduino Hub's LED display, and passes this on to
# the Arduino to get that done.
#
print("To specify the sensor to display, add script parameter, eg 1 for sensor 1")
#
# open the port
#
ser = serial.Serial('/dev/ttyACM0',115200)
#
# must wait a short time before issuing commands
# 
time.sleep(.25)
#
# flush old input that may be left over from previous session(s)
#
ser.flushInput()
#
# wait (max 3 cycles) for Hub report of SPI status before beginning to log data
# whether or not it is made
#
i = 0
rline = ser.readline()
while rline[0:3] != b"SPI" and i < 3:
	rline = ser.readline()
	i = i + 1
	time.sleep(1)
#
# specify sensor to display in the Arduino Hub's LED display, if requested
#
if len(sys.argv) > 1:
	ledBarSelect = sys.argv[1]
	ser.write(str.encode(ledBarSelect[0]))	
else:
	ledBarSelect = '<default>'
i = 0
#
# report the data; peridically reconfirm sensor # whose value is displayed on 
# Arduino Hub LED bar. 
#
while True:
	if i%10 == 0:
		print("LED bar displays sensor #", ledBarSelect)
	rline = ser.readline(); print(rline)
	i = i+1
		
