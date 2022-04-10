import cv2
import random
import matplotlib.pyplot as plt
from skimage import data,io,transform
import numpy as np
def D(img):
    z = random.random()
    change = np.array([[1,z,0],[0,1,0]], dtype=np.float32)
    height2, width2, locat2=img.shape
    imge_share=cv2.warpAffine(img,change,dsize=(int(width2 + z*height2 ),height2))
    return imge_share
plt.figure(num='蝴蝶',figsize=(10,8))
plt.subplot(345)
img1=plt.imread('butterfly.jpg')
plt.imshow(img1)
plt.axis('off')
plt.title('蝴蝶原图',fontproperties='SimHei')
plt.subplot(346)
img2=plt.imread('mountain.jpg')
plt.imshow(img2)
plt.axis('off')
plt.title('草地原图',fontproperties='SimHei')
height1,width1,locat1=img1.shape
height,width,locat=img2.shape
composite_image=np.ones((height,width,locat),dtype=np.double)
composite_image[:height,:width,:]=img2[:]
for i in range(20):
    img7 = D(img1)
    narrow = random.randint(10,60)
    height4,width4 = int(height1/narrow),int(width1/narrow)
    img = transform.resize(img7,(height4,width4))
    height3,width3 = random.randint(1,width-width4),random.randint(1,height-height4)
    mat_change = np.float32([[1, 0, height3], [0, 1, width3]])
    fun = cv2.warpAffine(img,mat_change,(height3+width4,width3+height4))
    composite_image[0:width3+height4, 0:height3+width4, :] = composite_image[0:width3+height4, 0:height3+width4, :] + fun*255
plt.subplot(122)
plt.axis('off')
plt.imshow(composite_image.astype('uint8'))
plt.title('漫天飞舞的蝴蝶',fontproperties='SimHei')
plt.show()