#!/usr/bin/env python3
   
import rospy
from sensor_msgs.msg import JointState

def callback(data):
    estado = ""
    for j in range(0,len(data.position)):
        estado += "J{}: {} ".format(j+1, data.position[j])
    print(estado)
    
def Joints_listener():
	rospy.init_node('Joints_listener', anonymous=True)
    rate = rospy.Rate(2)
	rospy.Subscriber("/move_group/fake_controller_joint_states", JointState, callback)
	rospy.spin()

if __name__ == '__main__':
	Joints_listener()