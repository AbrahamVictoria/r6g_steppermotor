#!/usr/bin/env python3
   
import rospy
from r6g_steppermotor.msg import Step_Signals

def callback(data):
	print("I heard: " + str(data.steps1))
    
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("Channel", Step_Signals, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()

