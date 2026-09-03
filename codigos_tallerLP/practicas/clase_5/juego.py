import cv2
import numpy as np
import random

def hay_colision(xA, yA, anchoA, altoA, xB, yB, anchoB, altoB):
    solapan_en_x = (xA < xB + anchoB) and (xB < xA + anchoA)
    solapan_en_y = (yA < yB + altoB) and (yB < yA + altoA)
    return solapan_en_x and solapan_en_y

def poner_imag(x, y, personaje, img):
    if y < 0 or y+personaje.shape[0] > img.shape[0] or x < 0 or x+personaje.shape[1] > img.shape[1]:
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):         
                if i in range(y,y+personaje.shape[0],1) and j in range(x, x+personaje.shape[1]):
                    img[i,j]= personaje[i-y][j-x]
    else:
        img[y:y+personaje.shape[0], x:x+personaje.shape[1]] = personaje
    return img

def crear_manzana(x, y, con, img):
    if con:
        x= random.randint(1, img.shape[1]-150)
        y= random.randint(1, img.shape[0]-150)
    return x, y



w= 1000
h= 500

azul= cv2.imread("images.jpg")
ancho=50
azul= cv2.resize(azul, (ancho, 126))
x,y = 50, 50
speed = 5
cantidad= 0

manzana= cv2.imread("images (1).jpg")
manzana= cv2.resize(manzana, (100, 100))
xm, ym = 0, 0
crear_nueva=True

while True:
    img=np.full((h, w, 3), 255, dtype=np.uint8)
    img= poner_imag(x, y, azul, img)
    xm, ym = crear_manzana(xm, ym, crear_nueva, img)
    img=poner_imag(xm, ym, manzana, img)
    crear_nueva= hay_colision(x, y, azul.shape[1], azul.shape[0], xm, ym, manzana.shape[1], manzana.shape[0])
    if crear_nueva:
        cantidad+= 1
        ancho+=20
        azul= cv2.resize(azul, (ancho, 126))
    
    cv2.putText(img, f"manzanas comidas {cantidad}", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5)
    cv2.imshow("Juego", img)
    
    tecla = cv2.waitKey(1) & 0xFF 
    if tecla == ord("d"):
        x= x + speed
    elif tecla == ord("s"):
        y= y + speed
    elif tecla == ord("a"):
        x= x - speed
    elif tecla == ord("w"):
        y= y - speed
    elif tecla == 27: # Presiona la tecla 'Esc' para salir
        break
    elif cv2.getWindowProperty('Juego', cv2.WND_PROP_VISIBLE) < 1: #Sale si se presiona el botón 'X' para cerrar la ventana
        break