import cv2
import numpy as np
from imutils import resize


def rle_encoding(data):
    encoding = []
    prev_char = data[0]
    count = 1
    for value in data[1:]:
        if value == prev_char:
            count+=1
        else:
            encoding.extend([prev_char,count])
            prev_char = value
            count =1
    encoding.extend([prev_char,count])
    return encoding

image = cv2.imread('image.bmp')
grayscale_img = cv2.cvtColor(image,cv2.IMREAD_GRAYSCALE)

width = int(grayscale_img.shape[1] * 0.5)
height = int(grayscale_img.shape[1] * 0.5)
dim = (width,height)

pixels = grayscale_img.flatten()



compersed_img = rle_encoding(pixels)
compersed_array = np.array(compersed_img,dtype=np.uint8)

np.save("Compersed_Exam", compersed_array)
print("Done")