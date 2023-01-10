# -*- coding: utf-8 -*-

import requests
import json
from tkinter import *
from tkinter import filedialog
import tkinter.font
import tkinter as tk
from PIL import ImageTk, Image
import wget
import os
import time
import datetime
from tkinter import messagebox
import cv2
import numpy as np


# 시리얼 통신
import serial
import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
com = ''

# 아두이노 연결 com 포트 찾아서 자동으로 연결하기
for port, desc, hwid in sorted(ports):
    if 'Arduino' in desc:
        com = port
if com != '':
    print('\n arduino USB detected: ', com)
else:
    print('\nPlease connect your microbit to this PC via USB')

ser = serial.Serial(com, 9600, timeout=0)

# ex)
# val = '1'
# val = val.encode('utf-8')
# ser.write(val)

payload = {}
files = []
headers = {}
productName = ""
productRate = ""
totalPrice = 0
tmp = ""
count = 0
price_meal = {"30cm자": 2000, "AIVisionSensor": 2000, "CRUNKY": 2000, "DrYou단백질바": 2000, "DrYou에너지바": 2000, "DrYou에너지바_화이트": 2000, "Kitkat_original": 2000, "Kitkat_블루": 2000, "Kitkat_화이트": 2000, "Loacker": 2000, "MagicMouse": 2000, "PUNKY": 2000, "Post단백질바": 2000, "TELLO": 2000, "USB": 2000, "WEBCAM": 2000, "_no_target": 0, "bueno": 2000, "kelloggs에너지바": 2000, "kinder맥시": 2000, "m&m_땅콩": 2000, "m&m_초코": 2000, "milka": 2000, "safe세제": 2000, "가나초코바": 2000, "가나초코바_브라운": 2000, "가위": 2000, "갈배사이다": 2000, "갈아만든배": 2000, "강력본드": 2000, "고구마깡": 2000, "고래밥": 2000, "김치도시락": 2000, "김치사발면": 2000, "김치왕뚜껑": 2000, "꼬깔콘": 2000, "꼬북칩": 2000, "나가사끼짬뽕": 2000, "나쵸": 2000, "다이제": 2000, "닭다리너겟": 2000, "더좋은물티슈": 2000, "도시락": 2000, "땅콩강정": 2000, "라면볶이": 2000, "마이구미": 2000, "매일바이오_딸기": 2000, "매일바이오_블루베리": 2000, "바이오캔디": 2000, "불닭볶음면": 2000, "비틀즈": 2000, "빼빼로_아몬드": 2000, "빼빼로_오리지널": 2000, "뽀로로짜장": 2000, "뿌셔뿌셔": 2000, "사리곰탕면": 2000, "삼양라면": 2000, "새우탕": 2000, "수박젤리": 2000, "스낵면": 2000, "스니커즈": 2000, "스프라이트": 2000, "신라면": 2000, "썬": 2000, "아빠맘": 2000, "야채죽": 2000, "열라면": 2000, "예감": 2000, "오감자": 2000, "오뚜기카레": 2000, "오뜨": 2000, "왕꿈틀이": 2000, "왕뚜껑": 2000, "육개장": 2000, "자연퐁솔잎": 2000, "자연퐁오렌지": 2000, "자유시간": 2000, "자유시간_미니": 2000, "자유시간_미니아몬드": 2000, "자유시간_아몬드": 2000, "잘풀리는집": 2000, "진라면매운맛": 2000, "진라면순한맛": 2000, "짜파게티범벅": 2000, "짬뽕왕뚜껑": 2000, "짱셔요": 2000, "쫄병": 2000, "참붕어빵": 2000, "청소박사": 2000, "초단백질바": 2000, "초코송이": 2000, "초코칩": 2000, "초코파이": 2000, "칠성사이다": 2000, "코카콜라": 2000, "크린백": 2000, "크린장갑": 2000, "크립": 2000, "키친타올": 2000, "포스틱": 2000, "포키_테이스티": 2000, "핫브레이크": 2000, "해바라기": 2000, "허니버터오징어": 2000, "화이트테이프": 2000, "환타": 2000}

