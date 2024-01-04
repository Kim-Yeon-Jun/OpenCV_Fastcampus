import numpy as np
import cv2

img1 = cv2.imread('file.bmp')
img2 = img1 # 영상 복사

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.waitKey()


#==============
img3 = img1.copy()
cv2.imshow('image3', img3)
cv2.waitKey()

#대입과 .copy의 차이
img1[:,:] = (0,255,255)
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image3', img3)
cv2.waitKey()
#결과물은 img1이 바뀐것 처럼 img2도 바뀜. img3는 원래의 img1의 데이터를 가지고 있음
# img2와 img1은 서로 공유, 동일한 데이터로 간주
# img3는 복사해서 새로 사용하는. img1과는 독립적인 데이터로 간주