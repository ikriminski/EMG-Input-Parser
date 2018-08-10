import serial

with serial.Serial('COM4', 9600) as ser:
    while True:
        last_line = ser.readline()
        print(last_line.split(':')[:-1])
