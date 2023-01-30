import serial
import time

ser = serial.Serial('COM6', baudrate = 9600, timeout = 1) # change 'COM6' to the port that your device is connected to
start_time = time.time()
count = 0

while True:
    data = ser.read() # read a line of data and decode it
    print(data)
    '''
    data = ser.readline().decode() # read a line of data and decode it
    if data:
        count += 1
    current_time = time.time()
    if current_time - start_time >= 1:
        frequency = count / (current_time - start_time)
        print("Frequency: {:.2f} Hz".format(frequency))
        start_time = current_time
        count = 0
    '''
