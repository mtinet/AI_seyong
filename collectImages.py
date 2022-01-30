import cv2

# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()


sample_num = 0
captured_num = 0

# loop through frames
while webcam.isOpened():

    # read frame from webcam
    status, frame = webcam.read()
    sample_num = sample_num + 1

    if not status:
        break

    # display output
    cv2.imshow("captured frames", frame)
    frame = frame[0:h, int((w-h)/2):int(w-((w-h)/2))]

    if sample_num == 8:
        captured_num = captured_num + 1
        # 폴더를 먼저 만들어 놓아야 저장이 됨, 폴더 안에 기존 사진은 모두 삭제
        cv2.imwrite('./ob1/img'+str(captureㄴd_num)+'.jpg', frame) # 첫번째 이미지 수집시
        # cv2.imwrite('./ob2/img'+str(captured_num)+'.jpg', frame) # 두번째 이미지 수집시
        # cv2.imwrite('./ob3/img'+str(captured_num)+'.jpg', frame) # 세번째 이미지 수집시
        sample_num = 0


    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()
