#! /usr/bin/env python3

import csv
import rospy
from r6g_steppermotor.msg import CurrentPose

pathCSV = 'src/csvfiles/joints_values.csv'

def readCSV():
	rospy.init_node('ReadCSV',anonymous = True)
	pub = rospy.Publisher('CurrentPose', CurrentPose, queue_size=100)
	print('Lector de CSV inicializado')
	rate = rospy.Rate(10) #Frecuencia de publicación
	r6g = CurrentPose()
	r6g.position = [0]*6
	r6g.name = ['Joint1', 'Joint2', 'Joint3', 'Joint4', 'Joint5', 'Joint6']
	comparador = False
	while not rospy.is_shutdown():
		comparador = False
		with open(pathCSV, newline = '') as csvfile:
			lector = csv.reader(csvfile, delimiter = ',', quotechar = '|')
			for pose in lector:
				actualPose = pose
		i = 0
		for joint in actualPose:
			joint = float(joint)
			if i < 5:
				if r6g.position[i] != joint:
					r6g.position[i] = joint
					comparador = True
				i += 1
		r6g.endEffector = int(0)
		if comparador:
			pub.publish(r6g)
			print("Publicando en Esp32 . . . ")
			rate.sleep()
		if comparador:
			with open(pathCSV, 'w') as csvfile:
				writer = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)

if __name__ == '__main__':
	try:
		readCSV()
	except rospy.ROSInterruptException:
		pass
