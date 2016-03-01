import serial
ser = serial.Serial('/dev/ttyACM0',115200)
while True:
    str = ser.readline()
    print(str)
