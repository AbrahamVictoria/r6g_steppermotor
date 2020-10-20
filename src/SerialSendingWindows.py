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

def callback(data):
	target = "{"
	for i in range(0,5):
		target += "\"J{}\": {},".format(i+1,data[i])
	target += "\"J{}\": {}".format(6,data[5])
	target += "}"
	PosName = "Position"
	SendData(PosName,target)
	 


grados = [0]*7
while True:

	for i in range(0,6):
		grados[i] = int(input("J{}: ".format(i+1)))
	callback(grados)
