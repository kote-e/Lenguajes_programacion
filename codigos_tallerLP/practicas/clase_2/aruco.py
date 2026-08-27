import cv2
import numpy as np

w= 1000
h= 500

img=[]

for i in range(h):
    row=[]
    for j in range(w):
        row.append(255) #(242, 234, i) o 255
    img.append(row)

img= np.array(img).astype(np.uint8)
cv2.imshow("Titulo", img)

cv2.waitKey(0)

#--------------------------------------------------------------------------------------------

# 1. Define the dictionary to use (6x6 grid blocks, max 250 unique IDs)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# 2. Specify marker ID and desired size (pixels)
marker_id = 0
marker_size = 100

# 3. Generate the binary matrix image
marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
# 4. Save and display the marker



cv2.imwrite("aruco0.png", marker_image)
cv2.imshow("Generated ArUco Marker", marker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

img[0:100, 0:100]= marker_image
cv2.imshow("Titulo", img)
cv2.waitKey(0)