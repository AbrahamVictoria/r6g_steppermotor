#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray

import serial, time

def SendData(name, target):
	arduino = serial.Serial('/dev/ttyUSB1', 115200)
	print('Puerto serial iniciado en /dev/ttyUSB1')
	arduino.write(target.encode())
	print("{}: {}".format(name, target))

	#nfirm = str(arduino.readline())
		#if 'OK' in confirm:
			#break
		#time.sleep(1)
	#print("OK!")
	arduino.close()

def callback(data):
	target = ""
	for i in range(0,5):
		target += "\"J{}\": {},".format(i+1,data.data[i])
	target += "\"J{}\": {}".format(6,data.data[5])
	PosName = "Position"
	SendData(PosName,target)
	 
def SerialSending():
	rospy.init_node('SerialSending', anonymous=True)
	rospy.Subscriber("Targets", Float64MultiArray, callback)
	print('Nodo creado con Éxito')
	rospy.spin()

if __name__ == '__main__':
	SerialSending()

