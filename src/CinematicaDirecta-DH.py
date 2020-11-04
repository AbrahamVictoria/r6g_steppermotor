#!/usr/bin/env python3
from sympy import *
import math
import numpy

def MatrizTransformacionHomogenea(theta, d, a, alpha):
    """Generación de matriz de tranformación homogénea para cada GDL"""
    alpha = math.radians(alpha)
    T = Matrix([[cos(theta), -cos(alpha)*sin(theta), sin(alpha)*sin(theta), a*cos(theta)],
            [sin(theta), cos(alpha)*cos(theta),  -sin(alpha)*cos(theta), a*sin(theta)],
            [0, sin(alpha), cos(alpha), d], [0,0,0,1]])
    return T

#Expresar ángulos de forma simbólica. 
q1 = Symbol("theta_1")
q2 = Symbol("theta_2")
q3 = Symbol("theta_3")
q4 = Symbol("theta_4")
q5 = Symbol("theta_5")
q6 = Symbol("theta_6")

#Tabla de parámetros de Denavit-Hartemberg.
#Recordar que <<theta>> es giro en Z, <<d>> es distancia en Z,
#<<a>> es distancia en X y <<alpha>> es giro en X. 

DHP = { #Robot original
    "theta1": q1, "d1": 132.5, "a1": 47,   "alpha1": -90,
    "theta2": q2, "d2": 0,   "a2": 110,    "alpha2": 0,
    "theta3": q3, "d3": 0.0,   "a3": 26.05,   "alpha3": -90,
    "theta4": q4, "d4": 116.5,   "a4": 0, "alpha4": 90,
    "theta5": q5, "d5": 0, "a5": 64,   "alpha5": -90,
    "theta6": q6, "d6": 0, "a6": 0,   "alpha6": 0
}

#Construir Matrices de Transformación Homogénea.
T1 = MatrizTransformacionHomogenea(DHP["theta1"], DHP["d1"], DHP["a1"], DHP["alpha1"])
T2 = MatrizTransformacionHomogenea(DHP["theta2"], DHP["d2"], DHP["a2"], DHP["alpha2"])
T3 = MatrizTransformacionHomogenea(DHP["theta3"], DHP["d3"], DHP["a3"], DHP["alpha3"])
T4 = MatrizTransformacionHomogenea(DHP["theta4"], DHP["d4"], DHP["a4"], DHP["alpha4"])
T5 = MatrizTransformacionHomogenea(DHP["theta5"], DHP["d5"], DHP["a5"], DHP["alpha5"])
T6 = MatrizTransformacionHomogenea(DHP["theta6"], DHP["d6"], DHP["a6"], DHP["alpha6"])

#Obtener matriz general. 
TCP = T1*T2*T3*T4*T5*T6

#Generar función de parámetros para grados de libertad. 
MTH_TCP = lambdify((q1,q2,q3,q4,q5,q6), TCP, "numpy")

if __name__ == "__main__":
    joints = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    for i in range(0,6):
        if i == 1:
            joints[i] = math.radians(float(input("J{}: ".format(i+1))) - 90)
        elif i == 4:
            joints[i] = math.radians(float(input("J{}: ".format(i+1))) + 90)
        else:
            joints[i] = math.radians(float(input("J{}: ".format(i+1))))
    print(joints)
    ValuesTCP = Matrix(MTH_TCP(joints[0], joints[1], joints[2], joints[3], joints[4], joints[5]))
    print("Valor en X: {}mm, Y: {}mm, Z: {}mm".format(round(ValuesTCP.col(-1)[0],8), round(ValuesTCP.col(-1)[1],8), round(ValuesTCP.col(-1)[2],8))) 