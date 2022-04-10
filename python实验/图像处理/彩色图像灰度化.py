from skimage import data
from matplotlib import pyplot as plt
import numpy as np
image=data.coffee()
max_gray=np.zeros(image.shape[0:2],dtype='uint8')
ave_gray=np.zeros(image.shape[0:2],dtype='uint8')
weight_gray=np.zeros(image.shape[0:2],dtype='uint8')
for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r,g,b=image[ii,jj,:]
        max_gray[ii,jj]=max(r,g,b)
        ave_gray[ii,jj]=(r+g+b)/3
        weight_gray[ii,jj]=0.30*r+0.59*g+0.11*b
plt.figure()
plt.axis('off')
plt.imshow(image)
plt.figure()
plt.axis('off')
plt.imshow(max_gray,cmap='gray')
plt.figure()
plt.axis('off')
plt.imshow(ave_gray,cmap='gray')
plt.figure()
plt.axis('off')
plt.imshow(weight_gray,cmap='gray')
plt.show()