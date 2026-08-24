import cv2
import numpy as np

def calcular_centro(esquinas):
    # Calcula el centro del marcador de ArUco a partir de sus esquinas
    xc = int(np.mean(esquinas[:, 0]))
    yc = int(np.mean(esquinas[:, 1]))
    return (xc, yc)


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
        print("Error con la cámara.")
        break

    esquinas, ids, rechazados = detector.detectMarkers(frame) #detecta los marcadores de aruco en el cuadro de la camara
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, esquinas, ids)

        centros = {}
        for i in range(len(ids)):
            #print(f"ID del marcador: {ids[i]}")
            lista_numeros = ids.flatten().tolist()
            centro = calcular_centro(esquinas[i][0])
            centros[lista_numeros[i]] = centro
        #print(centros)
    

    
    cv2.imshow('Mi Camara', frame) #imagen de la camara

        
    tecla = cv2.waitKey(1) & 0xFF 
    if tecla == 27: # Presiona la tecla 'Esc' para salir
        break
    # 2. Sale si se presiona el botón 'X' para cerrar la ventana
    if cv2.getWindowProperty('Mi Camara', cv2.WND_PROP_VISIBLE) < 1:
        break

# Liberamos el recurso de la cámara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()