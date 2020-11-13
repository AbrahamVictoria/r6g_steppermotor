from cv2 import cv2
import numpy as np

print("Configurando variables...")
# Configuración de detección de color.
font = cv2.FONT_ITALIC

def nothing(x):
   pass

cv2.namedWindow('ParametrosCalibracion')
cv2.createTrackbar('Hue Minimo','ParametrosCalibracion',0,179,nothing)
cv2.createTrackbar('Hue Maximo','ParametrosCalibracion',0,179,nothing)
cv2.createTrackbar('Saturation Minimo','ParametrosCalibracion',0,255,nothing)
cv2.createTrackbar('Saturation Maximo','ParametrosCalibracion',0,255,nothing)
cv2.createTrackbar('Value Minimo','ParametrosCalibracion',0,255,nothing)
cv2.createTrackbar('Value Maximo','ParametrosCalibracion',0,255,nothing)
cv2.createTrackbar('Kernel X', 'ParametrosCalibracion', 1, 30, nothing)
cv2.createTrackbar('Kernel Y', 'ParametrosCalibracion', 1, 30, nothing)

cv2.setTrackbarPos('Hue Minimo','ParametrosCalibracion',75)
cv2.setTrackbarPos('Hue Maximo','ParametrosCalibracion',116)
cv2.setTrackbarPos('Saturation Minimo','ParametrosCalibracion',98)
cv2.setTrackbarPos('Saturation Maximo','ParametrosCalibracion',236)
cv2.setTrackbarPos('Value Minimo','ParametrosCalibracion',97)
cv2.setTrackbarPos('Value Maximo','ParametrosCalibracion',255)
cv2.setTrackbarPos('Kernel X','ParametrosCalibracion',30)
cv2.setTrackbarPos('Kernel Y','ParametrosCalibracion',30)


# Bucle de detección de objetos.
print("Detección activada")

# Inicialización de captura de cámara.
captura = cv2.VideoCapture(0)

while(captura.isOpened()):    
    ret, frame = captura.read()
    #frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hMin = cv2.getTrackbarPos('Hue Minimo','ParametrosCalibracion')
    hMax = cv2.getTrackbarPos('Hue Maximo','ParametrosCalibracion')
    sMin = cv2.getTrackbarPos('Saturation Minimo','ParametrosCalibracion')
    sMax = cv2.getTrackbarPos('Saturation Maximo','ParametrosCalibracion')
    vMin = cv2.getTrackbarPos('Value Minimo','ParametrosCalibracion')
    vMax = cv2.getTrackbarPos('Value Maximo','ParametrosCalibracion')
    
    #Creamos los arrays que definen el rango de colores:
    color_bajos=np.array([hMin,sMin,vMin])
    color_altos=np.array([hMax,sMax,vMax])

    #Leemos los sliders que indican las dimensiones del Kernel:
    kernelx = cv2.getTrackbarPos('Kernel X', 'ParametrosCalibracion')
    kernely = cv2.getTrackbarPos('Kernel Y', 'ParametrosCalibracion')

    #Creamos el kernel:
    kernel = np.ones((kernelx,kernely),np.uint8)

    #Detectamos los colores y eliminamos el ruido:
    mask = cv2.inRange(hsv, color_bajos, color_altos)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    momentsAzul = cv2.moments(mask)



    areaAzul = momentsAzul['m00']
    if (areaAzul == 0): areaAzul = 1
    Y = int(momentsAzul['m10']/areaAzul)
    X = int(momentsAzul['m01']/areaAzul)
    cv2.circle(frame,(X,Y),7,(0,255,0),-1)
    cv2.putText(frame,'{},{}'.format(X,Y),(X,Y),font, 0.75, (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow('Vision', frame)
    cv2.imshow('Máscara', mask)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
cv2.destroyAllWindows()