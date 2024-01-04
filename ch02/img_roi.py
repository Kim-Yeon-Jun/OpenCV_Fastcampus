import sys
import cv2

#마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

#src, mask, dst는 사이즈가 같아야하고, src와 dst는 타입이 같아야함(그레이, 트루컬러) mask는 무조건 그레이스케일
cv2.copyTo(src, mask, dst) #(입력영상, 마스크 영상, 출력영상)

#boolean 방식
dst[mask > 0] = src[mask > 0]


cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()