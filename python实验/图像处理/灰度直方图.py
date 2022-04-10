import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def histogram(grayfig):
    x = grayfig.size[0]
    y = grayfig.size[1]
    ret = np.zeros(256)
    for i in range(x):
        for j in range(y):
            k = grayfig.getpixel((i, j))
            ret[k] = ret[k] + 1
    for k in range(256):
        ret[k] = ret[k] / (x * y)
    return ret
im = Image.open(r'girl.jpg')
im_gray = im.convert('L')
lenaGrayHist_1 = histogram(im_gray)
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title("灰度直方图")
plt.bar(range(256),lenaGrayHist_1,color='black')
plt.show()