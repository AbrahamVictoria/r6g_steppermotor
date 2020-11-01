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

def CinematicaInversa():
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('inverse_kinematics', anonymous=True)
	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	move_group = moveit_commander.MoveGroupCommander("r6g_um")
	move_group.set_planner_id("BFMT")
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		pose_target = geometry_msgs.msg.Pose()
		print("---- Posición ----")
		pose_target.position.x = float(input("Valor en X: "))
		pose_target.position.y = float(input("Valor en Y: "))
		pose_target.position.z = float(input("Valor en Z: "))
		print("---- Orientación ----")
		pose_target.orientation.x = float(input("Valor en R: "))
		pose_target.orientation.y = float(input("Valor en P: "))
		pose_target.orientation.z = float(input("Valor en Y: "))
		move_group.set_pose_target(pose_target)
		planeacion = move_group.plan()
		joints = move_group.get_current_joint_values()
		#rospy.sleep(5)
		#move_group.go(joints, wait = True)
		print(joints)
		#move_group.stop()
		rate.sleep()

if __name__ == '__main__':
	try:
		CinematicaInversa()
	except rospy.ROSInterruptException:
		pass
