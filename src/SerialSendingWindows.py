import serial, time

def SendData(name, target):
	#port = '/dev/ttyUSB1'
	port = 'COM4'
	arduino = serial.Serial(port, 115200)
	print('Puerto serial iniciado en {}'.format(port))
	arduino.write(target.encode())
	print("{}: {}".format(name, target))
	while True:
		confirm = str(arduino.readline())
		if 'OK' in confirm: 
			break
		time.sleep(1)
	print("OK!")
	arduino.close()

def ToJSONMessage(data, EndEffector):
	target = "{"
	for i in range(0,6):
		target += "\"J{}\": {},".format(i+1,data[i])
	target += "\"EF\": {}".format(EndEffector)
	target += "}"
	PosName = "Position"
	SendData(PosName,target)
	 
grados = [0]*6
while True:
	for i in range(0,6):
		grados[i] = float(input("J{}: ".format(i+1)))
	EndEffectorStatus = int(input("Estado del efector final: "))
	print(type(EndEffectorStatus))
	ToJSONMessage(grados, EndEffectorStatus)