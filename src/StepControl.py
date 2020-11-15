#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

JointValues = [0]*7

def StepControl():
	rospy.init_node('StepControl',anonymous = True)
	pub = rospy.Publisher('joint_states',JointState,queue_size=100)
	print('Nodo creado con Éxito')
	rate = rospy.Rate(10) #Frecuencia de publicaciÃ³n -> 10Hz
	grados = JointState()
	grados.position = [0]*6
	grados.name = ['Joint1', 'Joint2', 'Joint3', 'Joint4', 'Joint5', 'Joint6']
	i = 1
	while not rospy.is_shutdown():
		for i in range(0,6):
			grados.position[i] = float(input("J{}: ".format(i+1)))
		pub.publish(grados)
		rate.sleep()

if __name__ == '__main__':
	try:
		StepControl()
	except rospy.ROSInterruptException:
		pass
