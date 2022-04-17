import requests
import tkinter as tk
import json


# 시리얼 통신
import serial
import serial.tools.list_ports
import time

# ports = serial.tools.list_ports.comports()
# com = ''
#
# # 아두이노 연결 com 포트 찾아서 자동으로 연결하기
# for port, desc, hwid in sorted(ports):
#     if 'Arduino' in desc:
#         com = port
# if com != '':
#     print('\n arduino USB detected: ', com)
# else:
#     print('\nPlease connect your microbit to this PC via USB')
#
# ser = serial.Serial(com, 9600, timeout=0)

# ex)
# val = '1'
# val = val.encode('utf-8')
# ser.write(val)



# 데이터 서버에 송신
url = "http://61.97.243.126:5003/analyze"

payload = {}
files = [('files', ('5.png', open('5.png', 'rb'), 'application/octst-stream'))]
headers = {}

# 결과 수신
response = requests.request("POST", url, headers=headers, data=payload, files=files)


productName = ""
productRate = ""
totalPrice = 0
price_meal = {"bueno": 2000, "꼬북칩": 3500, "오뜨": 5000, "튀김": 5000, "쫄면": 7000}

# 결과 보여주기
# print(response.text)
# print()

filename = json.loads(response.text)['filename']
print("파일이름: " + str(filename))
print()

results = json.loads(response.text)['results']
# print(type(results))
print("분석결과:" + str(results))

for i in results:
    i = str(i).split(',')
    productName = i[0].strip("[").strip("'")
    productRate = i[1].strip("]")
    print("- " + productName + " : " + productRate)
    totalPrice = totalPrice + float(price_meal[productName])

print(f'현재 가격은 {totalPrice}원 입니다.')
print()

imageAddress = json.loads(response.text)['image']
print("이미지 저장 주소: " + str(imageAddress))
print()

msg = json.loads(response.text)['msg']
print("메시지:" + str(msg))



order_meal = {}

total_price = 0


def show_meal():
    fileUpload.configure(bg="yellow")
    frame2.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame2.pack(fill="both", expand=True)


def meal_add(m):
    global price_meal, order_meal, total_price
    if m not in price_meal:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_meal.get(m)
    total_price += this_price

    if m in order_meal:
        order_meal[m] = order_meal.get(m) + 1
    else:
        order_meal[m] = 1
    print_order()
    print_price()


def print_order():
    global order_meal

    tmp = ""
    for i in order_meal:
        tmp = tmp + i + " X " + str(order_meal.get(i)) + "\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)


def init():
    global total_price, order_meal
    total_price = 0
    del order_meal

    order_meal = {}
    print_price()
    print_order()
    show_meal()


def print_price():
    global total_price
    label_price.configure(text=str(total_price)+" 원")


window = tk.Tk()
window.title("상품 확인 프로그램")
window.geometry("600x250+500+300")
window.resizable(False, False)

frame1 = tk.Frame(window, width="600", height="10", padx="20", pady="10")
frame1.pack(fill="both")
# frame1.pack(fill="both", expand=True)

frame2 = tk.Frame(window, width="600", height="10", padx="20", pady="20")
frame2.pack(fill="both")
# frame2.pack(fill="both", expand=True)

fileUpload = tk.Button(frame1, text="파일 업로드", padx="10", pady="10", bg="yellow", width="10", command=lambda: meal_add('튀김'))
fileUpload.grid(row=0, column=0, padx=10, pady=10)

btn_init = tk.Button(frame1, text="초기화", padx="10", pady="10", command=init)
btn_init.grid(row=0, column=2, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="3", padx="10", pady="10")


# 주문 리스트
text_1 = tk.Text(frame2, height="10")
text_1.pack()

window.mainloop()
