import sys
import cv2

#마스크 영상을 이용한 영상 합성
src = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)#cv2.IMREAD_UNCHANGED : alpha 채널까지 포함하여 읽음
mask = src[:, :, -1]
src = src[:, :, 0:3]
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]
crop = dst[0:h, 0:w]

cv2.copyTo(src, mask, crop)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()