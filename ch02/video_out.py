import sys
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) #숫자를 직접 지정할 수도 있음

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
delay = round(1000 / fps) # 프레임간의 사이의 시간을 계산하기 위한 식

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #inversed = ~frame

    #out.write(inversed)
    out.write(frame)

    cv2.imshow('frame', frame)
    #cv2.imshow('inversed', inversed)

    #엣지 = 그레이스케일 형태 != 컬러영상 기존 방식으로는 저장 못함    
    #edge = cv2.Canny(frame, 50, 150)
    #컬러영상으로 변환해서 저장해줘야 함
    #edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    #out.write(edge)
    #cv2.imshow('edge', edge)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
