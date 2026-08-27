import cv2
import numpy as np


w= 1000
h= 500

personaje = cv2.imread("personaje.jpg")
personaje = cv2.resize(personaje, (100, 100))

boo= cv2.imread("boo.png")
boo= cv2.resize(boo, (100, 100))
x,y = 50, 50
xb, yb= 300, 300
speed = 5

while True:
    img=np.full((h, w, 3), 255, dtype=np.uint8)
    
    if y < 0 or y+personaje.shape[0] > img.shape[0] or x < 0 or x+personaje.shape[1] > img.shape[1]:
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):         
                if i in range(y,y+personaje.shape[0],1) and j in range(x, x+personaje.shape[1]):
                    img[i,j]= personaje[i-y][j-x]
    else:
        img[y:y+personaje.shape[0], x:x+personaje.shape[1]] = personaje
    
    
    
    img[yb:yb+boo.shape[0], xb:xb+boo.shape[1]]= boo
    
    cv2.imshow("Juego v1", img)
    
    if x <xb+boo.shape[1] and x+personaje.shape[1] > xb and y < yb+boo.shape[0] and y+personaje.shape[1] > yb:
        break
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
    elif cv2.getWindowProperty('Juego v1', cv2.WND_PROP_VISIBLE) < 1: #Sale si se presiona el botón 'X' para cerrar la ventana
        break