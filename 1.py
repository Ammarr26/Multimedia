import cv2

image = cv2.imread('image.bmp')

cv2.imshow("BMP img" , image)

cv2.waitKey(0)
cv2.destroyAllWindows()