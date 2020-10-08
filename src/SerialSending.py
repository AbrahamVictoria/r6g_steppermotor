#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray

import serial, time

PosNumber = 1

def SendData(name, target):
	arduino = serial.Serial('COM4', 115200)
	arduino.write(target.encode())
	print("{}: {}".format(name, target))
	while True:
		confirm = arduino.readline()
		if "OK" in confirm:
			break
		print(confirm)
		time.sleep(1)
	print("OK!")

def callback(data):
	target = ""
	for i in range(0,5):
		target += "\"J{}\": {},".format(i+1,data.data[i])
	target += "\"J{}\": {}".format(6,data.data[5])
	PosName = "Position {}".format(PosNumber)
	PosNumber += 1
	SendData(PosName,target)
	arduino.close()
    
def listener():
	rospy.init_node('SerialSending', anonymous=True)
	rospy.Subscriber("Targets", Float64MultiArray, callback)
	rospy.spin()

if __name__ == '__main__':
	SerialSending()

