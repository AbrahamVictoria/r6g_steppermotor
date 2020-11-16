#! /usr/bin/env python3

import csv
import numpy as np
import rospy
from sensor_msgs.msg import JointState

pathCSV = 'src/csvfiles/joints_values.csv'

def VerificarUltimoEstado(position):
	"""Verificar el último estado del robot en el archivo CSV para evitar sobreecribir datos"""
	actualPose = []
	with open(pathCSV, newline = '') as csvfile:
		verificador = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		for angulos in verificador:
			actualPose = angulos
		index = 0
		comparador = True
		for joint in actualPose:
			comparador = float(joint) == position[index] and comparador
			index += 1
	return comparador

def toCSV(data):
	"""Enviar ángulos a archivo CSV para su próxima lectura y envío mediante el puerto serial"""
	if not (VerificarUltimoEstado(data.position)):
		print("Escribiendo nueva pose para el robot en archivo CSV ... ")
		estado = ""
		rowValues = np.array([])
		for angulo in data.position:
			estado += "{}, ".format(angulo)
			rowValues = np.append(rowValues,'{}'.format(angulo))
		with open(pathCSV, 'a') as csvfile:
			writer = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
			writer.writerow(rowValues)
	

def trayectoria():
	rospy.init_node('Trayectoria', anonymous=True)
	rospy.Subscriber("joint_states", JointState, toCSV)
	rospy.spin()




if __name__ == '__main__':
	trayectoria()
