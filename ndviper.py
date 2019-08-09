import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
import numpy as np
from PIL import Image

image=plt.imread('result1.jpg')
NIR = image[:, :, 0].astype('float')
blue = image[:, :, 2].astype('float')
green = image[:, :, 1].astype('float')
bottom = (blue - green) ** 2
bottom[bottom == 0] = 1  # replace 0 from nd.array with 1
VIS = (blue + green) ** 2 / bottom
NDVI = ((NIR - VIS) / (NIR + VIS))
ndvi_list = NDVI.tolist()
print(NDVI)
total = len(NDVI[0])*len(NDVI)
print("total ndvi", total)

dense = 0
sparse = 0
barren = 0
for list in NDVI:
    for sublist in list:
        if (sublist>= 0.6):
            dense += 1
        elif (sublist<0.6 and sublist>=0.2):
            sparse += 1
        elif (sublist< 0.2):
            barren += 1

print("dense no.",dense)
print("sparse no.",sparse)
print("barren no.",barren)

print('dense % = ',(dense/total)*100)
print('sparse % = ',(sparse/total)*100)
print('barren % = ',(barren/total)*100)


#cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [ 'red','orange', 'yellow', 'green'])
#fig, ax = plt.subplots()
#ax.imshow(NDVI,cmap=cmap)
#plt.axis('off')
#plt.show(fig)

#img=Image.fromarray(NDVI,'RGB')
#img.save('outp_ndvi.jpg')
#img.show()

#plt.imshow(NDVI, interpolation='spline16')
#plt.show()