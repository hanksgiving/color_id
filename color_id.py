import cv2
import numpy
import matplotlib.pyplot as plt
from skimage import measure

img = cv2.imread('painting02.png')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

red = (0, 0, 0)
cyan= (300, 100, 100)

#mask3 = cv2.inRange(hsv_img, (255, 55, 0), (255, 221, 0))
#mask3 = cv2.inRange(hsv_img, (255, 98, 0), (255, 187, 0))
#mask2 = cv2.inRange(hsv_img, (0, 0, 0), (70, 255, 4))
#mask2 = cv2.inRange(hsv_img, (0, 0, 0), (245, 66, 206))
#mask1 = cv2.inRange(hsv_img, (0, 0, 0), (66, 245, 135))
#mask = cv2.inRange(hsv_img, (85, 50, 40), (135, 255, 255))

#mask1 = cv2.inRange(hsv_img, (9, 60, 106), (14, 185, 238))
#mask1 = cv2.inRange(hsv_img, (10, 127, 127), (120, 255, 255))
##gets the darkspots
#mask1 = cv2.inRange(img, (0, 0, 0), (180, 100, 100))
#mask1 = cv2.inRange(hsv_img, (0, 0, 0), (140, 255, 255))
#mask2 = cv2.inRange(hsv_img, (110, 20, 20), (180, 255, 255))
#mask3 = cv2.inRange(hsv_img, (16, 139, 226), (22, 216, 223))
#mask4 = cv2.inRange(hsv_img, (22, 216, 223), (175, 16, 223))

#mask = cv2.bitwise_or(mask1, mask2)
##Light background & dark spots
##mask1 = cv2.inRange(hsv_img, 100,255)
#mask1 = cv2.inRange(hsv_img, 50,255)
##result = cv2.bitwise_and(hsv_img, hsv_img, mask=mask1)

#lower_blue = (0, 0, 0)
#upper_blue = (14, 144, 238)

##mask = cv2.inRange(hsv_img, 100,255)

img_erode = cv2.medianBlur(hsv_img, 7)

## Countouring
##ret,thresh = cv2.threshold(img_erode,100,255,1)
## Contouring Darker
ret,thresh = cv2.threshold(img_erode,50,255,1)

#contours,h = cv2.findContours(thresh,1,2)
contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
for cnt in contours:
    img = cv2.drawContours(hsv_img,[cnt],0,(255,255,255),1)

print(len(contours))
#plt.subplot(1, 2, 1)
#plt.imshow(result, cmap="gray")
#plt.subplot(1, 2, 2)
#plt.imshow(mask)
#plt.imshow(hsv_img)
plt.imshow(img)
plt.show()


