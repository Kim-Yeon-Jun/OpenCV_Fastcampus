import sys
import math
import numpy as np
import cv2

#좌측 상단을 기준으로 하는 회전 방식
src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

#각도 -> 라디안 표기법으로 변환
rad = 20 * math.pi / 180
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
