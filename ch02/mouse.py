import sys
import numpy as np
import cv2


oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy, img

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
 
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y
        if flags & cv2.EVENT_FLAG_RBUTTON:
            cv2.circle(img, (x,y), 5, (0, 0, 255), -1)
            cv2.imshow('image', img)
            

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
#마우스 콜백 함수는 창이 떠있는 상태에서 호출이 되어야함
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
