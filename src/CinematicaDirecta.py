#!/usr/bin/env python3

from __future__ import print_function
from six.moves import input

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

import math

def CinematicaDirecta():
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('kinematics', anonymous=True)
	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	move_group = moveit_commander.MoveGroupCommander("r6g_um")
	joints = move_group.get_current_joint_values()
	print(joints)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		for i in range(0,len(joints)):
			joints[i] = math.radians(float(input("J{}: ".format(i+1))))
		move_group.go(joints, wait = True)
		print(move_group.get_current_pose())
		move_group.stop()
		rate.sleep()

if __name__ == '__main__':
	try:
		CinematicaDirecta()
	except rospy.ROSInterruptException:
		pass
