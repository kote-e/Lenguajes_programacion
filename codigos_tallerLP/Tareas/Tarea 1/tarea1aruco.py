import cv2
import numpy as np

# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolum

# ## Configurar control de volumen de Windows (PyCaw)
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume_control = interface.QueryInterface(IAudioEndpointVolume)

def calcular_centro(esquinas):
    filas= esquinas[:, 0]
    columnas = esquinas[:, 1]

    xc = int(np.mean(filas)) #mean calcula el promedio de los valores
    yc = int(np.mean(columnas))
    return (xc, yc)


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250) #diccionario de aruco
parametros = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parametros) #detector de aruco, se le pasa el diccionario y los parametros

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #abrimos la camara, 0 es la camara por defecto, si hay mas de una camara se puede cambiar el numero
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

        lista_numeros  = ids.flatten().tolist()
        #print(f"IDs detectados: {lista_numeros}")
        centros = {}
        for i, id in enumerate(lista_numeros):
            centro = calcular_centro(esquinas[i][0])
            centros[id] = centro
        #print(centros)
        #print(esquinas)
        if 0 in centros and 1 in centros and 2 in centros:
            x0, y0 = centros[0]
            x1, y1 = centros[1]
            x2, y2 = centros[2]
            cv2.line(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)
            distancia = np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            #print(f"Distancia: {distancia:.2f} píxeles")
            
            divisiones=[]
            distancias=[]
            for j in range(0, 7):
                punto=(int(x0 + (x1 - x0) * j / 6), int(y0 + (y1 - y0) * j / 7))
                #print(f"punto: {punto}")
                divisiones.append(punto)
                distancias.append(np.sqrt((punto[0] - x2) ** 2 + (punto[1] - y2) ** 2))

            for punto, distancia in zip(divisiones, distancias):
                cv2.circle(frame, punto, 7, (0, 0, 255), -1)
                if distancia == min(distancias):
                    cv2.line(frame, punto, (x2, y2), (0, 0, 255), 2)
                else:
                    cv2.line(frame, punto, (x2, y2), (0, 255, 0), 2)
            #print(divisiones)


    cv2.imshow('Mi Camara', frame) #imagen de la camara

        
    tecla = cv2.waitKey(1) & 0xFF 
    if tecla == 27: # Presiona la tecla 'Esc' para salir
        break
    # 2. Sale si se presiona el botón 'X' para cerrar la ventana
    if cv2.getWindowProperty('Mi Camara', cv2.WND_PROP_VISIBLE) < 1:
        break

# Liberamos el recurso de la cámara y cerramos las ventanas
cap.release()#
cv2.destroyAllWindows()