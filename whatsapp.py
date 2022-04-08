# Various Modules are imported which are necessary for the project to function
import serial
import time
import pywhatkit

# A connection is established between the Arduino and the messaging system (In this case the laptop) through the Serial Port the Arduino is connected to
serialMain = serial.Serial('COM3', 9600)
time.sleep(2)

# Time values needed for the project is established
currentTime = time.localtime()

currentHour = currentTime.tm_hour
currentMinute = currentTime.tm_min

# The time when the message is to be sent is established, being 1 minute after the current time
extraTime = 1;
extraMinutes = currentMinute + extraTime

print(currentHour, currentMinute, extraMinutes)

# A function is run through which a message is sent after multiple
serialData = []
for i in range(80):
    # The value printed by the Serial Monitor is read by the Arduino
    lineRead = serialMain.readline()

    # The printed value is converted from a string (text) to an integer
    if lineRead:
        decodedSerial = lineRead.decode()
        serialInt = int(float(decodedSerial))

        if (serialInt != 0):
            # If the serialInt is not 0, meaning a fire is detected; a message is sent
            pywhatkit.sendwhatmsg("+917249355827", "FIRE DETECTED, IMMEDIATE ACTION NEEDED AT SECTION-3\n\0", currentHour, extraMinutes)
            
        print(serialInt)

