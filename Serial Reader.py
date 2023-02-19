import serial
import time

print("================")
print("Serial Reader")
print("2023 EletrixTime")
print("Serial librairie version :")
print(serial.VERSION)
print("================")

com = input("COM port : ")
baudrate = input("Baudrate (default 9600) : ")
if baudrate == "":
    baudrate = 9600

ser = serial.Serial(com, baudrate)

while True:
    time.sleep(1)
    try:
        if ser.in_waiting > 0:
            read = ser.read(ser.in_waiting).decode()
            
            print(read)
    except serial.SerialException:
        print("ERROR : Connexion closed")
        ser.close()
        ser.open()
