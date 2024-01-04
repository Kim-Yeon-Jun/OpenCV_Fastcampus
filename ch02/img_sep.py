import numpy as np
import cv2

img1 = cv2.imread('file.bmp')

img2 = img1[250:650, 450:680]
img3 = img1[250:650, 450:680].copy()

#img2.fill(0)
# 특정 부부에 ROI를 지정해서 처리 가능(Region Of Interest)
cv2.circle(img2,(50,50), 20, (0,0,255),2)

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image3', img3)
cv2.waitKey()
