import cv2 as cv
import numpy as np

img = cv.imread('/home/han/Projects/frame/tests/squares.jpg')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# edges = cv.Canny(gray,50,150,apertureSize = 3)
# lines = cv.HoughLines(edges,1,np.pi/180,200)
# for line in lines:
#     rho,theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
# cv.imwrite('houghlines3.jpg',img)
#
#
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# edges = cv.Canny(gray,50,150,apertureSize = 3)
# lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
# for line in lines:
#     x1,y1,x2,y2 = line[0]
#     cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# cv.imwrite('houghlines5.jpg',img)

from matplotlib import pyplot as plt
# img = cv.imread('/home/han/Projects/frame/tests/squares.jpg')
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

