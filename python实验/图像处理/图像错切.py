import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
M = np.array([[0.9, 0.7, 0.1],[0, 1,   0]])
plt.set_cmap(cmap='gray')
img =data.camera()
plt.subplot(1,2,1)
plt.title("original image")
plt.imshow(img)
img_shear = cv.warpAffine(img,M,dsize=(800, 500))
plt.subplot(1,2,2)
plt.title("warp image")
plt.imshow(img_shear)
plt.show()
