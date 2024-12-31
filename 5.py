import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage.feature import local_binary_pattern

image_path = 'traka.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

radius = 1
n_point = 8 * radius

lbp = local_binary_pattern(image , n_point , radius)
lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0,n_point+3))
lbp_hist = lbp_hist.astype('float')
lbp_hist /= (lbp_hist.sum()+1e-1)


fig , axes = plt.subplots(1,2,figsize=(12,6))

axes[0].imshow(image,cmap='gray')
axes[0].set_title("Original img")
axes[0].axis("off")

axes[1].imshow(lbp,cmap='gray')
axes[1].set_title("LBP img")
axes[1].axis("off")

plt.figure(figsize=(8,6))
plt.bar(np.arange(0,len(lbp_hist)),lbp_hist,color='blue')
plt.title("LBPs")
plt.xlabel("LBP img")
plt.ylabel("% of Pixels")
plt.show()