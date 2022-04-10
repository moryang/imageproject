from skimage import data
from matplotlib import pyplot as plt
img1=data.camera()
img2=data.moon()
plus_img=img1+img2
sub_img=img1-img2
mult_img=img1*img2
div_img=img1/img2
plt.set_cmap(cmap='gray')

plt.subplot(3,2,1)
plt.imshow(img1)
plt.title("original camera")

plt.subplot(3,2,2)
plt.imshow(img2)
plt.title("original moon")

plt.subplot(3,2,3)
plt.imshow(plus_img)
plt.title("plusimg")

plt.subplot(3,2,4)
plt.imshow(sub_img)
plt.title("subimg")

plt.subplot(3,2,5)
plt.imshow(mult_img)
plt.title("multimg")

plt.subplot(3,2,6)
plt.imshow(div_img)
plt.title("divimg")
plt.show()