
import rospy
from std_msgs.msg import Float64MultiArray

import serial, time

def SendData(name, target):
	"""Envío de datos por el puerto serial con estructura JSON"""
	arduino.write(target.encode())
	print("{}: {}".format(name, target))
	while True:
		confirm = str(arduino.readline())
		print(confirm)
		if 'OK' in confirm: 
			break
		time.sleep(1)
	print("OK!")

def callback(data):
	"""Construcción del mensaje en formato JSON"""
	target = "{"
	for i in range(0,5):
		target += "\"J{}\": {},".format(i+1,data[i])
	target += "\"J{}\": {}".format(6,data[5])
	target += "}"
	PosName = "Position"
	print(target)
	SendData(PosName,target)
	 
def SerialSending():
	"""Inicialización del nodo suscriptor"""
	rospy.init_node('SerialSending', anonymous=True)
	rospy.Subscriber("Targets", Float64MultiArray, callback)
	print('Nodo creado con Éxito')
	rospy.spin()

#Inicialización del puerto serie
port = '/dev/ttyUSB1'
#port = 'COM4'
arduino = serial.Serial(port, 115200)
arduino.setDTR = False
print('Puerto serial iniciado en {}'.format(port))

if __name__ == '__main__':
	try:
	SerialSending()
	except rospy.ROSInterruptException:
		arduino.close()

