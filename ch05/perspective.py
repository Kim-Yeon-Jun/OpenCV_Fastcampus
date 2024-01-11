import sys
import numpy as np
import cv2


src = cv2.imread('namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

#출력 영상의 크기
w, h = 720, 400

#입력 영상에서 변환할 대상의 4개의 점(좌상, 우상, 우하, 좌하)
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
#위의 점들을 이동시킬 목적지 좌표 설정
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

#3x3 투시변환 행렬 반환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
#최종 변환 영상
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
