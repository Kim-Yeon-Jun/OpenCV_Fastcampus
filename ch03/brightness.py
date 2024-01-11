import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
src = cv2.imread('file.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, 100)
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)
#컬러 : dst = cv2.add(src, (100, 100, 100,  0))
#dst = src + 100 //255보다 커지면 255가 저장되는 것이 아니라 255를 뺀 수치가 저장이됨
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0))
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
