


import serial
import time
from PIL import Image
arduino=serial.Serial('/dev/ttyACM0',9600)
print("iniciamos")
try:
	imagen = Image.open("m.jpg")
	imagen.show()
except:
    print("No ha sido posible cargar la imagen")
    
time.sleep(2)
while(True):
	time.sleep(1)
	var = arduino.readline()
	time.sleep(1)
	sonido=var.split(",")[0]
	temperatura=var.split(",")[3]
	print "sonido:"+sonido
	print "temperatura:"+temperatura
	#for x in range(0,4):
		#variable = var.split(",")[x]
		#print str(x)+":"+variable
	#print "NUEVO:"
	
	
	if int(sonido)==1:
		print "ALERTA SONIDO";
	elif int(temperatura) > 300:
		print "ALERTA TEMPERATURA"
	else:
		print "TODO BIEN "
arduino.close()
