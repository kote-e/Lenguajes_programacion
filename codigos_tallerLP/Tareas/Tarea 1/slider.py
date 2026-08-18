import cv2
import numpy as np
from arucos_ldp import calcular_centro

W = 1000
H = 500

img = []

# for i in range(H):
#     row = []
#     for j in range(W):
#         row.append(200)
#     img.append(row)

# img = np.array(img).astype(np.uint8)
img = np.full((H, W, 3), 255, dtype=np.uint8)
# print(img.shape)


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# 2. Configure marker details
marker_size = 100   # Dimensions of output image in pixels (400x400)

# 3. Generate the marker image
marker_image_0 = cv2.aruco.generateImageMarker(aruco_dict, 0, marker_size)
marker_image_1 = cv2.aruco.generateImageMarker(aruco_dict, 1, marker_size)
marker_image_2 = cv2.aruco.generateImageMarker(aruco_dict, 2, marker_size)

marker_image_0 = cv2.cvtColor(marker_image_0, cv2.COLOR_GRAY2BGR)
marker_image_1 = cv2.cvtColor(marker_image_1, cv2.COLOR_GRAY2BGR)
marker_image_2 = cv2.cvtColor(marker_image_2, cv2.COLOR_GRAY2BGR)

# print(f"Las dimensines de la imagen son {img.shape}")
# print(f"Las dimensines del aruco son {marker_image_0.shape}")

# 4. Save the generated image
cv2.imwrite("aruco_marker_0.png", marker_image_0)
cv2.imwrite("aruco_marker_1.png", marker_image_1)
cv2.imwrite("aruco_marker_2.png", marker_image_2)
print("ArUco marker saved successfully as 'aruco_marker_0.png'")

from random import randint
r1 = randint(0, img.shape[0] - 100)
r2 = randint(0, img.shape[1] - 100)

r3 = randint(0, img.shape[0] - 100)
r4 = randint(0, img.shape[1] - 100)

r5 = randint(0, img.shape[0] - 100)
r6 = randint(0, img.shape[1] - 100)


# print(r1,r2)
# print(r3,r4)
# print(img[r1:r1+100, r2:r2+100].shape)
img[r1:r1+100, r2:r2+100] = marker_image_0
img[r3:r3+100, r4:r4+100] = marker_image_1
img[r5:r5+100, r6:r6+100] = marker_image_2
# img[H-120:H-120+100, W-120:W-120+100] = marker_image_2


# print(img[r1-5:r1+5, r2-5:r2+5])

detector_params = cv2.aruco.DetectorParameters()
    
# 3. Create the ArUco Detector instance (OpenCV 4.7+)
detector = cv2.aruco.ArucoDetector(aruco_dict, detector_params)
corners, ids, _ = detector.detectMarkers(img)

print(corners)
# print(corners[1][0][0][0], corners[1][0][0][1])

dict_ids = {}
print(list(ids))
for e, i in enumerate(ids):
    dict_ids[int(i[0])] = e

print(dict_ids)

centro_1 = calcular_centro(corners[dict_ids[0]][0][0][0], corners[dict_ids[0]][0][0][1], marker_size)
centro_2 = calcular_centro(corners[dict_ids[1]][0][0][0], corners[dict_ids[1]][0][0][1], marker_size)
centro_3 = calcular_centro(corners[dict_ids[2]][0][0][0], corners[dict_ids[2]][0][0][1], marker_size)
print(ids)
# print(centro_1, centro_2)
cv2.line(img, centro_1, centro_2, (255,0,0), 10)
cv2.circle(img, centro_3, 3, (0,0,255), 5)
print("#"*50, "\n"*10)
cv2.imshow("img", img)
cv2.waitKey(0)


