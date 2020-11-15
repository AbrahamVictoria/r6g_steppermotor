#! /usr/bin/env python3

import rospy
from r6g_steppermotor.msg import CurrentPose

JointValues = [0]*7

def StepControl():
	rospy.init_node('StepControl',anonymous = True)
	pub = rospy.Publisher('CurrentPose', CurrentPose, queue_size=100)
	print('Nodo creado con Éxito')
	rate = rospy.Rate(10) #Frecuencia de publicaciÃ³n -> 10Hz
	r6g = CurrentPose()
	r6g.position = [0]*6
	r6g.name = ['Joint1', 'Joint2', 'Joint3', 'Joint4', 'Joint5', 'Joint6']
	i = 1
	while not rospy.is_shutdown():
		for i in range(0,6):
			r6g.position[i] = float(input("J{}: ".format(i+1)))
		r6g.endEffector = int(input("Estado del efector final: "))
		pub.publish(r6g)
		rate.sleep()

if __name__ == '__main__':
	try:
		StepControl()
	except rospy.ROSInterruptException:
		pass
