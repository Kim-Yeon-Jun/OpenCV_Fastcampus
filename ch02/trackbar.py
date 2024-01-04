import numpy as np
import cv2


def on_level_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255

    img[:] = value
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
#트랙바(트랙바 이름, 창 이름, 초기값 위치, 최대값 위치, 트랙바 이동에 대한 콜백함수 이름)
#창이 생성된 후에 호출해야 함
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
