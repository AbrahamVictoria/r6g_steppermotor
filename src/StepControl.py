#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

JointValues = [0]*7

def StepControl():
	rospy.init_node('StepControl',anonymous = True)
	pub = rospy.Publisher('Targets',JointState,queue_size=100)
	print('Nodo creado con Éxito')
	rate = rospy.Rate(10) #Frecuencia de publicaciÃ³n -> 10Hz
	grados = JointState()
	grados.position = [0]*7
	while not rospy.is_shutdown():
		for i in range(0,6):
			grados.position[i] = JointValues[i]
		pub.publish(grados)
		rate.sleep()

def callback(data):
	estado = ""
	for x in range(0,len(data.position)):
		JointValues[x] = data.position[x]
        estado += "J{}: {} ".format(j+1, data.position[j])
    print(estado)
    
def Joints_listener():
	rospy.init_node('Joints_listener', anonymous=True)
	rospy.Subscriber("joint_states", JointState, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		StepControl()
		Joints_listener()
	except rospy.ROSInterruptException:
		pass
