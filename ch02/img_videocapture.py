import sys
import cv2

# 카메라 열기(0 : 기본 카메라)
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture() 
#cap.open(0)
if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

#cap.get()을 통해서 장치의 속성 값을 참조할 수 있다.
W = int(cap.get(cv2.CAP_PORP_FRAME_WIDTH)) #프레임의 가로 크기
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #프레임의 세로 크기
print(W, H)

#cap.set()으로 장치의 속성 값을 지정할 수 있다.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리★
while True:
    ret, frame = cap.read() # 현재 open된 카메라에서 True, false와 1프레임씩 받아옴 

    if not ret:
        break

    inversed = ~frame  # 반전
    
    #윤곽선 추출
    edge = cv2.Canny(frame, 50, 150)
    
    
    cv2.imshow('frame', frame) #프레임을 화면에 출력
    cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)
    if cv2.waitKey(10) == 27: #ESC 입력시 while문 탈출
        break

cap.release()
cv2.destroyAllWindows()
