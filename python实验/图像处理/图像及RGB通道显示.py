from skimage import data
from matplotlib import pyplot as plt
image=data.coffee()
plt.figure()
plt.axis('off')
plt.imshow(image)
imageR=image[:,:,0]
plt.figure()
plt.axis('off')
plt.imshow(imageR,cmap='gray')
imageG=image[:,:,1]
plt.figure()
plt.axis('off')
plt.imshow(imageG,cmap='gray')
imageB=image[:,:,2]
plt.figure()
plt.axis('off')
plt.imshow(imageB,cmap='gray')
plt.show()
