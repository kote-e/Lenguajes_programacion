import cv2
import numpy as np

W = 1000
H = 500

img = []

for i in range(H):
    row = []
    for j in range(W):
        row.append(200)
    img.append(row)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
img = np.array(img).astype(np.uint8)
for i in range(4):
    marker_id = i     
    marker_size = 100 
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
    from random import randint
    r1 = randint(0, img.shape[0] - 100)
    r2 = randint(0, img.shape[1] - 100)
    
    print(r1,r2)
    print(img[r1:r1+100, r2:r2+100].shape)
    img[r1:r1+100, r2:r2+100] = marker_image

cv2.imshow("Titulo", img)
cv2.waitKey(0)

