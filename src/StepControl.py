#! /usr/bin/env python3

import rospy
from r6g_steppermotor.msg import Step_Signals

def StepControl():
	pub = rospy.Publisher('Channel',Step_Signals,queue_size=100)
	rospy.init_node('StepControl',anonymous = True)
	print('Nodo creado con Éxito')
	rate = rospy.Rate(10) #Frecuencia de publicaciÃ³n -> 10Hz
	while not rospy.is_shutdown():
		pasos = int(input("Número de pulsaciones: "))
		pub.publish(pasos)
		print(pasos)
		rate.sleep()

if __name__ == '__main__':
	try:
		StepControl()
	except rospy.ROSInterruptException:
		pass
