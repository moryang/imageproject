from skimage import data
from matplotlib import pyplot as plt
import math
import numpy as np
import sys
def rgb2hsi(r,g,b):
    r=r/255
    g=g/255
    b=b/255
    num=0.5*((r-g)+(r-b))
    den=((r-g)*(r-g)+(r-b)*(g-b))**0.5
    if b<=g:
        if den==0:
            den=sys.float_info.min
        h=math.acos(num/den)
    elif b>g:
        if den==0:
            den=sys.float_info.min
        h=(2*math.pi)-math.acos(num/den)
    s=1-(3*min(r,g,b)/(r+g+b))
    i=(r+g+b)/3
    return int(h),int(s*100),int(i*255)
image=data.imread('flower1.jpg')
hsi_image=np.zeros(image.shape,dtype='uint8')
for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r,g,b=image[ii,jj,:]
        h,s,i=rgb2hsi(r,g,b)
        hsi_image[ii,jj,:]=(h,s,i)
H=hsi_image[:,:,0]
S=hsi_image[:,:,1]
I=hsi_image[:,:,2]
S_template=np.zeros(S.shape,dtype='uint8')
for i in range(S.shape[0]):
    for j in range(S.shape[1]):
        if S[i,j]>0.3*S.max():
            S_template[i,j]=1
F=np.zeros(H.shape,dtype='uint8')
for i in range(F.shape[0]):
    for j in range(F.shape[1]):
        F[i,j]=H[i,j]*S_template[i,j]
plt.figure()
plt.axis('off')
plt.imshow(image)
plt.figure()
plt.axis('off')
plt.imshow(H,cmap='gray')
plt.figure()
plt.axis('off')
plt.imshow(S,cmap='gray')
plt.figure()
plt.axis('off')
plt.imshow(I,cmap='gray')
plt.figure()
plt.axis('off')
plt.imshow(S_template,cmap='gray')
plt.figure()
plt.axis('off')
plt.imshow(F,cmap='gray')
plt.show()