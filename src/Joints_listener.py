#!/usr/bin/env python3
   
import rospy
import math
from sensor_msgs.msg import JointState

grados = JointState()
grados.position = [0]*7

pub = rospy.Publisher('Targets',JointState,queue_size=100)

def callback(data):
    estado = ""
    for j in range(0,len(data.position)):
        grados.position[j] = data.position[j]
        estado += "J{}: {} ".format(j+1, math.degrees(data.position[j]))
    print(estado)
    
def Joints_listener():
	rospy.init_node('Joints_listener', anonymous=True)
	rospy.Subscriber("joint_states", JointState, callback)
	pub.publish(grados)
	rospy.spin()

if __name__ == '__main__':
	Joints_listener()







    
