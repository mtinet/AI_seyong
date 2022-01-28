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

print('환영합니다. 샘랩 인공지능 카운터입니다.')

count = 0

while True:
    if ser.readable():
        val = ser.readline()
        if (len(val) > 0) :
            val = val.decode()[:len(val)-1]  # 넘어온 데이터 중 마지막 개행문자 제외
            # print(val)
            # 아두이노에서 'i'가 입력되면 숫자를 올리고, 'o'가 입력되면 숫자를 내림, 0보다 작아지면 0으로 고정함.
            if ('o' in val) :
                count = count + 1
                print(f'입장객 수는 {count}입니다.')
            if ('i' in val) :
                count = count - 1
                if (count < 0) :
                    count = 0
                print(f'입장객 수는 {count}입니다.')


        time.sleep(0.1)
