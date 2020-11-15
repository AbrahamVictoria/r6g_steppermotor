#! /usr/bin/env python3
import rospy
import math
from r6g_steppermotor.msg import CurrentPose

import serial, time

def SendData(name, target):
	"""Envío de datos por el puerto serial con estructura JSON"""
	if esp32.readable():
		esp32.write(target.encode())

def ToJSONFile(robot):
	"""Construcción del mensaje en formato JSON"""
	
	target = "{"
	estado = ""
	i = 0

	comparative = True

	for grado in robot.position:
		grado_Degrees = round(math.degrees(grado),4)
		comparative = grado_Degrees == valuesDoF[i] and comparative 
		valuesDoF[i] = grado_Degrees
		target += "\"J{}\": {},".format(i+1,grado_Degrees)
		estado += "J{}: {} ".format(i+1,grado_Degrees)
		i += 1
	target += "\"EF\": {}".format(robot.endEffector)
	estado += "EF: {}".format(robot.endEffector)
	target += "}"
	PosName = "Position"
	if not comparative:
		print(estado)
		SendData(PosName,target)

def SerialSending():
	"""Inicialización del nodo suscriptor"""
	rospy.init_node('SerialSending', anonymous=True)
	rospy.Subscriber("CurrentPose", CurrentPose, ToJSONFile)
	print('Nodo creado con Éxito')
	rospy.spin()

#Inicialización del puerto serie
port = '/dev/ttyUSB0'
#port = 'COM4'
esp32 = serial.Serial(port, 115200)
esp32.setDTR = False
print('Puerto serial iniciado en {}'.format(port))
valuesDoF = [0, -71, 75, 0, 0, 0]

if __name__ == '__main__':
	try:
		SerialSending()
	except rospy.ROSInterruptException:
		esp32.close()

