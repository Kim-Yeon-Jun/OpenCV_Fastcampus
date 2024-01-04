import sys
import cv2

#영상 불러오기
img1 = cv2.imread('file.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('file.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load Failed')
    sys.exit()


#영상의 속성 참조
print('type(img1) : ', type(img1))
print('type(img2) : ', type(img2))
print('img1.shape : ', img1.shape)
print('img2.shape : ', img2.shape)
print('img1.dtype : ', img1.dtype)
print('img2.dtype : ', img2.dtype)

#영상의 크기 참조
#그레이 스케일 이미지 (_,_)
h, w = img1.shape[:2]
print('w x h = {} x {}'.format(w,h))

#트루컬러 이미지 (_,_,_)
h2, w2 = img2.shape[:2]
print('img2 size : {} x {}'.format(w2,h2))

if len(img1.shape) == 2: #그레이스케일 조건 img1.ndim == 2 도 같은 조건임
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

#영상의 픽셀값 참조 (처리 속도가 느림 / 제공하는 함수를 이용)
for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = (0,0,255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
