import serial
import time
import pywhatkit

serialMain = serial.Serial('COM3', 9600)
time.sleep(2)

serialData = []
for i in range(80):
    lineRead = serialMain.readline()

    if lineRead:
        decodedSerial = lineRead.decode()
        serialInt = int(float(decodedSerial))

        if (serialInt != 0):
            pywhatkit.sendwhatmsg("+919209388529", "FIRE DETECTED, IMMEDIATE ACTION NECESSARY. PLEASE GIVE ATTENTION\n\0", 19, 16)
            
        print(serialInt)


