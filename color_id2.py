import cv2
import numpy
import matplotlib.pyplot as plt
from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt


img = cv2.imread('painting01.png')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = cv2.inRange(hsv_img, 100,255)
cv2.imwrite('mask.png', mask)

im = io.imread('mask.png')
val = filters.threshold_otsu(im)
drops = ndimage.binary_fill_holes(im < val)
plt.imshow(drops, cmap='gray')
plt.show()

from skimage import measure
labels = measure.label(drops)
print(labels.max())