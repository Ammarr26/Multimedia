import cv2
import numpy as np

img = np.ones((300,300,3) , dtype=np.uint8)* 255

cv2.rectangle(img, (50,50) , (250,250) , (0,255,0) , 2)
cv2.line(img, (50,50) , (250,250) , (610,0,0) , 2)



center= (img.shape[1] // 2 , img.shape[0] // 2 )
angle = 45
scale = 1.0

rotaion_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotaed_img = cv2.warpAffine(img, rotaion_matrix, (img.shape[1] , img.shape[0]))

cv2.imshow("Original img",img)
cv2.imshow("Rotated img",rotaed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()