import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, transform
M = np.array([[0.9, 0.7, 0.1],[0, 1,   0]])
img_but=plt.imread("butterfly.jpg")
img_mun=plt.imread("mountain.jpg")
img_but_small1=img_small=transform.resize(img_but,(601,900))
img_but_warp1=cv.warpAffine(img_but_small1,M,dsize=(900, 601))
img1=(img_mun+img_small)/300
plt.imshow(img1)
plt.show()