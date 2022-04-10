import cv2
from imageio import imread
from numpy import zeros
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from PIL import Image


# # def im2double(im):
# #     min_val = np.min(im.ravel())
# #
# #     max_val = np.max(im.ravel())
# #     out = (im.astype('float') - min_val) / (max_val - min_val)
# #     return out
#
def im2double(im):
    out = cv2.normalize(im.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
    # info = np.iinfo(im.dtype) # Get the data type of the input image
    return out
#     # return im.astype(np.float) / info.max

Image=im2double(rgb2gray(imread('lotus.png')))
h=Image.shape[0]
w=Image.shape[1]
NewImage1=zeros((h,w))
NewImage2=zeros((h,w))
NewImage3=Image
a=30/256
b=100/256
c=75/256
d=200/256
for x in range(w):
    for y in range(h):
        if Image[y, x] < a:
            NewImage1[y,x] = Image[y, x] * c / a
        elif Image[y, x] > b:
            NewImage1[y,x] = (Image[y, x] - a) * (d - c) / (b - a) + c
        else:
            NewImage1[y,x] = (Image[y, x] - b) * (1 - d) / (1 - b) + d
        if Image[y, x] > a and Image[y, x] < b:
            NewImage3[y,x] = (Image[y,x] - a) * (d - c) / (b - a) + c

def imadjust(img):
    f =Image
    f1=zeros((h,w))
    for x in range(w):
        for y in range(h):
            if f[y, x] <= a:
                f1[y, x] = c
            elif f[y, x] >= b:
                f1[y, x]= d
            else:
                f1[y, x] = (d-c)/(b-a)*(f[y,x]-a)+c

    return f1
NewImage2=imadjust(Image)

plt.set_cmap(cmap='gray')
plt.subplot(221)
plt.imshow(rgb2gray(imread('lotus.png')))
plt.subplot(222)
plt.imshow(NewImage3)
plt.subplot(223)
plt.imshow(NewImage1)
plt.subplot(224)
plt.imshow(NewImage2)
plt.show()