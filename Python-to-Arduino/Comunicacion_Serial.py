


import serial
import time
arduino=serial.Serial('/dev/ttyACM0',115200)
print("iniciamos")
time.sleep(2)
coordenadaX=200
coordenadaY=300
while(True):
    	envio=str(coordenadaX)+","+str(coordenadaY) 	
	arduino.write(envio)	
	time.sleep(1.5)
arduino.close()
