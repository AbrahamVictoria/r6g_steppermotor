#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray

def StepControl():
	rospy.init_node('StepControl',anonymous = True)
	pub = rospy.Publisher('Targets',Float64MultiArray,queue_size=100)
	print('Nodo creado con Éxito')
	rate = rospy.Rate(10) #Frecuencia de publicaciÃ³n -> 10Hz
	grados = Float64MultiArray()
	grados.data = [0]*7
	while not rospy.is_shutdown():
		for i in range(0,6):
			grados.data[i] = int(input("J{}: ".format(i+1)))
		pub.publish(grados)
		rate.sleep()

if __name__ == '__main__':
	try:
		StepControl()
	except rospy.ROSInterruptException:
		pass
