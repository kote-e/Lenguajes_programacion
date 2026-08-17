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

img = np.array(img).astype(np.uint8)
print(img)


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# 2. Configure marker details
marker_size = 100   # Dimensions of output image in pixels (400x400)

# 3. Generate the marker image
marker_image_0 = cv2.aruco.generateImageMarker(aruco_dict, 0, marker_size)
marker_image_1 = cv2.aruco.generateImageMarker(aruco_dict, 1, marker_size)

print(f"Las dimensines de la imagen son {img.shape}")
print(f"Las dimensines del aruco son {marker_image_0.shape}")

# 4. Save the generated image
cv2.imwrite("aruco_marker_0.png", marker_image_0)
print("ArUco marker saved successfully as 'aruco_marker_0.png'")

from random import randint
r1 = randint(0, img.shape[0] - 100)
r2 = randint(0, img.shape[1] - 100)

r3 = randint(0, img.shape[0] - 100)
r4 = randint(0, img.shape[1] - 100)


print(r1,r2)
print(r3,r4)
print(img[r1:r1+100, r2:r2+100].shape)
img[r1:r1+100, r2:r2+100] = marker_image_0
img[r3:r3+100, r4:r4+100] = marker_image_1

cv2.imshow("titulo", img)

detector_params = cv2.aruco.DetectorParameters()
    
# 3. Create the ArUco Detector instance (OpenCV 4.7+)
detector = cv2.aruco.ArucoDetector(aruco_dict, detector_params)
corners, ids, _ = detector.detectMarkers(img)
print(ids)
cv2.waitKey(0)
