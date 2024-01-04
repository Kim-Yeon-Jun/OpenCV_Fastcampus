import numpy as np
import cv2

#새 영상 생성하기
img1 = np.empty((240,320), dtype=np.uint8) #그레이스케일 이미지
img2 = np.empty((240,320,3), dtype=np.uint8) #트루컬러 형식의 이미지
img3 = np.ones((240,320,3), dtype=np.uint8) #1로 초기화된 픽셀 이미지 
img4 = np.full((240,320), 123, dtype=np.uint8) # 123으로 초기화된 픽셀 이미지
# img3 = img3 * 255  // 픽셀값으로 처리하는 것이기 때문에 연산도 가능하다
img5 = np.full((240,320,3), (0,0,255), dtype=np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.imshow('img5', img5)

cv2.waitKey()