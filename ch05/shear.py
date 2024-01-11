import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

#x축 방향으로 전단 변환
aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

#변환된 이미지의 전체를 보기 위해 결과 영상의 크기를 조절
h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
