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


while True:
    if ser.readable():
        val = input()

        if val == '1':
            val = val.encode('utf-8')
            ser.write(val)
            print("LED TURNED ON")
            time.sleep(0.5)

        elif val == '0':
            val = val.encode('utf-8')
            ser.write(val)
            print("LED TURNED OFF")
            time.sleep(0.5)
