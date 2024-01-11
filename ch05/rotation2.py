import sys
import numpy as np
import cv2

#특정 좌표를 기준으로 회전하는 방식
src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2)
#회전의 중심을 성정한느 getRotationMatrix2D
#확대 비율을 0.5로 설정하여 축소해서 결과를 출력
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
