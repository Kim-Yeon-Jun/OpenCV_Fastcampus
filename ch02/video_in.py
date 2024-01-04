import sys
import cv2


# 비디오 파일 열기(카메라에서는 장치번호, 비디오 파일의 경우 영상 파일 이름을 넣음)
cap = cv2.VideoCapture('video1.mp4')

if not cap.isOpened():
    print("Video open failed!")
    sys.exit()

# 비디오 프레임 크기, 전체 프레임수, FPS 등 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS:', fps)

delay = round(1000 / fps)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    #동영상의 맨 마지막 부분에 도달하면 해당 조건문에 걸림 -> while문 탈출ㅁ
    if not ret:
        break

    inversed = ~frame  # 반전
    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)
    
    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()
