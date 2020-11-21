# Importando librería de cv2 y np.
from cv2 import cv2
import numpy as np

# Inicialización de captura de cámara.
captura = cv2.VideoCapture(0)

# Colocando un nuevo tipo de fuente.
font = cv2.FONT_ITALIC

# Definiendo parámetros de detección de colores.
def nothing(x):
   pass

# Construir las barras de seguimiento para colores HSV.
cv2.namedWindow('Parametros de Calibracion')
cv2.createTrackbar('Matiz Min','Parametros de Calibracion',0,179,nothing)
cv2.createTrackbar('Matiz Max','Parametros de Calibracion',0,179,nothing)
cv2.createTrackbar('Saturacion Min','Parametros de Calibracion',0,255,nothing)
cv2.createTrackbar('Saturation Max','Parametros de Calibracion',0,255,nothing)
cv2.createTrackbar('Brillo Min','Parametros de Calibracion',0,255,nothing)
cv2.createTrackbar('Brillo Max','Parametros de Calibracion',0,255,nothing)

# Establecer parámetros de las posiciones en las barras de seguimiento.
cv2.setTrackbarPos('Matiz Min','Parametros de Calibracion',75)
cv2.setTrackbarPos('Matiz Max','Parametros de Calibracion',116)
cv2.setTrackbarPos('Saturacion Min','Parametros de Calibracion',98)
cv2.setTrackbarPos('Saturation Max','Parametros de Calibracion',236)
cv2.setTrackbarPos('Brillo Min','Parametros de Calibracion',97)
cv2.setTrackbarPos('Brillo Max','Parametros de Calibracion',255)

# Creando una imagen con colores HSV.
vizualizar_color1 = np.zeros((100, 300, 3), np.uint8)
vizualizar_color2 = np.zeros((100, 300, 3), np.uint8)
vizualizar_color1 = cv2.cvtColor(vizualizar_color1, cv2.COLOR_BGR2HSV)
vizualizar_color2 = cv2.cvtColor(vizualizar_color2, cv2.COLOR_BGR2HSV)

# Condición de cámara encendida.
while True:    
    
    # Convertir el color de la imagen de la cámara, de RGB a HSV.
    ret, frame = captura.read()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Obtener las posiciones de las barras de seguimiento.
    hMin = cv2.getTrackbarPos('Matiz Min','Parametros de Calibracion')
    hMax = cv2.getTrackbarPos('Matiz Max','Parametros de Calibracion')
    sMin = cv2.getTrackbarPos('Saturacion Min','Parametros de Calibracion')
    sMax = cv2.getTrackbarPos('Saturation Max','Parametros de Calibracion')
    vMin = cv2.getTrackbarPos('Brillo Min','Parametros de Calibracion')
    vMax = cv2.getTrackbarPos('Brillo Max','Parametros de Calibracion')
    
    # Crear los arrays que definen el rango de colores:
    color_bajos=np.array([hMin,sMin,vMin])
    color_altos=np.array([hMax,sMax,vMax])

    # Crear un array auxiliar.
    array_aux = np.array([2])
    
    # Creación de  los colores.
    mask = cv2.inRange(frameHSV, color_bajos, color_altos)
    vizualizar_color1[:] = (hMin, sMin, vMin)
    vizualizar_color2[:] = (hMax, sMax, vMax)
    vizualizar_color = cv2.addWeighted(vizualizar_color1, 0.5, vizualizar_color2, 0.5, 0)
    vizualizar_color = cv2.cvtColor(vizualizar_color, cv2.COLOR_HSV2BGR)
    
    # Detección de los colores en la imagen y liminación de ruido.
    AND = cv2.bitwise_and(frame, frame, mask = mask)
    
    if np.any(mask):
    
        frameGRAY = cv2.cvtColor(AND, cv2.COLOR_BGR2GRAY)
        frameGRAY = cv2.GaussianBlur(frameGRAY, (7, 7), 3)
    
        t, dst = cv2.threshold(frameGRAY, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
        cntrs,_ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        
        # Detección de contornos de la imagen.
        for c in cntrs:
            epsilon = 0.01*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)

            x,y,w,h = cv2.boundingRect(approx)
            frameGRAY = cv2.drawContours(frameGRAY, [c], 0, (150, 150, 150), 1)     
        
        # Detección de las coordenadas.
        for i in range(len(cntrs)):
            momento = cv2.moments(frameGRAY)
            cx = int(momento['m10']/momento['m00'])
            cy = int(momento['m01']/momento['m00'])
            cv2.circle(frameGRAY,(cx, cy), 3, (20, 20, 150), -1)
            cv2.putText(frameGRAY, ' {},{}'.format(cx,cy), (cx,cy), font, 0.75, (150,150,150), 1, cv2.LINE_AA)
        

    # Mostrar las imágenes obtenidas.
    cv2.imshow('Vision', frame)
    cv2.imshow('Máscara_1', frameGRAY)
    cv2.imshow('Color', vizualizar_color)

    # Función para cerrar las ventanas que hayan sido abiertas.
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
cv2.destroyAllWindows()