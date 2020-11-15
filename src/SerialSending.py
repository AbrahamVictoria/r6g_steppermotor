#! /usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import JointState

import serial, time



def SendData(name, target):
	"""Envío de datos por el puerto serial con estructura JSON"""
	if arduino.readable():
		arduino.write(target.encode())
	#print("{}: {}".format(name, target))
	"""
	while True:
		confirm = str(arduino.readline())
		#print(confirm)
		if 'OK' in confirm: 
			break
		time.sleep(1)
	print("OK!")
	"""

def callback(data):
	"""Construcción del mensaje en formato JSON"""
	
	target = "{"
	estado = ""
	i = 0

	comparative = True

	for grado in data.position:
		grado_Degrees = round(math.degrees(grado),4)
		comparative = grado_Degrees == valuesDoF[i] and comparative 
		valuesDoF[i] = grado_Degrees
		target += "\"J{}\": {},".format(i+1,grado_Degrees)
		estado += "J{}: {} ".format(i+1,grado_Degrees)
		i += 1
	#target += "\"J{}\": {}".format(6,0)
	EndEffector = int(input("Estado del efector final: "))
	target += "\"EF\": {}".format(EndEffector)
	target += "}"
	PosName = "Position"
	if not comparative:
		print(estado)
		SendData(PosName,target)

def SerialSending():
	"""Inicialización del nodo suscriptor"""
	rospy.init_node('SerialSending', anonymous=True)
	rospy.Subscriber("joint_states", JointState, callback)
	print('Nodo creado con Éxito')
	rospy.spin()

#Inicialización del puerto serie
port = '/dev/ttyUSB0'
#port = 'COM4'
arduino = serial.Serial(port, 115200)
arduino.setDTR = False
print('Puerto serial iniciado en {}'.format(port))
valuesDoF = [0, -71, 75, 0, 0, 0]

if __name__ == '__main__':
	try:
		SerialSending()
	except rospy.ROSInterruptException:
		arduino.close()

