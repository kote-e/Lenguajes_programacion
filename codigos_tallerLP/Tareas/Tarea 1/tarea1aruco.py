import cv2
import numpy as np
from arucos_ldp import calcular_centro


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250) #diccionario de aruco
parametros = cv2.aruco.DetectorParameters()


detector = cv2.aruco.ArucoDetector(aruco_dict, parametros) #detector de aruco, se le pasa el diccionario y los parametros

cap = cv2.VideoCapture(0) #abrimos la camara, 0 es la camara por defecto, si hay mas de una camara se puede cambiar el numero

if not cap.isOpened():
    print("No se pudo acceder a la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al recibir el cuadro de la cámara.")
        break

    esquinas, ids, rechazados = detector.detectMarkers(frame) #detectamos los marcadores de aruco en el cuadro de la camara
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, esquinas, ids)
        #salimos los ids de los marcadores detectados y sus esquinas, para cada marcador detectado, calculamos el centro y dibujamos el id en el centro del marcador

    cv2.imshow('Mi Camara', frame)
        

    # Presiona la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberamos el recurso de la cámara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()