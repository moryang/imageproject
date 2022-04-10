import cv2
from matplotlib import pyplot as plt
import numpy as np
def im2double(im):
    out = cv2.normalize(im.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
    return out
Image=cv2.imread(r'lotus.png')
Image_yaun=Image
Image_1=cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)



NewImage1=np.zeros((Image_1.shape[0], Image_1.shape[1]), dtype=np.uint8)
NewImage2=Image
r_left, r_right = 150, 230
r_min, r_max = 0, 255
for x in range(Image_1.shape[0]):
    for y in range(Image_1.shape[1]):
        if Image_1[x,y]<170:
            NewImage1[x, y] = 90
        else:
            NewImage1[x, y]=250
        if Image_1[x,y]  > 90 and Image_1[x,y]  < 170:
            NewImage2[x,y]  = 0
plt.subplot(131)
plt.imshow(NewImage1,cmap='gray')
plt.subplot(132)
plt.imshow(NewImage2,cmap='gray')
plt.subplot(133)
plt.imshow(Image_1,cmap='gray')
plt.show()