# 데이터 서버에 송신
def recognition(m) :
    # url = "http://61.97.243.126:5003/analyze"
    url = "http://localhost:5003/analyze"

    global files
    print(m)
    files = [('files', ("saved.png", open(m, 'rb'), 'application/octet-stream'))]

    # POST 전송 후 결과값 수신
    print("이미지 업로드 시간:" + str(datetime.datetime.now()))
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print("결과 다운로드 시간:" + str(datetime.datetime.now()))


    global productName
    global productRate
    global totalPrice
    global price_meal
    global tmp

    totalPrice = 0
    tmp = ""

    # 결과 보여주기
    print(response.text)
    print()

    filename = json.loads(response.text)['filename']
    print("파일이름: " + str(filename))
    print()

    results = json.loads(response.text)['results']
    print(type(results))
    print("분석결과:" + str(results))

    for i in results:

        i = str(i).split(',')
        productName = i[0].strip("[").strip("'")
        productRate = i[1].strip("]")
        print("- " + productName + " : " + productRate)
        totalPrice = totalPrice + float(price_meal[productName])


        tmp = tmp + productName + ' : ' + str(price_meal[productName]) + '원' + '\n'

    # 리스트 갯수 세기
    count = len(results)

    print(f'현재 가격은 {totalPrice}원 입니다.')
    print()

    imageAddress = json.loads(response.text)['image']
    print("이미지 저장 주소: " + str(imageAddress))
    print()

    msg = json.loads(response.text)['msg']
    print("메시지:" + str(msg))
    print()

    analizingTimeCheck = json.loads(response.text)['analizingTimeCheck']
    print(str(analizingTimeCheck))
    print()

    # 메시지 보여주기
    # 상품 리스트
    tmp = tmp + '\n' + str(msg)
    text_2.configure(text = tmp)

    # 총 분석시간
    label_time.configure(text = analizingTimeCheck)

    # 수량 갱신
    label_count.configure(text="수량       "+str(count)+" 개")

    # 가격 갱신
    label_price.configure(text="총 금액       "+str(totalPrice)+" 원")


    # 결과 이미지 레이블
    downloadImage = Image.open(wget.download(imageAddress))
    my_image = ImageTk.PhotoImage(downloadImage)
    widget2.configure(image=my_image)
    display(widget2)


def captureCamera() :
    cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    ret, frame1 = cap1.read() # 사진 촬영
    frame1 = cv2.flip(frame1, 1) # 좌우 대칭

    ret, frame2 = cap2.read() # 사진 촬영
    # frame2 = cv2.flip(frame2, 1) # 좌우 대칭

    scaleX = 0.6
    scaleY = 0.6

    # 사진 자르기
    resize1 = cv2.resize(frame1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    resize2 = cv2.resize(frame2, dsize=(640, 480), interpolation=cv2.INTER_AREA)

    # 사진 자르기
    cropped_img1 = resize1[60:350, 0:640]
    cropped_img2 = resize2[60:350, 0:640]

    # 사진 합치기
    add_img = np.vstack((cropped_img1, cropped_img2))

    # 사진 보여주기
    # cv2.imshow('111', frame1)
    # cv2.imshow('222', frame2)
    # cv2.imshow('add', add_img)

    # 사진 저장
    # cv2.imwrite('111.jpg', frame1)
    # cv2.imwrite('222.jpg', frame2)
    cv2.imwrite('capture.jpg', add_img)

    cap1.release()
    cap2.release()


    # cv2.waitKey(0)
    cv2.destroyAllWindows()

    recognition('./capture.jpg')


def openFile():
    global uploadFileName
    tk.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))

    uploadFileName = tk.filename
    recognition(uploadFileName)


