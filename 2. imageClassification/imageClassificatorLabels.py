import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import ImageFont, ImageDraw, Image

# 모델 가져오기
model = load_model('model.h5')
model.summary()

# 레이블 가져오기
labels=[]
f=open("labels.txt", "r")
for x in f:
     labels.append(x.rstrip('\n'))
label_count = len(labels)
f.close()

# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

# loop through frames
while webcam.isOpened():

    # read frame from webcam
    status, frame = webcam.read()

    if not status:
        break

    # 이미지 높이, 폭 추출
    h = frame.shape[0]
    w = frame.shape[1]

    # 이미지를 teachable machine이 학습할 때 사용하는 이미지 비율로 크롭
    frame = frame[0:h, int((w-h)/2):int(w-((w-h)/2))]

    img = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    prediction = model.predict(x)
    predicted_class = np.argmax(prediction[0]) # 예측된 클래스 0, 1, 2

    # 글씨 넣기 준비
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    fontColor = (0,255,0)
    lineThickness = 1

    # 표기 문구 초기화
    scoreLabel = 0
    score = 0
    result = ''

    for x in range(0, label_count):
        #예측값 모니터링
        line=('%s=%0.0f' % (labels[x], int(round(prediction[0][x]*100)))) + "%"
        cv2.putText(frame, line, (10,(x+1)*35), font, fontScale, fontColor, lineThickness)

        # 가장 높은 예측 찾기
        if score < prediction[0][x]:
            scoreLabel = labels[x]
            score = prediction[0][x]
            result = str(scoreLabel) + " : " + str(score)
            # print(result)

    # 최고 결과치 보여주기
    frame = cv2.putText(frame, result, (10, int(label_count+1)*35), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

    # display
    cv2.imshow('imageClassficator', frame)


    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(np.round(prediction[0], 2))
        print(predicted_class)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()
