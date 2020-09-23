#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int64MultiArray

def StepControl():
	rospy.init_node('StepControl',anonymous = True)
	pub = rospy.Publisher('Channel',Int64MultiArray,queue_size=100)
	print('Nodo creado con Éxito')
	rate = rospy.Rate(10) #Frecuencia de publicaciÃ³n -> 10Hz
	grados = Int64MultiArray()
	grados.data = [0]*7
	while not rospy.is_shutdown():
		grados.data[0] = int(input("Número de pulsaciones: "))
		pub.publish(grados)
		print(grados.data[0], grados)
		rate.sleep()

if __name__ == '__main__':
	try:
		StepControl()
	except rospy.ROSInterruptException:
		pass
