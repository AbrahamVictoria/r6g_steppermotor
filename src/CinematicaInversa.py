#!/usr/bin/env python3

from __future__ import print_function
from six.moves import input

import sys
import copy
import rospy
import moveit_commander
from moveit_msgs.msg import OrientationConstraint, Constraints, CollisionObject
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

from geometry_msgs.msg import PoseStamped

import math

def CinematicaInversa():
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('inverse_kinematics', anonymous=True)
	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	move_group = moveit_commander.MoveGroupCommander("r6g_um")
	move_group.set_planner_id("TRRT")
	move_group.set_planning_time(5)
	move_group.set_goal_position_tolerance(0.1)
	move_group.set_goal_orientation_tolerance(0.1)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		pose_target = PoseStamped()
		pose_target.header.frame_id = "Base"
		print("---- Posición ----")
		pose_target.pose.position.x = float(input("Valor en X: "))
		pose_target.pose.position.y = float(input("Valor en Y: "))
		pose_target.pose.position.z = float(input("Valor en Z: "))
		print("---- Orientación ----")
		pose_target.pose.orientation.x = float(input("Valor en R: "))
		pose_target.pose.orientation.y = float(input("Valor en P: "))
		pose_target.pose.orientation.z = float(input("Valor en Y: "))
		pose_target.pose.orientation.w = float(input("Valor en W: "))
		move_group.set_pose_target(pose_target)
		move_group.set_start_state_to_current_state()
		constraints = Constraints()
		constraints.orientation_constraints = []
		move_group.set_path_constraints(constraints)
		planeacion = move_group.plan()
		joints = move_group.get_current_joint_values()
		#rospy.sleep(5)
		#move_group.go(joints, wait = True)
		print(joints)
		move_group.stop()
		rate.sleep()

if __name__ == '__main__':
	try:
		CinematicaInversa()
	except rospy.ROSInterruptException:
		pass
