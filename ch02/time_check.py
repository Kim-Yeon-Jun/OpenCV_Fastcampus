import sys
import time
import numpy as np
import cv2


img = cv2.imread('file.bmp')

tm = cv2.TickMeter()

tm.reset()
tm.start()
t1 = time.time()

edge = cv2.Canny(img, 50, 150)

tm.stop()
ms = tm.getTimeMilli()
t2 = time.time()

exec_time = t2 - t1

print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

