import cv2
import sys

print('Hello OpenCV', cv2.__version__)

img = cv2.imread('file.bmp',cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image not load')
    sys.exit()

# cv2.imwrite('file_gray.png', img)

cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.waitKey()

cv2.destroyAllWindows()