def initSetting():
    totalPrice = 0
    label_count.configure(text="수량           "+str(totalPrice)+" 개")
    label_price.configure(text="총 금액           "+str(totalPrice)+" 원")
    label_time.configure(text = "인식속도(초) : ")
    text_2.configure(text = "")


def doorOpen():
    val = '1'
    val = val.encode('utf-8')
    ser.write(val)
    print("문이 열렸습니다.")
    messagebox.showinfo("비상창", "문이 열렸습니다.")
    time.sleep(0.5)
    val = '0'
    val = val.encode('utf-8')
    ser.write(val)


def payRequest():
    val = '1'
    val = val.encode('utf-8')
    ser.write(val)
    print("결제되었습니다.")
    messagebox.showinfo("결제창", "결제되었습니다.")
    doorOpen()
    initSetting()



# GUI
root = tk.Tk()
root.configure(bg="#FFFFFF",)

# getting screen width and height of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

# setting tkinter window size
root.geometry("%dx%d" % (width, height))


font=tkinter.font.Font(family="맑은 고딕", size=15)

# 텍스트 레이블
widget1 = tk.Label(root, text="AI 상품 인식 시스템", fg="black", bg="#FFFFFF", width=30, height=2, font=font)
widget1.pack()


# 프레임 1
frame1 = tk.Frame(root, width="600", height="10", bg="#FFFFFF", padx="20", pady="10")

# 원본 이미지 위젯
my_image = PhotoImage(file="upload.png")
widget2 = tk.Label(frame1, image=my_image)
widget2.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

# 텍스트 레이블
label_price = tk.Label(frame1, width="20", bg="#FFFFFF", padx=10, pady="10", fg="blue", font=font)
label_price.grid(row=0, column=2, padx="10", pady="10")

# 버튼1 레이블
fileUpload = tk.Button(frame1, text="상품 인식하기", padx="10", pady="10", bg='#CCCCCC', width="10", command=lambda: captureCamera(), font='Arial 15')
fileUpload.grid(row=1, column=2, padx=10, pady=10)

# 버튼2 레이블
emergency = tk.Button(frame1, text="비상출입버튼", padx="10", pady="10", bg='#CCCCCC', width="10", command=lambda: doorOpen(), font='Arial 15')
emergency.grid(row=2, column=2, padx=10, pady=10)

frame1.pack(side='top')


# 프레임 2
frame2 = tk.Frame(root, width="600", height="10", bg="#FFFFFF", padx="20", pady="10")

# 주문 리스트
text_1 = tk.Label(frame2, text="장바구니에 담으신 메뉴", bg="#E1E1E1", padx=10, pady="10", font=font)
text_1.pack()

# 주문 리스트
text_2 = tk.Label(frame2, bg="#FFFFFF", padx=10, pady="10", font=font)
text_2.pack()

frame2.pack(side='top')



# 프레임 3
frame3 = tk.Frame(root, width="600", height="10", bg="#FFFFFF", padx="20", pady="10")

# 분석시간
label_time = tk.Label(frame3, text="인식속도(초) : ", padx=10, bg="#FFFFFF",  pady="10", font=font)
label_time.grid(row=0, column=0, padx="10", pady="10")

# 텍스트 레이블
label_count = tk.Label(frame3, text="수량           0 개", width="20", bg="#FFFFFF", padx=10, pady="10", font=font)
label_count.grid(row=1, column=0, padx="10", pady="10")

# 텍스트 레이블
label_price = tk.Label(frame3, text="총 금액           0 원", width="20", bg="#FFFFFF", padx=10, pady="10", fg="red", font=font)
label_price.grid(row=1, column=1, padx="10", pady="10")

# 버튼3 레이블
payment = tk.Button(frame3, text="결제하기", padx="10", pady="10", bg="red", width="10", command=lambda: payRequest(), font='Arial 15')
payment.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

frame3.pack(side='top')

# 메인 루프
root.mainloop()
