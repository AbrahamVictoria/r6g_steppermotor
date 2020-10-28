#! /usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState

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
	for i in range(0,len(data.position)):
		dataJoint = data.position[i] 
		if dataJoint < 0.1:
			dataJoint = 0
		target += "\"J{}\": {},".format(i+1,dataJoint)
	target += "\"J{}\": {}".format(6,0)
	target += "}"
	PosName = "Position"
	print(target)
	SendData(PosName,target)
	 
def SerialSending():
	"""Inicialización del nodo suscriptor"""
	rospy.init_node('SerialSending', anonymous=True)
	rospy.Subscriber("/move_group/fake_controller_joint_states", JointState, callback)
	print('Nodo creado con Éxito')
	rospy.spin()

#Inicialización del puerto serie
port = '/dev/ttyUSB0'
#port = 'COM4'
arduino = serial.Serial(port, 115200)
arduino.setDTR = False
print('Puerto serial iniciado en {}'.format(port))

if __name__ == '__main__':
	try:
		SerialSending()
	except rospy.ROSInterruptException:
		arduino.close()

