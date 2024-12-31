import cv2

image = cv2.imread('Median_image.png')

Median_filter = cv2.medianBlur(image,ksize=7)

cv2.imshow("Orginal img",image)
cv2.imshow("Denoised img" ,Median_filter)


rgb_image = cv2.cvtColor(Median_filter , cv2.COLOR_RGB2BGR)
rgb_image[: , : , 0]= 0
rgb_image[: , : , 1]= 0

rgb_image = cv2.cvtColor(rgb_image , cv2.COLOR_RGB2BGR)
cv2.imshow("Orginal imzg",rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()