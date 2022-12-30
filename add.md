# 프로그램 설치 및 사용 방법

## python 설치(3.8버전으로 설치할 것)
[python 3.8.10 다운로드 링크](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)  

## 기본 라이브러리 설치  
(torch, torchvision을 최신 버전으로 설치하면 소스코드 일부를 수정해야 함)
```python
python.exe -m pip install --upgrade pip
pip install numpy
pip install opencv-python
pip install pillow
pip install matplotlib
pip install easydict
pip install flask
pip install torch
pip install torchvision
pip install pandas
pip install pyyaml
pip install tqdm
pip install seaborn
pip install wget
pip install pyserial
```

## 옵션 라이브러리 설치(여기부터는 음성 추가용, 추후 옵션으로 사용할 예정)
```python
pip install pip install speechrecognition
pip install pip install gtts
pip install pip install playsound
```

## 오류메시지
### 자동문을 여닫는 용도의 아두이노 우노를 USB포트에 연결하지 않았을 경우 이런 오류가 발생함, 연결하면 해결됨
```python
serial.serialutil.SerialException: could not open port '': FileNotFoundError(2, '지정된 경로를 찾을 수 없습니다.', None, 3)
```

## cmd와 폴더 이동
### 1. 윈도우 왼쪽 하단의 돋보기를 클릭하고 cmd를 쳐서 명령프롬프트를 연다.
### 2. 서버가 설치되어 있는 폴더로 이동한다. 
```cmd
cd C:\<시스템이 설치되어 있는 주소>\AI_seyong-main\3. kiosk\smartM_ai_server
```
### 3. 파이썬 프로그램으로 서버를 연다
```cmd
python smartM_ai_server_new.py
```

### 4. 다시 돋보기로 가서 cmd 명령어를 이용해 새로운 명령프롬프트를 연다.
### 5. 클라이언트가 설치되어 있는 폴더로 이동한다. 
```cmd
cd C:\<시스템이 설치되어 있는 주소>\AI_seyong-main\3. kiosk
```
### 5. 파이썬 프로그램으로 클라이언트를 연다
현재 자동으로 문이 열리는 부분은 주석처리 되어 있으므로, 이 기능을 살리려면 아래 파이썬 프로그램의 28~36번째 줄, 216번 줄을 주석해제하고 사용할 것  
```cmd
python kiosk.py
```
### 6. 명령프롬프트 창의 위치를 적당히 조정하고, 클라이언트 프로그램에서 결제하기 버튼을 눌러 결과를 확인함
#### 주의사항
- 하드웨어 세팅이 잘 되어 있지 않으면 결과물을 확인할 수 없음
- 카메라 두 대의 위치와 각도, 결과물로 보여지는 y축의 정렬이 정확해야 원하는 값을 얻을 수 있으므로, 하드웨어 세팅이 매우 중요함


