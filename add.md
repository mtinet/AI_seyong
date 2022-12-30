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

