#! /usr/bin/env python3

import csv
import numpy as np
import rospy
from sensor_msgs.msg import JointState

"""
#data = [["J1", "J2", "J3"], ["0", "0", "0"], ["90", "90", "90"]]
data = [['J1', 'J2', 'J3'], ['0', '0', '0']]

with open('joints_values.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        #writer.writerow(['Spam'] * 5 + ['Baken Beans'])
        writer.writerows(data)
"""


def toCSV(data):
	estado = ""
	rowValues = np.array([])
	degrees = np.array(['J1','J2','J3','J4','J5','J6'])
	for angulo in data.position:
		estado += "{}, ".format(angulo)
		rowValues = np.append(rowValues,'{}'.format(angulo))
	degrees = np.vstack((degrees, rowValues))
	with open('csvfiles/joints_values.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
		#writer.writerow(['Spam'] * 5 + ['Baken Beans'])
		writer.writerows(degrees)

def trayectoria():
	rospy.init_node('Trayectoria', anonymous=True)
	rospy.Subscriber("joint_states", JointState, toCSV)
	rospy.spin()




if __name__ == '__main__':
	trayectoria()
