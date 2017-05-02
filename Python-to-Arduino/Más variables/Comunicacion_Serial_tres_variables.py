

import serial
import time
arduino=serial.Serial('/dev/ttyACM0',115200)
print("iniciamos")
time.sleep(2)
x=200
y=300
z=172

def mandarDatos(x,y,z):
	for i in range(0,2):
		envio=str(x)+","+str(y)+","+str(z) 	
		arduino.write(envio)	
		time.sleep(1.5)

mandarDatos(x,y,z)    	
arduino.close()
