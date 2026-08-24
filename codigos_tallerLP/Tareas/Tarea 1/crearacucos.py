import cv2
import numpy as np

# 1. Definir el diccionario (tipo de ArUco)
diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

for i in range(3):
    id_marcador = i      # El número de identificación del ArUco (0 a 249)
    tamano_pixeles = 400  # Tamaño de la imagen final (400x400 píxeles)

    # 3. Generar la imagen del marcador
    # El tercer parámetro representa el grosor del borde (por defecto 1)
    imagen_aruco = cv2.aruco.generateImageMarker(diccionario, id_marcador, tamano_pixeles, 1)

    # 4. Guardar la imagen en tu computadora
    cv2.imwrite(f'aruco_{i}.png', imagen_aruco)

    # 5. Mostrar en pantalla (Opcional)
    cv2.imshow(f'Marcador ArUco Generado {i}', imagen_aruco)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
