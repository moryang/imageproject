import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
def log(c, img):
    output = c * np.log(1.0 + img)
    output = np.uint8(output + 0.5)
    return output
img=cv2.imread(r'girl.jpg')
print(img)
output = log(42, img)
gamma_img1 = np.zeros((img.shape[0], img.shape[1],img.shape[2]), dtype=np.float32)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        gamma_img1[i, j, 0] = math.pow(img[i, j, 0], 0.4)*1.1
        gamma_img1[i, j, 1] = math.pow(img[i, j, 1], 0.4)*1.1
        gamma_img1[i, j, 2] = math.pow(img[i, j, 2], 0.4)*1.1
cv2.normalize(gamma_img1, gamma_img1, 0, 255, cv2.NORM_MINMAX)
gamma_img1=cv2.convertScaleAbs(gamma_img1)
plt.subplot(221)
plt.imshow(output)
plt.subplot(222)
plt.imshow(img)
plt.subplot(223)
plt.imshow(gamma_img1)
plt.show()