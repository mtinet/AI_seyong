# 세용

## python 설치(3.8버전으로 설치할 것)
[python 3.8.10 다운로드 링크](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)  

## 기본 라이브러리 설치(torch, torchvision을 최신 버전으로 설치하면 소스코드 일부를 수정해야 함)
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
### 아두이노 우노를 USB포트에 연결하지 않음
```python
serial.serialutil.SerialException: could not open port '': FileNotFoundError(2, '지정된 경로를 찾을 수 없습니다.', None, 3)
```

##
## 인공지능
### 데이터 수집하기
- 1. maskDetector/collectData.py

### 모델만들기
- 1. maskDetector/makeModel.py

### 마스크 디텍터
- 1. maskDetector/maskDetector.py


##
## 아두이노
### 적외선 센서를 사용한 아두이노 카운터
- 0.test/arduino/Bidirectional_counter/Bidirectional_counter.ino


##
## 파이썬-아두이노 통신하기
### 파이썬에서 값을 입력받아 아두이노에 전달, 1은 LED 켜기, 0은 LED 끄기
- 0.test/ledControl.py
- 0.test/arduino/ledOnOff_python/ledOnOff_python.ino

### 아두이노의 값을 파이썬에 전달하여 표시하기
- 0.test/arduino/valOutput_python/valOutput_python.ino - 숫자 올리기
- 0.test/valInput.py
- 1.maskDetector/arduino/Bidirectional_counter_python/Bidirectional_counter_python.ino


##
## 별첨
### 모자이크 처리하기, 카툰화하기
- 0.test/mosaic.py
- 0.test/cartoonize.py


##
## exe파일 만들기
- pyinstaller 설치

```python
pip install pyinstaller
```
- exe로 만들 파이썬 파일이 있는 폴더로 이동
- -w : 콘솔창 없애기
- -F : 하나의 파일로 만들기
- --ico : 아이콘 만들기

```python
pyinstaller -w -F --icon=logo.ico maskDetector.py
```

- 실행 파일을 만들고 실행파일 폴더 안에 model.h5 파일, cvlib, cvlib-0.2.6.dist-info폴더를 복사해 넣어야 함


