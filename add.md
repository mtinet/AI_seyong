# 프로그램 설치 방법

## 프로그램 다운로드
- 아래 링크에서 프로그램을 다운로드 받는다.  
[프로그램 다운로드](https://drive.google.com/file/d/1lKk5NDPP_T890f0dJTW6lMgdaqSoPFpP/view?usp=sharing)  
- 원하는 곳에 압축을 푼다. 
- 이 파일은 인공지능 학습을 위한 사진데이터를 모두 포함하고 있어 5기가 정도 용량이지만, 프로젝트를 위한 서버와 클라이언트는 부수적인 파일들은 필요하지 않다.  
- 서버 파일은 3.kiosk 폴더의 smartM_ai_server 폴더 안에 있는 smartM_ai_server_new.py 파일이다.  
- 클라이언트 파일은 3. kiosk 폴더에 kiosk.py 파일이다.  
- 전자제어 여닫이 문을 제어하는 파일은 3. kiosk 폴더의 doorOpenClose_python 폴더 안에 있는 doorOpenClose_python.ino 파일이다. 
- .py로 되어 있는 파일은 python으로 실행하고, .ino로 되어 있는 파일은 아두이노 IDE를 이용해 아두이노 우노보드에 업로드 하여 사용한다.  


## python 설치(3.8버전으로 설치할 것)
- 아래 링크를 클릭해 python 3.8.10 버전을 다운로드 받고 설치한다.  
[python 3.8.10 다운로드 링크](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)  
- 설치 화면 하단의 Add Python 3.8 to PATH를 반드시 체크하고 Install Now버튼을 눌러 설치한다.  
![image](https://user-images.githubusercontent.com/13882302/210344769-3c3108bf-fdfb-442d-9bef-95b968dac583.png)

## cmd를 통한 폴더 이동
![image](https://user-images.githubusercontent.com/13882302/210346348-55fc5098-b360-4945-b9ab-12275e734d1a.png)
- 탐색기를 열어 서버가 설치되어 있는 폴더로 이동 한 다음 위 그림처럼 주소창을 클릭하고 해당 폴더의 주소를 복사한다.  
![image](https://user-images.githubusercontent.com/13882302/210346494-8abfb3e2-b487-40a4-912f-c02180b50603.png)
- 윈도우 왼쪽 하단의 검색창을 열고 cmd를 입력한다음 엔터를 눌러 명령 프롬프트를 연다.  
![image](https://user-images.githubusercontent.com/13882302/210346603-1e19e823-5180-4676-90d8-e6c8a8135158.png)
- 명령 프롬프트가 열리면 아래 예시의 형태로 cd 명령어를 써서 서버 폴더로 이동한다. 위의 탐색기에서 복사한 주소를 붙여넣으면 된다.    
```cmd
cd C:\<압축을 푼 위치>\AI_seyong-main\3. kiosk\smartM_ai_server
```
- 폴더 이동이 잘 되면 아래 그림과 같은 형태로 폴더 위치를 확인할 수 있다.  
![image](https://user-images.githubusercontent.com/13882302/210348019-f4787201-9dd5-4488-901a-81316cc7a73f.png)
- dir명령어를 통해 해당 폴더에 들어있는 폴더와 파일을 볼 수 있다.  
![image](https://user-images.githubusercontent.com/13882302/210348135-770e05e1-9ef4-437f-b92d-a33aff55e673.png)


## 기본 라이브러리 설치  
- 아래 명령어를 순서대로 입력하여 모두 설치한다.  
- torch, torchvision을 최신 버전으로 설치하면 소스코드 일부를 수정해야 한다.  

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

# 프로그램 사용 방법
## 오류메시지
### 파이썬을 이용해 사용하는 라이브러리들이 제대로 설치가 되어 있지 않아서 발생하는 오류가 가장 많음. 위에 제시한 모든 라이브러리들이 제대로 설치되어 있어야 함
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
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/291fadee-88fa-448d-81c6-3d0405172606/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014219Z&X-Amz-Expires=86400&X-Amz-Signature=a01cffc8f29b469da1c4f5dbd32311665ec0ded8f508949243672b91bd600f84&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1bf48fc7-5f63-4960-a798-1828c5b08f25/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014756Z&X-Amz-Expires=86400&X-Amz-Signature=d76a2add47bc6cae78b0245c384120880aaacfee179adcf92df487b3af76543f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a1a7d405-68f6-46df-9c02-ad75a7cc343a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014817Z&X-Amz-Expires=86400&X-Amz-Signature=3bae274c20341c3e33a7c50702ef1aa548ce1e7d7c0eef3249aa360ed33c161d&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/977ab77d-9819-4727-9c4d-c43986b7acc8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014904Z&X-Amz-Expires=86400&X-Amz-Signature=3a89834013ac13c7bf48bb215d71407ed46567bb3e9237e88f8c610e5e991400&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
- 서버에 표현되는 결과 로그에서 추정된 결과값 bpred의 값 아래쪽에 같은 상품명이 2개가 모두 찍혀야 해당 상품이 키오스크의 값으로 들어가게 설정되어 있음. 이는 오작동을 줄이기 위해 카메라를 2대를 세팅해서 각각 해당 카메라에 들어온 값이 온전하느냐를 판별하기 위함임  
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d6790a11-7093-40cd-b9a1-53511324cce9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T015000Z&X-Amz-Expires=86400&X-Amz-Signature=4bc4f4616b9dc902eb665384c9e6cd44193fb8ff8969484c319386a35d43b3ee&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/67a8385e-1776-437d-aeb3-a867167b340c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014925Z&X-Amz-Expires=86400&X-Amz-Signature=c01a2070607bcfe8681bc45a5861b6e20e8e4cb5cf5b269d2580b4f8a2e404b3&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)


### 7. 여닫이 문을 자동제어 하려면, 아두이노 코드가 설치되어 있는 폴더로 이동한다. 
현재 자동으로 문이 열리는 부분은 주석처리 되어 있으므로, 이 기능을 살리려면 kiosk.py 파이썬 프로그램의 28~36번째 줄, 216번 줄을 주석해제하고 사용할 것
```cmd
cd C:\<시스템이 설치되어 있는 주소>\AI_seyong-main\3. kiosk\doorOpenClose_python
```
안에 있는 doorOpenClose_python.ino 파일을 아두이노 IDE를 이용해 아두이노 우노보드에 업로드 하고, 인공지능 키오스크 클라이언트가 구동되는 컴퓨터에 USB케이블로 연결해 놓는다. 아두이노의 13번 핀을 이용해 여닫이 문에 설치된 릴레이를 제어하도록 코딩되어 있음.
