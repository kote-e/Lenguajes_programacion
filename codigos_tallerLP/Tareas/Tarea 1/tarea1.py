import cv2 
import numpy as np
from random import randint

W = 1000
H = 500
img = []

for i in range(H):
    row = []
    for j in range(W):
        row.append(200)
    img.append(row)
img = np.array(img).astype(np.uint8) #convertir a array de numpy y tipo uint8 osea una imagen


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250) #dicccionario de aruco
posiciones = [] # aqui voy a poner las posiciones de los marcadores de aruco para que no se repitan ni se superpongan
for i in range(2):
    marker_id = i     
    marker_size = 100
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size) #buscando el marcador de aruco con el id y tamaño especificado

    buscar = True
    while buscar:
        r1 = randint(0, img.shape[0] - 100)
        r2 = randint(0, img.shape[1] - 100)

        if (r1,r2) not in posiciones: #si la posicion no esta en la lista de posiciones
            if len(posiciones) == 0: #si la lista de posiciones esta vacia
                posiciones.append((r1,r2)) #agregar la posicion a la lista de posiciones
                buscar = False #salir del while
            else:
                buscar = False
                for pos in posiciones:
                    if (r1 < pos[0] + 100 and r1 + 100 > pos[0] and  r2 < pos[1] + 100 and r2 + 100 > pos[1]): #si la posicion esta en la lista de posiciones
                        buscar = True #seguir buscando
                        break
                if not buscar:
                    posiciones.append((r1,r2)) #agregar la posicion a la lista de posiciones

    print(r1,r2)
    print(img[r1:r1+100, r2:r2+100].shape)
    img[r1:r1+100, r2:r2+100] = marker_image #reemplazando la parte de la imagen con el marcador de aruco generado

centro1 = (posiciones[0][1] + 50, posiciones[0][0] + 50)
centro2 = (posiciones[1][1] + 50, posiciones[1][0] + 50)
cv2.line(img, centro1, centro2, 0, 2) # imagen, punto_inicial, punto_final, color, grosor


cv2.imshow("Titulo", img)
cv2.waitKey(0)